# -*- coding: utf-8 -*-

from typing import Text
from unicodedata import normalize as nl

def normalize_unicode_text(text: Text=None):
    text = nl('NFKC', text)

    return text

def lower_text(text: Text=None):

    return text.lower()

def find_sublist_in_list(sublist: list=None, list: list=None):
    results = []
    len_sublist = len(sublist)

    for idx in (i for i, e in enumerate(list) if e == sublist[0]):
        if list[idx: idx + len_sublist] == sublist:
            results.append((idx, idx + len_sublist - 1))
    
    return results