import re
import markdown
import os
import shlex
from scripts.parse import parse_all_commands
from scripts.commands import set_context, fill_template, set_context_from_file, set_context_from_md_file

cmd_dict = {
    "set": set_context,
    "fill_template": fill_template,
    "set_from_md_file": set_context_from_md_file,
    "set_from_file": set_context_from_file,
}

class object:
    context = dict()
    cmds = []

    def __init__(self, file_path):
        self.cmds = parse_all_commands(file_path)
        for (command, params) in self.cmds:
            if command not in cmd_dict:
                print("ERR: Command \""+command+"\" is not in cmd_dict.")
            else:
                cmd_dict[command](self, params)


for root, dirs, files in os.walk(os.getcwd() + "/input"):
    for file in files:
        if(file.endswith(".cfg")):
            p = os.path.join(root,file)
            object(p)
