@echo off
setlocal
cd /d "%~dp0"

echo.
echo  ROK META // LOCAL SERVER
echo  ------------------------

if not exist ".venv\Scripts\python.exe" (
    echo [1/3] Creating Python virtual environment...
    where py >nul 2>nul
    if errorlevel 1 (
        python -m venv .venv
    ) else (
        py -3 -m venv .venv
    )
    if errorlevel 1 goto :venv_error
) else (
    echo [1/3] Virtual environment ready.
)

echo [2/3] Installing dependencies...
".venv\Scripts\python.exe" -m pip install --disable-pip-version-check -q -r requirements.txt
if errorlevel 1 goto :install_error

echo [3/3] Starting server...
".venv\Scripts\python.exe" server.py
goto :end

:venv_error
echo.
echo ERROR: Could not create the virtual environment.
echo Install Python 3.10 or newer from https://www.python.org/downloads/
pause
exit /b 1

:install_error
echo.
echo ERROR: Dependency installation failed. Check your internet connection.
pause
exit /b 1

:end
endlocal

