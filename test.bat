@REM ---用于隐藏cmd黑框---
if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin
@REM ---用于隐藏cmd黑框---
D:
cd \worker\help_worker
python help_worker.py
@REM ---用于调试闪退的情况---
@REM Pause
@REM ---用于调试闪退的情况---