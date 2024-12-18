import re


def get_match(pattern, string):
    match = re.search(pattern, string)
    if match:
        return match.group(0)
    return None
