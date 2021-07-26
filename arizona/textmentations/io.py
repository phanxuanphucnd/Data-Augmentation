# -*- coding: utf-8 -*-
# Provide function loads/ dumps data

import os
import json
import regex

from pandas import DataFrame
from typing import Pattern, Text, Union, Any

def get_emoji_regex() -> Pattern:
    """Returns regex to identify emojis."""
    return regex.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\u200d"  # zero width joiner
        "\u200c"  # zero width non-joiner
        "]+",
        flags=regex.UNICODE,
    )

def convert_csv_to_yaml(
    data: Union[DataFrame, Text]=None, 
    text_col: Text='text', 
    intent_col: Text='intent', 
    tags_col: Text='tags',
    export_dir: Text='./output/',
    export_file: Text='data.yaml'
):
    """
    Function to convert csv format to yaml format.

    Args:
        data: A DataFrame or Path to the data .csv format.
        text_col: The text column name.
        intent_col: The intent column name. `intent_col` must be not None.
        tags_col: The tags column name. If None, the output not has entities.
        export_dir: The path to the directory to storages file.
        export_file: The path to the stored file.

    Returns:
        A file yaml storaged in `export_file`.
    """
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    return

def convert_yaml_to_csv(
    data: Union[Text, Any]=None,
    text_col: Text='text',
    intent_col: Text='intent',
    tags_col: Text='tags',
    export_dir: Text='./output/',
    export_file: Text='data.csv'
):
    """
    Function to convert yaml format to csv format.

    Args:
        data: A path to the data yaml format.
        text_col: The text column name.
        intent_col: The intent column name. `intent_col` must be not None.
        tags_col: The tags column name. If None, the output not has entities.
        export_dir: The path to the directory to storages file.
        export_file: The path to the stored file.

    Returns:
        A file csv storaged in `export_file` if not None, else return a DataFrame.
    """
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    return

def convert_json_to_csv(
    data: Union[Text, Any]=None,
    text_col: Text='text',
    intent_col: Text='intent',
    tags_col: Text='tags',
    export_dir: Text='./output/',
    export_file: Text='data.csv'
):
    """
    Function to convert json format to csv format.

    Args:
        data: A path to the data json format.
        text_col: The text column name.
        intent_col: The intent column name. `intent_col` must be not None.
        tags_col: The tags column name. If None, the output not has entities.
        export_dir: The path to the directory to storages file.
        export_file: The path to the stored file.

    Returns:
        A file csv storaged in `export_file` if not None, else return a DataFrame.
    """
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    return

def convert_csv_to_json(
    data: Union[DataFrame, Text]=None, 
    text_col: Text='text', 
    intent_col: Text='intent', 
    tags_col: Text='tags',
    export_dir: Text='./output/',
    export_file: Text='data.json'
):
    """
    Function to convert csv format to json format.

    Args:
        data: A DataFrame or Path to the data .csv format.
        text_col: The text column name.
        intent_col: The intent column name. `intent_col` must be not None.
        tags_col: The tags column name. If None, the output not has entities.
        export_dir: The path to the directory to storages file.
        export_file: The path to the stored file.

    Returns:
        A file json storaged in `export_file`.
    """
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    return


def load_json(file: Text=None):
    """
    Function load a json file.

    Args:
        file: The file to load the object from.

    Returns:
        The loaded object.
    """
    with open(file) as json_file:
        data = json.load(json_file)

    return data

def dumps_json(data, export_dir: Text='./output/', export_file: Text='data.json'):
    """
    Function dumps a json file.

    Args:
        export_dir: The path to the directory to storages file.
        export_file: The path to the stored json file.

    Returns:
        The path to the stored json file.
    """
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
        
    EXPORT_FILE_PATH = os.path.join(export_dir, export_file)
    with open(EXPORT_FILE_PATH, "w") as f:
        json.dump(data, f, sort_keys=True, indent=2)

    return EXPORT_FILE_PATH