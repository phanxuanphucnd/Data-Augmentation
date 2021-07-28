from augly import text
from arizona.textmentations.functions import remove_accent_func

text = "giới thiệu về công ty ftech"

results = remove_accent_func(
    text,
    num_samples=5,
    intent='faq_company',
    tags='O O O B-work_unit I-word_unit I-work_unit'
)

from pprint import pprint
pprint(results)