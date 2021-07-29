from arizona.textmentations.functions import keyboard_func

text = "giới thiệu về công ty ftech"

results = keyboard_func(
    text,
    num_samples=5,
    intent='faq_company',
    tags='O O O B-work_unit I-word_unit I-work_unit',
    aug_char_percent=0.2,
    aug_word_percent=0.1,
    unikey_percent=0.5,
    config_file='configs/unikey.json',
)

from pprint import pprint
pprint(results)