import re
import markdown
import os
import shlex
from scripts.parse import parse_all_commands
from scripts.commands import *

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
    "priority": set_priority,
    "id": set_id,
}

global_context = dict()

class object:
    priority = 0
    context = dict()
    cmds = []
    glob = global_context
    id = "Unnamed"

    def __init__(self, file_path):
        self.cmds = parse_all_commands(file_path)
        for (command, params) in self.cmds:
            if command=="priority" or command=="id":
                cmd_dict[command](self, params)

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


objects = []
for root, dirs, files in os.walk(os.getcwd() + "/input"):
    for file in files:
        if(file.endswith(".cfg")):
            print("> Parsing: " + file)
            p = os.path.join(root,file)
            objects.append(object(p))

objects.sort(key=lambda x: x.priority, reverse=True)
for obj in objects:
    print("> Processing: " + obj.id)
    obj.process()
