rem @echo off
chcp 65001

rem Sドライブで作業すると仮定
s:

rem Sドライブ配下の録音フォルダに全てのインタビューデータがあると仮定
cd s:\rec\録音

rem そこにあるフォルダ名を記録しておく
dir /AD /B > foloderlist.txt

rem Sドライブ配下のrecフォルダにプログラムがあると仮定
cd s:\rec

set BASE_REC_DIR=s:\rec\録音

set REC_DIRS=afolder
rem anotherfolder anotherfolder anotherfolder ...

setlocal enabledelayedexpansion

for %%i in (%REC_DIRS%) do (
    set C_DIR=%BASE_REC_DIR%\%%i
    
    python printlinevtt.py !C_DIR! > !C_DIR!\103.txt
    python printline3.py !C_DIR! > !C_DIR!\002.txt
    python removeCRLF.py !C_DIR! > !C_DIR!\003.txt
    python conv.py !C_DIR!
)