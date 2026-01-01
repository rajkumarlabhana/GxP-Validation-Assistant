@echo off
echo ========================================
echo  Final Push - Robot Icon Update
echo ========================================
echo.
echo This will push the robot icon changes to GitHub.
echo.
pause

cd /d "%~dp0"

"C:\Program Files\Git\bin\git.exe" add app_openai.py
"C:\Program Files\Git\bin\git.exe" commit -m "Change to robot icon in chat"
"C:\Program Files\Git\bin\git.exe" push origin main

echo.
echo ========================================
echo  Done! Wait 2 minutes for Streamlit
echo ========================================
echo.
echo Then refresh your Streamlit app with Ctrl+Shift+R
echo.
pause
