[![PyPI - Python](https://img.shields.io/badge/py%203.7%20-blue.svg)]()
[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/phanxuanphucnd/Data-Augumentation/blob/main/LICENSE)
[![Open In Jupyter notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/phanxuanphucnd/Data-Augumentation/blob/main/tutorials/tutorial.ipynb)

<img src="docs/imgs/textmentations.gif" width="45%" height="45%" align="right" />

## Table of contents

1. [Introduction](#introduction)
2. [How to use `arizona textmentations`](#how_to_use)
    - [Installation](#installation)
    - [Data structure](#data_structure)
    - [Example usage](#usage)


## <a name='introduction'></a> Introduction

**Arizona textmentations** is a library to augment Text data for the Nature Language Understanding (NLU) problem, an important component in building chatbots. The library is built on some approaches as follows:

- ``remove_accent``: Remove the accents of some characters according to a random distribution.
- ``abbreviation``: Replace some correctly spelled-words with Vietnamese abbreviation-words in Vietnamese, following ours trend in social networks.
- ``keyboard``: Based on how we can enter the wrong keys, or unikey in Vietnamese.

## <a name='how_to_use'></a> How to use `arizona textmentations`

### Installation <a name='installation'></a>

```js
>>> pip install dist/arizona-0.0.1-py3-none-any.whl
```

### <a name='data_structure'></a> Data Structure

The input maybe a text sentence or a .csv file contains 3 columns:

| text | intent | tags |
| ---- | ------ | ---- | 
| tôi là Phúc | inform | O O B-people |

### <a name='usage'></a> Example usage

- Input: A TEXT

```py
from arizona.textmentations.functions import abbreviates_func

text = "giới thiệu về công ty abc"

results = abbreviates_func(
    text,
    num_samples=10,
    intent='faq_company',
    tags='O O O B-work_unit I-word_unit I-work_unit',
    config_file='configs/abbreviations.json'
)

from pprint import pprint
pprint(results)


from arizona.textmentations.functions import keyboard_func

text = "giới thiệu về công ty abc"

results = keyboard_func(
    text,
    num_samples=10,
    intent='faq_company',
    tags='O O O B-work_unit I-word_unit I-work_unit',
    aug_char_percent=0.2,
    aug_word_percent=0.1,
    unikey_percent=0.5,
    config_file='configs/unikey.json',
)

from pprint import pprint
pprint(results)


from arizona.textmentations.functions import remove_accent_func

text = "giới thiệu về công ty abc"

results = remove_accent_func(
    text,
    num_samples=5,
    intent='faq_company',
    tags='O O O B-work_unit I-word_unit I-work_unit'
)

from pprint import pprint
pprint(results)

```

- Input: A `.csv` FILE

```py
from arizona.textmentations import TextAugmentation

path = './data/nlu.csv'

text_augs = TextAugmentation(
    data=path,
    text_col='text',
    intent_col='intent',
    tags_col='tags'
)

text_augs.augment(
    methods=['remove_accent', 'abbreviation', 'keyboard'],
    without_origin_data=True
)
```

## License

```
MIT License

Copyright (c) 2021 Phuc Phan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
  
## Author

**Arizona textmentations** was developed by Phuc Phan © Copyright 2021.

For any questions or comments, please contact the following email: phanxuanphucnd@gmail.com

Thank you for your interesting to ``Arizona textmentations``!