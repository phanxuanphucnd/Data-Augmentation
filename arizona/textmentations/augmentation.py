# -*- coding: utf-8 -*-

import os

from typing import List, Text, Union

class TextAugmentation:
    def __init__(self) -> None:
        pass
    
    def augment(
        self, 
        methods: Union[List[dict], dict], 
        export_folder: Text='./data/',
        export_file: Text='aug_data.csv'
    ):

        raise NotImplementedError
