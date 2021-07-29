from arizona.textmentations.utils import line_csv_to_dict_output
from arizona.textmentations.io import convert_yaml_to_csv, convert_csv_to_json

def test_convert_yaml_to_csv():
    path = './data/nlu.yml'
    df = convert_yaml_to_csv(data=path)
    print(df)

# test_convert_yaml_to_csv()

def test_line_csv_to_dict_output():
    a = line_csv_to_dict_output(
        text="tôi là Phúc Phan",
        intent="inform",
        tags="O O B-Name I-Name"
    )
    print(a)

def test_convert_csv_to_json():
    data = convert_csv_to_json(
        data='data/test.csv',
        text_col='text',
        intent_col='intent',
        tags_col='tags',
        export_dir='./data',
        export_file='nlu.json'
    )
    print(data)

test_convert_csv_to_json()