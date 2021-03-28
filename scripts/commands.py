import re
import markdown
from .parse import condition_parser, insert_parser

def set_context(obj, params):
    obj.context[params[0]] = " ".join(params[1:])


def set_context_from_file(obj, params):
    content = open(params[1], "r").read()
    obj.context[params[0]] = content


def set_context_from_md_file(obj, params):
    content = open(params[1], "r").read()
    content = markdown.markdown(content, extensions=['extra'])
    obj.context[params[0]] = content



def fill_template(obj, params):
    template_path = params[0]
    write_path = params[1]

    content = open(template_path, "r").read()

    # Do conditions
    found, before, condition, embed, after = condition_parser(content)
    while(found):
        if condition in obj.context:
            content = before + embed + after
        else:
            content = before + after
        found, before, condition, embed, after = condition_parser(content)

    # Do replacements
    found, before, token, after = insert_parser(content)
    while(found):
        content = before + obj.context[token] + after
        found, before, token, after = insert_parser(content)

    # Get file
    f = open(params[1], "a")
    # Delete previous contents
    f.seek(0)
    f.truncate()
    # write output
    f.write(content)
    f.close()
