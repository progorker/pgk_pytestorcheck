#
# Copyright (c) 2026 Dinh Thoai Tran <zinospetrel@sdf.org>
# All rights reserved.
#
# + Source URL: https://github.com/progorker/pgk_pytestorcheck/
#
# + License: GPL-2.0
#

import pytestor

g_token = pytestor.g_token
g_suite_id = pytestor.g_suite_id

name = 'pkg_tests'
data = '/tests.py'
pytestor.api_testor_option( g_token, g_suite_id, data, 'src:' + name, False )

name = 'pkg_tests_config'
data = '/tests_config.py'
pytestor.api_testor_option( g_token, g_suite_id, data, 'src:' + name, False )

name = 'pkg_tests_source'
data = '/tests_source.py'
pytestor.api_testor_option( g_token, g_suite_id, data, 'src:' + name, False )

name = 'test_numbers'
data = '/test_numbers.py'
pytestor.api_testor_option( g_token, g_suite_id, data, 'src:' + name, False )

name = 'test_strings'
data = '/test_strings.py'
pytestor.api_testor_option( g_token, g_suite_id, data, 'src:' + name, False )

