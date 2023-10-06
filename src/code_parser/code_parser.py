from collections import Counter

FLAG_TO_NEW_SCOPE = 4 * ord(' ')

def parse_py_script(path: str) -> dict:
    if len(path) == 0:
        raise Exception('File path error or file does not exist')
    
    code = {
        "functions" : [],
        "class" : [],
        "comments" : [],
        "multiline_comments" : []
    }
    
    with open(path, "rb") as f:
        while (_bytes := f.readline()):
            decoded = _bytes.decode('utf-8')
            if decoded.startswith('#'):
                code["comments"].append(decoded)
            elif decoded.startswith('"""'):
                code["multiline_comments"].append(decoded)
            elif decoded.startswith('def'):
                code["functions"].append(decoded)
            elif decoded.startswith('class'):
                code["class"].append(decoded)
            
    return code


def parse_cpp_header(path: str) -> dict:
    if len(path) == 0:
        raise Exception('File path error or file does not exist')
    
    code = {
        "functions" : [],
        "class" : [],
        "comments" : [],
        "multiline_comments" : []
    }
    
    with open(path, "rb") as f:
        while (_bytes := f.readline()):
            decoded = _bytes.decode('utf-8')
            if decoded.startswith('//'):
                code["comments"].append(decoded)
            elif decoded.startswith('class'):
                code["class"].append(decoded)
            
    return code


def parse_py_function(path: str) -> str:
    if len(path) == 0:
        raise Exception('File path error or file does not exist')
    
    count_tabs = lambda line: sum([*map(lambda x : ord(x), line[0:4])])
    
    with open(path, "rb") as f:
        while (_bytes := f.readline()):
            decoded = _bytes.decode('utf-8')
            n_tabs = count_tabs(decoded)
            new_scope = n_tabs  == FLAG_TO_NEW_SCOPE
            if new_scope:
                print('Started new scope function or class')
                print(decoded)
                print(n_tabs)