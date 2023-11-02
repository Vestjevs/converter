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


def test_parse_cpp_func_intro() -> None:
    code_parser.parse_signature_func_cpp("int main(int a)")
    code_parser.parse_signature_func_cpp("double foo(const double* a)")
    code_parser.parse_signature_func_cpp("float bar(float* a, int b, int c)")
    code_parser.parse_signature_func_cpp("Type* main(int a, int i, int j, void* void_p)")
    pass