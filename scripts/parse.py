import os
import re
import shlex

# parses all commands in a file and returns a list
def parse_all_commands(file_path):
    ret = []
    c = open(file_path, "r").read()

    cmd_regex = re.compile('\$([\w]+)\s*([^$]*)\$')
    commands = cmd_regex.findall(c)

    for (command, params) in commands:
        params = shlex.split(params)
        ret.append((command, params))

    return ret

# Takes a string and returns the first $if condition$ (...) $endif$
def condition_parser(s):
    found = False
    before = ""
    condition = ""
    embed = []
    after = ""

    i = 0
    ic = 0
    while i<len(s):

        # $if at current position
        if s[i:i+3] == "$if":

            # if we havent found a previous one
            if not found:
                before = s[0:i] # Set before and found
                found = True

                # parse condition
                j = i+1
                while s[j] != "$": j += 1
                condition = s[i+3:j].strip()
                i = j

            # if we already found one, add this to the embed
            else:
                embed.append(s[i])

            ic += 1 # increase if-counter
            i+=1

        # $endif$ at current position
        elif s[i:i+7] == "$endif$":

            ic -= 1 # lower counter

            # if we have 0 ifs on the stack -> end
            if ic==0:
                after = s[i+7:]
                break
            # otherwise add it to the embed
            else:
                embed.append(s[i:i+7])

            i += 7

        # Nothing special at this position
        else:
            if found:
                embed.append(s[i])
            i+=1

    embed = ''.join(embed)

    return found, before, condition, embed, after


def loop_parser(s):
    found = False
    before = ""
    embed = []
    after = ""

    i = 0
    ic = 0
    while i<len(s):

        if s[i:i+8] == "$forall$":

            # if we havent found a previous one
            if not found:
                before = s[0:i] # Set before and found
                found = True

            # if we already found one, add this to the embed
            else:
                embed.append(s[i])

            ic += 1 # increase if-counter
            i+=8

        elif s[i:i+8] == "$endfor$":

            ic -= 1 # lower counter

            # if we have 0 on the stack -> end
            if ic==0:
                after = s[i+8:]
                break
            # otherwise add it to the embed
            else:
                embed.append(s[i:i+8])

            i += 8

        # Nothing special at this position
        else:
            if found:
                embed.append(s[i])
            i+=1

    embed = ''.join(embed)

    return found, before, embed, after


def insert_parser(s):
    found = False
    before = ""
    token = ""
    after = ""

    i = 0
    while i<len(s):
        if s[i:i+7] == "$insert":
            before = s[0:i] # Set before and found
            found = True

            # parse condition
            j = i+8
            while s[j] != "$": j += 1
            token = s[i+8:j].strip()
            after = s[j+1:]
            break
        i += 1

    return found, before, token, after
