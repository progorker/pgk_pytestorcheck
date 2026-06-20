#
# Copyright (c) 2026 Dinh Thoai Tran <zinospetrel@sdf.org>
# All rights reserved.
#
# + Source URL: https://github.com/progorker/pgk_pytestorcheck/
#
# + License: GPL-2.0
#

import pytestor

def test_numbers( p_token, p_suite_id ):
  v_case_code = 'test_numbers'
  v_case_id = pytestor.api_testor_case( p_token, p_suite_id, v_case_code )
  print( "Case ID: " + str(v_case_id) + "\n" )

  # -------------------------------------------- #

  v_test_code = 'equals.1'
  v_num_a = 30.3
  v_num_b = 30.3
  v_test_id = pytestor.api_testor_equals( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  v_test_code = 'equals.2'
  v_num_a = 30.3
  v_num_b = 45.8
  v_test_id = pytestor.api_testor_equals( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  v_test_code = 'not_equals.1'
  v_num_a = 30.3
  v_num_b = 30.3
  v_test_id = pytestor.api_testor_not_equals( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  v_test_code = 'not_equals.2'
  v_num_a = 30.3
  v_num_b = 45.8
  v_test_id = pytestor.api_testor_not_equals( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  # -------------------------------------------- #

  v_test_code = 'greater_than.1'
  v_num_a = 43.6
  v_num_b = 30.3
  v_test_id = pytestor.api_testor_greater_than( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  v_test_code = 'greater_than.2'
  v_num_a = 43.6
  v_num_b = 60.7
  v_test_id = pytestor.api_testor_greater_than( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  v_test_code = 'not_greater_than.1'
  v_num_a = 43.6
  v_num_b = 30.3
  v_test_id = pytestor.api_testor_not_greater_than( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  v_test_code = 'not_greater_than.2'
  v_num_a = 43.6
  v_num_b = 60.7
  v_test_id = pytestor.api_testor_not_greater_than( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  # -------------------------------------------- #

  v_test_code = 'less_than.1'
  v_num_a = 30.5
  v_num_b = 40.8
  v_test_id = pytestor.api_testor_less_than( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  v_test_code = 'less_than.2'
  v_num_a = 50.5
  v_num_b = 40.8
  v_test_id = pytestor.api_testor_less_than( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  v_test_code = 'not_less_than.1'
  v_num_a = 30.5
  v_num_b = 40.8
  v_test_id = pytestor.api_testor_not_less_than( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

  v_test_code = 'not_less_than.2'
  v_num_a = 50.5
  v_num_b = 40.8
  v_test_id = pytestor.api_testor_not_less_than( p_token, p_suite_id, v_case_id, v_test_code, v_num_a, v_num_b )
  print( "Test ID: " + str(v_test_id) + "\n" )

