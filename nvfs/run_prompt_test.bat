echo off
echo ## Available test ##
echo Get_data.py          
echo:
echo: 
set /p Input=Test to run:
echo on 
call ipy -m unittest %Input%
pause