def is_balanced(str):
    brackets = ['()', '{}', '[]']
    while any(x in str for x in brackets):
        for br in brackets:
            str = str.replace(br, '')
    return not str
