### SUPAHAXOR ###
### RenPy to cJSON parser ###
### 11/06/2025 ###

import re
import json

dialogues = []
print("Hello World")

with open('script-ch0.rpy', "r", encoding='utf-8') as file:
    
    lines = file.readlines()

for line in lines:

    line = line.strip()
    ### SKIP COMMENT OR BLANK LINES ###

    if not line or line.startswith('#'):
        continue

    match = re.match(r'(?:(\w+)(?: \w+)? )?"(.+?)"', line)
    if match:
        speaker = match.group(1) if match.group(1) else "Narrator"
        text = match.group(2)
        dialogues.append((speaker, text))

for speaker, text in dialogues[:10]:
    print(f"{speaker}: {text}")

