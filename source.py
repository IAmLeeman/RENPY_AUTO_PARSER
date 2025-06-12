### SUPAHAXOR ###
### RenPy to cJSON parser ###
### 12/06/2025 ###

import re
import json

char_map = {
    "s": "Sayori",
    "m": "Monika",
    "y": "Yuri",
    "n": "Natsuki",
    "mc": "MC"
}

dialogues = []


with open('script-ch0.rpy', "r", encoding='utf-8') as file:
    
    lines = file.readlines()

for line in lines:

    line = line.strip()
    ### SKIP COMMENT OR BLANK LINES ###

    if not line or line.startswith('#'):
        continue

    match = re.match(r'(\w+)\s+(\w+)\s+"(.+?)"', line)  ### REGEX -- Great...
    if match:

        char_code = match.group(1)
        sprite_code = match.group(2)
        text = match.group(3)

        
        character = char_map.get(char_code, "Unknown")
        sprite = character.lower() + sprite_code

        data = {
        "text": text,
        "character": character,
        "sprite": sprite 
        }

        escaped = json.dumps(data).replace('"', '\\"')
        print(f"\"{escaped}\"")

    else:
        match = re.search(r'"(.+?)"', line)
        if match:
            text = match.group(1)
            data = {
                "text": text,
                 "character": "Narrator",
                "sprite": ""
            }
            json_str = json.dumps(data).replace('"', '\\"')
            dialogues.append(f"\"{json_str}\"")

with open("output.txt", "w", encoding="utf-8") as out_file:
    for line in dialogues:
        out_file.write(line + "\n")

print("Done. Wrote output.txt with all dialogue lines.")
