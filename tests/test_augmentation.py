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