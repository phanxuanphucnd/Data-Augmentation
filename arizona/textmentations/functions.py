# -*- coding: utf-8 -*-
# Provide function to augmentation data

import os
import copy
import random
import augly.text as textaugs

from typing import Text
from arizona.textmentations.io import load_json
from arizona.textmentations.utils import find_sublist_in_list, lower_text, replace_sublist, get_new_tags

def abbreviates_func(
    text: Text=None, 
    intent: Text=None,
    tags: Text=None,
    replace_thresold: float=0.5, 
    num_samples: int=5,
    lowercase: bool=True,
    config_file: str='configs/abbreviations.json',
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

    for i in range(num_samples):
        list_words = text.split(" ")
        list_tags = tags.split(" ")
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
        output_data["tags"].append(' '.join(list_tags))
    
    return output_data

def remove_accent_func(
    text: Text=None, 
    intent: Text=None,
    tags: Text=None,
    replace_thresold: float=0.5, 
    num_samples: int=5, 
    lowercase: bool=True,
    **kwargs
):
    s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
    
    output_data = {
        "text": [],
        "intent": [],
        "tags": []
    }

    if lowercase:
        text = lower_text(text)

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
        
        output_data["text"].append(textout)
        output_data["intent"].append(intent)
        output_data["tags"].append(tags)

    return output_data

def keyboard_func(
    text: Text, 
    intent: Text=None, 
    tags: Text=None,
    replace_thresold: float=0.5, 
    num_samples: int=5, 
    lowercase: bool=True,  
    aug_char_percent: float=0.2,
    aug_word_percent: float=0.1,
    unikey_percent: float=0.5,
    config_file: str='configs/unikey.json',
    **kwargs
):
    unikey_numbers = int(unikey_percent * num_samples)
    keyboard_numbers = num_samples - unikey_numbers
    maps = load_json(config_file)
    viunikey = maps.get('examples', {})

    if lowercase:
        text = lower_text(text)
    
    output_data = {
        "text": [],
        "intent": [],
        "tags": []
    }

    for i in range(unikey_numbers):
        textlist = []
        for word in text.split(" "):
            chartmp = ''
            chars = [c for c in word]
            rd = random.random()
            if rd >= replace_thresold:
                for i, c in enumerate(chars):
                    if (c in viunikey.keys()):
                        chars[i] = viunikey[c][0]
                        chartmp = viunikey[c][1]
                    if (i == len(chars) - 1):
                        word = ''.join(chars) + chartmp

            textlist.append(word)

        textout = " ".join(textlist)
        output_data["text"].append(textout)
        output_data["intent"].append(intent)
        output_data["tags"].append(tags)

    keyboard_outputs = textaugs.simulate_typos(
        text, 
        aug_char_p=aug_char_percent, 
        aug_word_p=aug_word_percent, 
        n=keyboard_numbers
    )

    for textout in keyboard_outputs:
        output_data["text"].append(textout)
        output_data["intent"].append(intent)
        output_data["tags"].append(tags)

    return output_data
