# -*- coding: utf-8 -*-
# Provide function to augmentation data

import random

from typing import Text

def abbreviates_func(text: Text, replace_prob: float=0.5):
    
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
