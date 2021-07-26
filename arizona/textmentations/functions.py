# -*- coding: utf-8 -*-
# Provide function to augmentation data

import os
import random

from typing import Text

from arizona.textmentations.io import load_json
from arizona.textmentations.utils import find_sublist_in_list

def abbreviates_func(
    text: Text=None, 
    replace_prob: float=0.5, 
    config_file: str='configs/abbreviations.json'
):
    # Check config file
    if not os.path.exists(config_file):
        raise ValueError(
            f"The `config_file` path not exists or broken ! "
            f"Please check `config_file` from path {config_file}. "
        )
    elif not config_file.endswith('.json'):
        raise ValueError(
            f"The `config_file` must be .json format. "
            f"Please check `config_file` from path {config_file}. "
        )

    abbreviations_words = load_json(os.path.abspath(config_file))

    for 
    
    return 

def remove_accent_func(text: Text, replace_prob: float=0.5):
    s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
    
    output = ''
    for char in text:
        if char in s1:
            rd = random.random()
            if rd >= replace_prob:
                output += s0[s1.index(char)]
            else:
                output += char
        else:
            output += char

    return output


def keyboard_func(text: Text, replace_prob: float=0.5):
    
    return 
