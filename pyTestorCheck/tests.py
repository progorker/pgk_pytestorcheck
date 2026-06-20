#
# Copyright (c) 2026 Dinh Thoai Tran <zinospetrel@sdf.org>
# All rights reserved.
#
# + Source URL: https://github.com/progorker/pgk_pytestorcheck/
#
# + License: GPL-2.0
#

import sys
import os

sys.path.append( os.path.abspath( '/bioogr/psk-19/pyTestor' ) )

import pytestor
import tests_config

pytestor.api_testor_startup()

import tests_source

import test_numbers
test_numbers.test_numbers( pytestor.g_token, pytestor.g_suite_id )

import test_strings
test_strings.test_strings( pytestor.g_token, pytestor.g_suite_id )

func_not_declared()

pytestor.api_testor_shutdown()
