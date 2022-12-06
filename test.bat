if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin
d:
cd \worker\worker_notifier\worker_notifier
python win_shedule.py
Pause
