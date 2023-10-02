import code_parser

TEST_FILENAME = 'src\check_copies.py'

def test_parse_python_script() -> list:
    return code_parser.parse_python_script(TEST_FILENAME)
