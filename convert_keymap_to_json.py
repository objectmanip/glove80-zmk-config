import os
import json

keymap_path = "./config/glove80.keymap"
json_path = "./config/keymap.json"

json_template = {"keyboard": "glove80", "keymap": "default", "layout": "LAYOUT", "layer_names": [], "layers": []}

with open(keymap_path, "r", encoding='utf-8') as kmf:
    keymap_content = kmf.readlines()

section = ""
layer_information = []
for line in keymap_content:
    # get behaviors:
    if line.strip().startswith("behaviors {"):
        section = "behaviors"
    elif line.strip().startswith("macros {"):
        section = "macros"
    elif line.strip().startswith("combos {"):
        section = "combos"
    elif line.strip().startswith("keymap {"):
        section = "keymap"

    if section == "behaviors":
        pass
    elif section == "macros":
        pass
    elif section == "combos":
        pass
    elif section == "keymap":
        if "{" in line:
            layer_name = line.split(" ")[0].strip()
            json_template["layer_names"].append(layer_name)
            layer_information.append([])
            print(f"parsing {layer_name}")
        if "label = " in line:
            layer_label = line.split(" ")[-1][:-2].strip("\"")
            print(layer_label)
        key_commands = line.split("&")
        if len(key_commands) < 2:
            continue
        for km in key_commands:
            components = km.strip().split(" ")
            key_function = components[0]
            key_codes = components[1:]
            key_entry = {"value": f"&{key_function}", "params": [{"value": key_code, "params": []} for key_code in key_codes]}
            layer_information[-1].append(key_entry)
print(layer_information)


