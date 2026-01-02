@echo off
echo ========================================
echo  Fix Git and Push Changes
echo ========================================
echo.

cd /d "%~dp0"

echo Aborting any pending merges...
"C:\Program Files\Git\bin\git.exe" merge --abort 2>nul

echo.
echo Pulling latest from GitHub...
"C:\Program Files\Git\bin\git.exe" pull origin main --no-edit

echo.
echo Adding app_openai.py...
"C:\Program Files\Git\bin\git.exe" add app_openai.py

echo.
echo Committing changes...
"C:\Program Files\Git\bin\git.exe" commit -m "Update to robot icons" 2>nul

echo.
echo Pushing to GitHub...
"C:\Program Files\Git\bin\git.exe" push origin main

echo.
echo ========================================
echo  Done! Wait 2 minutes then refresh
echo  your Streamlit app
echo ========================================
echo.
pause
