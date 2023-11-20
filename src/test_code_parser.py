import code_parser

TEST_FILENAME = 'src\\test_python_script.py'
TEST_FILENAME_CPP = 'src\\test_cpp_c.cpp'

def test_parse_py_script() -> dict:
    return code_parser.parse_py_script(TEST_FILENAME)

def test_parse_cpp_header() -> dict:
    return code_parser.parse_cpp_header(TEST_FILENAME)

def test_parse_py_function() -> list:
    for_pdf = []
    try:
        for_pdf = code_parser.parse_py_file(TEST_FILENAME)
    except Exception as e:
        print(e)
    return for_pdf


def test_parse_cpp_impl() -> list:
    res = []
    try: 
        res = code_parser.find_cpp_scopes(TEST_FILENAME_CPP)
    except Exception as e:
        print(e)
    return res

def print_signature(signature: dict) -> None:
    return_type = signature["return_type"]
    name = signature["name"]
    arguments = signature["arguments"]
    print(f"Return type: {return_type}\nFunction name: {name}\nFunction arguments: {arguments}\n")

def test_parse_cpp_func_intro() -> None:
    print_signature(code_parser.parse_signature_func_cpp("constint main \n( int a )"))
    print_signature(code_parser.parse_signature_func_cpp("double foo \n( const double* a )"))
    print_signature(code_parser.parse_signature_func_cpp("float bar \n( float* a, int b, int c )"))
    print_signature(code_parser.parse_signature_func_cpp("Type* \nmain ( int a, int i, int j, void* void_p )"))
    