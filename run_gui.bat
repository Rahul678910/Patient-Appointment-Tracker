@echo off
setlocal
title Patient Appointment Tracker - GUI

:: Detect python executable
where python3.11 >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=python3.11
    goto run
)

where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=python
    goto run
)

where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=py -3
    goto run
)

if exist "%USERPROFILE%\.local\bin\python3.11.exe" (
    set PYTHON_CMD="%USERPROFILE%\.local\bin\python3.11.exe"
    goto run
)

if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    set PYTHON_CMD="%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
    goto run
)

echo [ERROR] Python 3 was not found in your PATH.
echo Please ensure Python 3 is installed.
pause
exit /b 1

:run
echo Starting Patient Appointment Tracker GUI...
%PYTHON_CMD% main.py --gui %*
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Application exited with error code %ERRORLEVEL%.
    pause
)
