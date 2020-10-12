import re

def rearrange_name(name):
    if type(name) != str:
        raise TypeError("Name must be string") 
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
