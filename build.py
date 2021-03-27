import re
import markdown
import os


def parse_tags(file_path):
    ret = dict()

    # open file
    c = open(file_path, "r").read()

    # find all tags
    tag_tegex = re.compile('\$tag\s*([^\s]*)\s*([^$]*)\$')
    tags = tag_tegex.findall(c)

    # insert tags into ret
    for (tag, value) in tags:
        ret[tag] = value

    return ret


def get_tag(object, tag):
    if tag not in object:
        print("Object does not contain tag:" + tag)
        return None
    else:
        return object[tag]


def process(file_path):
    tags = parse_tags(file_path)

    ft = get_tag(tags, "filetype")

    if ft=="project" or ft=="proj":
        r = open(get_tag(tags, "project_description"), "r").read()
        o = markdown.markdown(r, extensions=['extra'])

        # Get file
        f = open("output/"+get_tag(tags, "project_id")+".html", "a")
        # Delete previous contents
        f.seek(0)
        f.truncate()
        # write output
        f.write(o)
        f.close()


for root, dirs, files in os.walk(os.getcwd() + "/input"):
    for file in files:
        if(file.endswith(".cfg")):
            p = os.path.join(root,file)
            process(p)
