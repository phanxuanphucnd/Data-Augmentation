from arizona.textmentations.functions import abbreviates_func

text = "giới thiệu về công ty ftech"

results = abbreviates_func(
    text,
    num_samples=10,
    intent='faq_company',
    tags='O O O B-work_unit I-word_unit I-work_unit',
    config_file='configs/abbreviations.json'
)

from pprint import pprint
pprint(results)