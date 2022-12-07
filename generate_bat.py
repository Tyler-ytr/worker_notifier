import os

root=os.path.abspath('.')[:2]+"\n"
place="cd "+os.path.abspath('.')[2:]+"\n"
header="if \"%1\"==\"hide\" goto CmdBegin\n"
header+="start mshta vbscript:createobject(\"wscript.shell\").run(\"\"\"%~0\"\" hide\",0)(window.close)&&exit\n"
header+=":CmdBegin\n"
result=header+root+place+"python win_shedule.py"

with open("test.bat","w") as f:
    f.write(result)
# print(result)