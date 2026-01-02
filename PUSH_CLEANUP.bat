@echo off
echo ========================================
echo  Push Cleaned Files to GitHub
echo ========================================
echo.

cd /d "%~dp0"

echo Checking status...
git status
echo.

echo Adding all changes...
git add .
echo.

echo Committing changes...
git commit -m "Remove unwanted files and clean up project"
echo.

echo Pushing to GitHub...
git push origin main

echo.
echo ========================================
echo  Done! Files pushed to GitHub
echo ========================================
echo.
echo Check your repository:
echo https://github.com/rajkumarlabhana/GxP-Validation-Assistant
echo.
pause
