import re
import markdown
import os
import shlex
from scripts.parse import parse_all_commands
from scripts.commands import *
from scripts.exif_remover import exif_cleanse

init_cmd_dict = {
    "priority": set_priority,
    "id": set_id,
}

cmd_dict = {
    "set": set_context,
    "fill_template": fill_template,
    "set_from_md_file": set_context_from_md_file,
    "set_from_file": set_context_from_file,
    "globalset": globalset_context,
    "globalset_from_file": globalset_context_from_file,
    "globalset_from_md_file": globalset_context_from_md_file,
    "globalappend": globalappend_context,
    "globalappend_from_file": globalappend_context_from_file,
    "globalappend_from_md_file": globalappend_context_from_md_file,
    "priority": do_nothing,
    "id": do_nothing,
}

global_context = dict()
objects = []

class object:
    priority = 0
    context = dict()
    cmds = []
    glob = global_context
    all_objects = objects
    id = "Unnamed"

    def __init__(self, file_path):
        self.cmds = parse_all_commands(file_path)
        self.context = dict()
        self.glob = global_context
        for (command, params) in self.cmds:
            if command in init_cmd_dict:
                init_cmd_dict[command](self, params)

    def process(self):
        for (command, params) in self.cmds:
            if command not in cmd_dict:
                print(">> ERR: Command \""+command+"\" is not in cmd_dict.")
            else:
                cmd_dict[command](self, params)

    def get_token(self, token):
        if token in self.context:
            return self.context[token]
        elif token in self.glob:
            return self.glob[token]
        else:
            print(">> ERR: Object does not have token \""+token+"\"")
            return None

    def has_token(self, token):
        if token in self.context:
            return True
        elif token in self.glob:
            return True
        else:
            return False


for root, dirs, files in os.walk(os.getcwd() + "/config"):
    for file in files:
        if(file.endswith(".cfg")):
            print("> Parsing: " + file)
            p = os.path.join(root,file)
            objects.append(object(p))

objects.sort(key=lambda x: x.priority, reverse=True)
for obj in objects:
    print("> Processing: " + obj.id)
    obj.process()

# REMOVE EXIF tags from all images in the project
exif_cleanse(".")
