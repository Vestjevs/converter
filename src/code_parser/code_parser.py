import collections

from structs import *

import sys


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


def parse_py_file(path: str) -> str:
    if len(path) == 0:
        raise Exception("File path error or file does not exist")
    
    count_tabs = lambda line: sum([*map(lambda x : ord(x), line[0:4])])
    
    scopes = []
    scope = []
    with open(path, mode="r") as f:
        while (line := f.readline()):
            scope.append(line)
            if line == END_SCOPE_TEXTM1 or line == END_SCOPE_TEXTM2: # "    \n", "\n" - end of scope/ or in byte mode "    \r\n", "\r\n" 
                scope.append("\n")
                scopes.append(scope.copy())
                scope.clear()
        
        scope.append("\n")
        scopes.append(scope.copy())
        scope.clear()        
    
    for scope in scopes:
        print("Started scope: \n")
        for line in scope:
            print(line)
        print("Ended scope. \n")
                
    with open(path, mode="w") as f:
        if len(scopes) == 0:
            raise Exception("Nothing to write to file")
        for scope in scopes:
            f.writelines(scope)
            
    return "File parsed and formatted"
    

def find_cpp_scopes(path: str) -> list():
    if len(path) == 0:
        raise Exception("File path error or file does not exist")
    
    scopes = []
    with open(path, mode="r") as f:
        scope_start = 0
        scope_end = 0
        
        while (line := f.readline()):
            for i in range(len(line)):
                if line[i] == '{':
                    scope_start += 1
                
                if line[i] == '}':
                    scope_end += 1
            
            if scope_start != scope_end:
                print(line)
            
    return scopes
    
def parse_signature_func_cpp(intro: str) -> None:
    if len(intro) == 0:
        raise Exception("Invalid string for parse.")
    specifiers = ""
    return_type = ""
    name = ""
    arguments = ""
    start = 0
    end = 0
    
    intro = intro.replace('\n', '')
    
    while intro[end] != ' ' and end < len(intro): end += 1
    if start != end:
        return_type += intro[start:end]
    else:
        raise Exception("Invalid type")
    
    end += 1
    start = end
    while intro[end] != '(' and end < len(intro): end += 1
    
    if start < end:
        name += intro[start:end]
    else:
        raise Exception("Invalid name") # !tbd: rewrite checks
    
    end += 1
    start = end
    while intro[end] != ')' and end < len(intro): end += 1
    
    args = intro[start:end]
    
    if start < end:
        arguments += args
    else:
        raise Exception("Invalid name") # !tbd: rewrite checks
    
    return {
        "return_type" : return_type,
        "name": name,
        "arguments": arguments
    }
    
    