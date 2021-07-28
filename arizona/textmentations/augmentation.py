# -*- coding: utf-8 -*-

import os
import pandas as pd

from pandas import DataFrame
from typing import List, Text, Union

from arizona.textmentations.functions import *
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
    
    def augment(
        self, 
        methods: Union[List[dict], dict], 
        export_dir: Text='./output/',
        export_file: Text='aug_data.csv'
    ):
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        raise NotImplementedError


def get_build_method(method_type):
    return get_from_registry(method_type, methods_registry)

    
methods_registry = {
    'keyboard': keyboard_func,
    'abbreviation': abbreviates_func,
    'remove_accent': remove_accent_func
}
