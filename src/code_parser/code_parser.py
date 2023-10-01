def parse_python_script(path: str) -> list:
    if len(path) == 0:
        raise Exception('File path error or file does not exist')
    
    lines = []
    with open(path, "rb") as f:
        while (bytes := f.readline()):
            print(bytes)
            lines.append(str(bytes))
    
    return lines