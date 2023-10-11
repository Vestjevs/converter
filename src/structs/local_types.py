import collections

N_TABS = 4
FILE_NAME = "test_file"
DIR_OUTPUT = "test_output_pdf"

FLAG_TO_NEW_SCOPE = 4 * ord(' ')
END_SCOPE_TEXTM1 = "\n"
END_SCOPE_TEXTM2 = "    \n"
SCOPE_END_BYTEM1 = "\r\n"
SCOPE_END_BYTEM2 = "    \r\n"

author = collections.namedtuple('Author', ['name',  'create_date', 'change_date'])
