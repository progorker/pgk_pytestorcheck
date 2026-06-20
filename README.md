```
===========_____=======_============
  _ __ _  |_   _|__ __| |_ ___ _ _ 
 | '_ \ || || |/ -_|_-<  _/ _ \ '_|
 | .__/\_, ||_|\___/__/\__\___/_|  
=|_|===|__/=========================
Check Testor's features using Python
====================================


-|_|-----------|___/----------------------
             Alpha Testing
------------------------------------------


-|_|-------|_|---------------------------
       Controlling source versions
-----------------------------------------

$) export PY_TESTOR_CHECK_DIR=""
$) nano $PY_TESTOR_CHECK_DIR/csvc-cfg.php
---> Modify myTestor account and other settings
$) cd $PY_TESTOR_CHECK_DIR && php ./csvc.php


-|_|-------|_|---------------------------
            Running tests
-----------------------------------------

$) export PY_TESTOR_CHECK_DIR=""
$) cd $PY_TESTOR_CHECK_DIR && python3 ./tests.py

```
