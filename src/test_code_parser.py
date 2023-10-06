import code_parser

TEST_FILENAME = 'src\\test_python_script.py'

def test_parse_py_script() -> dict:
    return code_parser.parse_py_script(TEST_FILENAME)

def test_parse_cpp_header() -> dict:
    return code_parser.parse_cpp_header(TEST_FILENAME)

def test_parse_py_function() -> list:
    return code_parser.parse_py_function(TEST_FILENAME)

def test_parse_cpp_impl() -> list:
    pass
