@echo off
echo ========================================
echo  Quick Push to GitHub
echo ========================================
echo.

cd /d "%~dp0"

echo Adding app_openai.py...
git add app_openai.py

echo Committing changes...
git commit -m "Update chatbot icon with styled gradient design"

echo Pushing to GitHub...
git push origin main

echo.
echo ========================================
echo  Done! Check Streamlit in 1-2 minutes
echo ========================================
echo.
pause
