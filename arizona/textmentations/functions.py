# -*- coding: utf-8 -*-
# Provide function to augmentation data

import os
import copy
import random

from typing import Text
from arizona.textmentations.io import load_json
from arizona.textmentations.utils import find_sublist_in_list, lower_text, replace_sublist, get_new_tags

def abbreviates_func(
    text: Text=None, 
    replace_thresold: float=0.5, 
    num_samples: int=5,
    lowercase: bool=True,
    config_file: str='configs/abbreviations.json',
    intent: Text=None,
    tags: Text=None,
    **kwargs
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

    data = load_json(os.path.abspath(config_file))
    abbreviations_words = data.get('examples', {})
    
    if lowercase:
        text = lower_text(text)

    list_words = text.split(" ")
    list_tags = tags.split(" ")

    output_data = {
        "text": [],
        "intent": [],
        "tags": []
    }

    assert len(list_words) == len(list_tags), f"Error: `{text}`. The numbers words must be equal to the number of tags."

    # _words = copy.deepcopy(list_words)

    for i in range(num_samples):
        for key, value in abbreviations_words.items():
            if lowercase:
                abb_word = [i.lower() for i in key.split(" ")]
            else:
                abb_word = key.split(" ")

            indexes = find_sublist_in_list(sublist=abb_word, list=list_words)
            for index in indexes:
                for candidate in value:
                    candidate = candidate.split(" ")
                    rd = random.random()
                    if rd >= replace_thresold:
                        # Generate new tags
                        newtags = get_new_tags(tags=list_tags[index[0]: index[1] + 1], length=len(candidate))
                        list_words = replace_sublist(candidate, list_words, index[0], index[1])
                        list_tags = replace_sublist(newtags, list_tags, index[0], index[1])
                        break
        
        output_data["text"].append(' '.join(list_words))
        output_data["intent"].append(intent)
        output_data["tags"].append(' '.join(tags))
    
    return output_data

def remove_accent_func(
    text: Text=None, 
    replace_thresold: float=0.5, 
    num_samples: int=5, 
    lowercase: bool=True,
    intent: Text=None,
    tags: Text=None,
    **kwargs
):
    s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
    
    output_data = {
        "text": [],
        "intent": [],
        "tags": []
    }

    for i in range(num_samples):
        textout = ''
        for char in text:
            if char in s1:
                rd = random.random()
                if rd >= replace_thresold:
                    textout += s0[s1.index(char)]
                else:
                    textout += char
            else:
                textout += char

        if lowercase:
            textout = lowercase(textout)
        
        output_data["text"].append(textout)
        output_data["intent"].append(intent)
        output_data["tags"].append(' '.join(tags))

    return output_data


def keyboard_func(
    text: Text, 
    replace_thresold: float=0.5, 
    **kwargs
):
    
    return 
