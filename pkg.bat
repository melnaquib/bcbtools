echo off
title AlgoMedical Package
echo Create Dir for Packaging Using PyInstaller
set  "APPDIR=C:\work\code\bcbtools"

set "APPNAME=tools-multimodeprocessing"
set "APPDIST=%APPDIR%\dist\%APPNAME%"
set "ANACODA_HOME=C:\work\opt\Anaconda3"
set "QT5DIR=%ANACODA_HOME%\Library"
set "INNOSETUP=C:\Program Files (x86)\Inno Setup 5"
set "WORKING_DIR=C:\work"
rd %APPDIST%
md  %APPDIST%
echo %CD%
echo %APPDIST%


rmdir  /s /q %WORKING_DIR%\build\
echo Finish Removing Working dir


cd %APPDIR%
echo %cwd%
del /F /Q %APPDIR%\dist
del /F /Q %APPDIR%\build

REM %ANACODA_HOME%\Scripts\pyinstaller  --distpath=%WORKING_DIR%\build\ --icon=%APPDIR%\algosend\ui\res\images\logo.ico  %APPDIR%\main.spec
%ANACODA_HOME%\Scripts\pyinstaller  --distpath=%WORKING_DIR%\build\ --icon=%APPDIR%\algosend\ui\res\images\logo.ico  %APPDIR%\main.spec
REM del /F /Q %WORKING_DIR%\build\%APPNAME%\
REM mkdir %WORKING_DIR%\build\%APPNAME%\
REM xcopy %WORKING_DIR%\build\main %WORKING_DIR%\build\%APPNAME%\ /i /h /e /y
copy %WORKING_DIR%\build\%APPNAME%\main.exe %WORKING_DIR%\build\%APPNAME%\%APPNAME%.exe

echo Finishing Pyinstaller

"%INNOSETUP%\Compil32.exe" /cc %APPDIR%\pkg\InnoSetup.iss

%WORKING_DIR%\build\BcbTools_setup.exe

::#pause
