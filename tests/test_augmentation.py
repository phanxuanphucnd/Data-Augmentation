from arizona.textmentations import TextAugmentation

path = './data/train.csv'

text_augs = TextAugmentation(
    data=path,
    text_col='text',
    intent_col='intent',
    tags_col='tags'
)

text_augs.augment(
    methods={
        "remove_accent": {
            "replace_thresold": 0.3,
            "num_samples": 10,
            "lowercase": True
        }, 
        "abbreviation": {
            "replace_thresold": 0.5,
            "num_samples": 10,
            "lowercase": True,
            "config_file": "configs/abbreviations.json"
            }, 
        "keyboard": {
            "replace_thresold": 0.5,
            "num_samples": 10,
            "lowercase": True,
            "aug_char_percent": 0.2,
            "aug_word_percent": 0.1,
            "unikey_percent": 0.6,
            "config_file": "configs/unikey.json"
        }
    },
    without_origin_data=False,
    write_file=True,
    export_dir='./output',
    export_file='train-aug.csv'
)