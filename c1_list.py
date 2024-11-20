from utils import *
import pypinyin

clean_data = rdj('b_clean')
dictionary: list = list(clean_data.keys())

item = '女武神'
dictionary += clean_data[item].keys()
for role in clean_data[item]:
    dictionary += clean_data[item][role].keys()
    for build in clean_data[item][role]:
        dictionary += clean_data[item][role][build]
        for dress in clean_data[item][role][build]:
            matches = re.findall(ZH_PATTERN, dress)
            dictionary.append(''.join(matches))
            dictionary += matches
        del dress

for item in ['人偶', '协同者', '宿舍名册', '圣痕', '武器', '敌人']:
    dictionary += clean_data[item]
    for name in clean_data[item]:
        matches = re.findall(ZH_PATTERN, name)
        if len(matches) < 1:
            continue
        dictionary.append(''.join(matches))
        dictionary += matches

dictionary = sorted([i for i in set(dictionary) if len(i) > 1])
svj(dictionary, 'dictionary')
# svj({'dictionary': dictionary}, 'dictionary')
