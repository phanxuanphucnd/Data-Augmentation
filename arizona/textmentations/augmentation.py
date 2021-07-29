# -*- coding: utf-8 -*-

import os
import pandas as pd

from tqdm import tqdm
from pandas import DataFrame
from typing import List, Text, Union

from arizona.textmentations.functions import *
from arizona.textmentations.io import load_json
from arizona.textmentations.utils import get_from_registry

class TextAugmentation:
    def __init__(
        self, 
        data: Union[DataFrame, Text]=None, 
        text_col: Text='text', 
        intent_col: Text='intent', 
        tags_col: Text='tags'
    ) -> None:
        super(TextAugmentation, self).__init__()
        
        if isinstance(data, Text):
            data = pd.read_csv(data, encoding='utf-8')

        self.data = data
        self.text_col = text_col
        self.intent_col = intent_col
        self.tags_col = tags_col

    @staticmethod
    def get_default_params(method, config_file: Text='configs/default.json'):
        default = load_json(config_file)

        params = []
        if method in default:
            params = default.get(method.lower())
        else:
            raise ValueError(
                f"Method name `{method}` not supported, available options: {default.keys()}"
            )

        return params
    
    def augment(
        self, 
        methods: Union[dict, List[Text]], 
        without_origin_data: bool=False,
        export_dir: Text='./output/',
        export_file: Text='aug_data.csv'
    ):
        # Methods examples: 
        # methods= {
        #   "abbreviations": {
        #                       "replace_thresold": 0.5, 
        #                       "num_samples": 10, 
        #                       "lowercase": true, 
        #                       "config_file": "configs/abbreviations.json"},
        #   "remove_accent": {
        #                       "replace_thresold": 0.5, 
        #                       "num_samples": 10, 
        #                       "lowercase": true
        #                    }
        #   "keyboard": {
        #                   "replace_thresold": 0.5, 
        #                   "num_samples": 10, 
        #                   "lowercase": true, 
        #                   "aug_char_percent": 0.2, 
        #                   "aug_word_percent": 0.1, 
        #                   "unikey_percent": 0.intent: Text=None,
        #                   "config_file": "configs/unikey.json"
        #               }
        # }

        if not os.path.exists(export_dir):
            os.makedirs(export_dir)
        
        if isinstance(methods, List):
            temp = {}
            for method in methods:
                _params = self.get_default_params(method)
                temp[method] = _params
            methods = temp

        outdata = {
            'text': [],
            'intent': [],
            'tags': []
        }
        for i in tqdm(range(len(self.data))):
            for method, params in methods.items():
                results = get_build_method(method.lower())(
                    self.data[self.text_col][i],
                    self.data[self.intent_col][i],
                    self.data[self.tags_col][i],
                    **params
                )

                outdata['text'].extend(results['text'])
                outdata['intent'].extend(results['intent'])
                outdata['tags'].extend(results['tags'])

        data_df = pd.DataFrame.from_dict(outdata)
        
        # TODO: Drop duplicates
        data_df = data_df.drop_duplicates(subset=self.text_col, keep='first')

        if without_origin_data:
            df = data_df
        else:
            df = self.data + data_df
        
        # TODO: Write to a file
        save_path = os.path.join(export_dir, export_file)
        df.to_csv(save_path, encoding='utf-8', index=False)

        return df


def get_build_method(method_type):
    return get_from_registry(method_type, methods_registry)

methods_registry = {
    'keyboard': keyboard_func,
    'abbreviation': abbreviates_func,
    'remove_accent': remove_accent_func
}
