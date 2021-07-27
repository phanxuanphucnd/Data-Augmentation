from arizona.textmentations.io import convert_yaml_to_csv
from arizona.textmentations.utils import line_csv_to_json_output

def test_convert_yaml_to_csv():
    path = './data/nlu.yml'


    df = convert_yaml_to_csv(data=path)

    print(df)

test_convert_yaml_to_csv()

a = line_csv_to_json_output(
    text="tôi là Phúc Phan",
    intent="inform",
    tags="O O B-Name I-Name"
)

print(a)