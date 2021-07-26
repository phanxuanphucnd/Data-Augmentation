# -*- coding: utf-8 -*-

import os

from pandas import DataFrame
from typing import List, Text, Union

from arizona.textmentations.functions import *

class TextAugmentation:
    def __init__(self, data: DataFrame=None, text_col) -> None:
        super(TextAugmentation, self).__init__()
        
        self.data = data
    
    def augment(
        self, 
        methods: Union[List[dict], dict], 
        export_dir: Text='./output/',
        export_file: Text='aug_data.csv'
    ):
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        raise NotImplementedError
