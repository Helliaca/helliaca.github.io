import re
import markdown

# Read file
content = open("input/sample_project/sample_project.txt", "r").read()

# Get all tags
object = dict()

tag_tegex = re.compile('\$tag\s*([^\s]*)\s*([^$]*)\$')
tags = tag_tegex.findall(content)

for (tag, value) in tags:
    object[tag] = value

# Function for reading tags
def get_tag(tag):
    if tag not in object:
        print("Object does not contain tag:" + tag)
        return None
    else:
        return object[tag]

# Get filetype
ft = get_tag("filetype")

if ft=="project" or ft=="proj":
    r = open(get_tag("project_description"), "r").read()
    o = markdown.markdown(r)

    f = open("output/out.html", "a")
    f.write(o)
    f.close()
