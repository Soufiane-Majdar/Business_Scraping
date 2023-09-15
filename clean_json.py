import json
import re

def clean_json():
    with open('business_data.json', 'r') as json_file:
        data = json.load(json_file)

    for i in range(len(data)):
        for key in data[i]:
            if isinstance(data[i][key], str):
                data[i][key] = re.sub(r'\\u00e9', 'é', data[i][key])
                data[i][key] = re.sub(r'\\u00e0', 'à', data[i][key])
                data[i][key] =  re.sub(r'\\u00e8', 'è', data[i][key])
                data[i][key] =  re.sub(r'\\u2019', '’', data[i][key])
                data[i][key] =  re.sub(r'\\u00e2', 'â', data[i][key])
                data[i][key] =  re.sub(r'\\u00fb', 'û', data[i][key])
                data[i][key] =  re.sub(r'\\u00e7', 'ç', data[i][key])
                data[i][key] =  re.sub(r'\\u00ee', 'î', data[i][key])
                data[i][key] =  re.sub(r'\\u00f4', 'ô', data[i][key])
                data[i][key] =  re.sub(r'\\u00e3', 'ã', data[i][key])
                data[i][key] =  re.sub(r'\\u00f9', 'ù', data[i][key])
                data[i][key] =  re.sub(r'\\u00e4', 'ä', data[i][key])
                data[i][key] =  re.sub(r'\\u00f6', 'ö', data[i][key])
                data[i][key] =  re.sub(r'\\u00e5', 'å', data[i][key])
                data[i][key] =  re.sub(r'\\u00f8', 'ø', data[i][key])
                data[i][key] =  re.sub(r'\\u00e6', 'æ', data[i][key])
                data[i][key] =  re.sub(r'\\u00f1', 'ñ', data[i][key])
                data[i][key] =  re.sub(r'\\u00fc', 'ü', data[i][key])
                data[i][key] =  re.sub(r'\\u00e7', 'ç', data[i][key])
                data[i][key] =  re.sub(r'\\u00cf', 'Ï', data[i][key])
                data[i][key] =  re.sub(r'\\u00c9', 'É', data[i][key])
                data[i][key] =  re.sub(r'\\u00c8', 'È', data[i][key])
                data[i][key] =  re.sub(r'\\u00c0', 'À', data[i][key])
                data[i][key] =  re.sub(r'\\u00c2', 'Â', data[i][key])
                data[i][key] =  re.sub(r'\\u00c7', 'Ç', data[i][key])
                data[i][key] =  re.sub(r'\\u00c3', 'Ã', data[i][key])
                data[i][key] =  re.sub(r'\\u00c6', 'Æ', data[i][key])
                data[i][key] =  re.sub(r'\\u00c4', 'Ä', data[i][key])
                data[i][key] =  re.sub(r'\\u00c5', 'Å', data[i][key])
                data[i][key] =  re.sub(r'\\u00c1', 'Á', data[i][key])


    with open('business_data_clean.json', 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print('Business URLs cleaned successfully.')

clean_json()
