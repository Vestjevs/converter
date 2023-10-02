def parse_python_script(path: str) -> list:
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