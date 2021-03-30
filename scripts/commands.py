import re
import markdown
import os
from .parse import *

def do_nothing(obj, params):
    return


def set_priority(obj, params):
    obj.priority = int(params[0])


def set_id(obj, params):
    obj.id = params[0]


def globalappend_context(obj, params):
    if params[0] not in obj.glob: obj.glob[params[0]] = ""
    obj.glob[params[0]] += " ".join(params[1:])


def globalappend_context_from_file(obj, params):
    if params[0] not in obj.glob: obj.glob[params[0]] = ""
    content = open(params[1], "r").read()
    obj.glob[params[0]] += content


def globalappend_context_from_md_file(obj, params):
    if params[0] not in obj.glob: obj.glob[params[0]] = ""
    content = open(params[1], "r").read()
    content = markdown.markdown(content, extensions=['extra'])
    obj.glob[params[0]] += content


def globalset_context(obj, params):
    obj.glob[params[0]] = " ".join(params[1:])


def globalset_context_from_file(obj, params):
    content = open(params[1], "r").read()
    obj.glob[params[0]] = content


def globalset_context_from_md_file(obj, params):
    content = open(params[1], "r").read()
    content = markdown.markdown(content, extensions=['extra'])
    obj.glob[params[0]] = content


def set_context(obj, params):
    obj.context[params[0]] = " ".join(params[1:])


def set_context_from_file(obj, params):
    content = open(params[1], "r").read()
    obj.context[params[0]] = content


def set_context_from_md_file(obj, params):
    content = open(params[1], "r").read()
    content = markdown.markdown(content, extensions=['extra'])
    obj.context[params[0]] = content


def fill_section(obj, content):
    # Do loops
    found, before, embed, after = loop_parser(content)
    while found:
        app = ""
        for o in obj.all_objects:
            app  += fill_section(o, embed)
        content = before + app + after
        found, before, embed, after = loop_parser(content)

    # Do conditions
    found, before, condition, embed, after = condition_parser(content)
    while(found):
        if obj.has_token(condition):
            content = before + embed + after
        else:
            content = before + after
        found, before, condition, embed, after = condition_parser(content)

    # Do replacements
    found, before, token, after = insert_parser(content)
    while(found):
        content = before + obj.get_token(token) + after
        found, before, token, after = insert_parser(content)

    return content


def fill_template(obj, params):
    template_path = params[0]
    write_path = params[1]

    content = open(template_path, "r").read()

    content = fill_section(obj, content)

    # Create directories if necessary
    try:
        os.makedirs(os.path.dirname(os.path.abspath(params[1])))
        print(">> Creating new directories for path: " + os.path.dirname(os.path.abspath(params[1])))
    except FileExistsError:
        pass # directory already exists
    # Get file
    print(">> Writing template to file: " + params[1])
    f = open(params[1], "a")
    # Delete previous contents
    f.seek(0)
    f.truncate()
    # write output
    f.write(content)
    f.close()
