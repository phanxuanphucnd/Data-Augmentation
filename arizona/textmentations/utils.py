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

def replace_sublist(
    sublist: list=None, 
    list: list=None, 
    start_idx: int=None, 
    end_idx: int=None
):
    list[start_idx: end_idx + 1] = sublist

    return list

def get_new_tags(
    tags: list=None,
    length: int=None
):
    tag_name = tags[0].split("-")[-1]
    newtags = ['B-' + tag_name if i == 0 else 'I-' + tag_name for i in range(length)]

    return newtags

def line_csv_to_dict_output(text, intent, tags):
    """
    Convert outputs in rasa's format
    
    Args:
        text: Text column
        intent: Intent column
        tags: Tags column

    Returns: 
        A result as rasa format. Example: \n
            [{  \n
                'confidence': confidence, \n 
                'end': end, \n
                'start': start, \n
                'entity': entity, \n
                'extractor': extractor, \n
                'value': value  \n
            }] \n
    """
    rasa_output = {}
    rasa_output["text"] = text
    rasa_output["intent"] = intent
    tags = tags.split(' ')
    words = text.split(' ')

    # get index start words
    ids = [0]
    temp = 0
    for i in range(1, len(words)):
        ids.append(temp + len(words[i-1]) + 1)
        temp = ids[-1]
    ids.append(len(rasa_output["text"]) + 1)

    entities = []
    start = 0
    entity = None
    end = 0
    ping = False

    for i in range(len(tags)):
        if ping == True:
            if tags[i] == 'O':
                end = i
                entities.append({
                    'entity': entity, 
                    'start': ids[start], 
                    'end': ids[end] - 1,                     
                    'value': ' '.join(words[start:end]).strip()
                })
                ping = False

            elif ("B-" in tags[i]) and (i == len(tags) - 1):
                end = i
                entities.append({
                    'entity': entity, 
                    'start': ids[start], 
                    'end': ids[end] - 1,                     
                    'value': ' '.join(words[start:end]).strip()
                })

                start = i
                end = i + 1
                entity = tags[i][2:]

                entities.append({
                    'entity': entity, 
                    'start': ids[start], 
                    'end': ids[end] - 1,
                    'value': ' '.join(words[start:end]).strip()
                })

            elif "B-" in tags[i]:
                end = i
                entities.append({
                    'entity': entity, 
                    'start': ids[start], 
                    'end': ids[end] - 1,                     
                    'value': ' '.join(words[start:end]).strip()
                })
                ping = True
                start = i
                entity = tags[i][2:]

            elif i == len(tags) - 1:
                end = i + 1
                entities.append({
                    'entity': entity, 
                    'start': ids[start], 
                    'end': ids[end] - 1,
                    'value': ' '.join(words[start:end]).strip()
                })

        else:
            if "B-" in tags[i] and i == len(tags) - 1:
                start = i
                end = i + 1
                entity = tags[i][2:]
                entities.append({
                    'entity': entity, 
                    'start': ids[start], 
                    'end': ids[end] - 1,
                    'value': ' '.join(words[start:end]).strip()
                })

            elif "B-" in tags[i]:
                start = i
                entity = tags[i][2:]
                ping = True

    rasa_output["entities"] = entities

    return rasa_output

def get_from_registry(key, registry):
    if hasattr(key, 'lower'):
        key = key.lower()

    if key in registry:
        return registry[key]
    else:
        raise ValueError(
            f"Key `{key}` not supported, available options: {registry.keys()}"
        )
