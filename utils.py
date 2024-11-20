import os
import re
import json

ZH_PATTERN = r'[\u4e00-\u9fa5]+'
DATA = os.path.join(os.path.dirname(__file__), 'data', '%s.json')

def svj(j: dict, nm: str) -> None:
    open(DATA % nm, 'wb').write(json.dumps(
        j, ensure_ascii=False, indent=4
    ).encode('utf8'))


def rdj(nm: str) -> dict:
    return json.loads(open(DATA % nm, 'rb').read().decode('utf8'))
