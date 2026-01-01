@echo off
echo ========================================
echo  Fix GitHub Push
echo ========================================
echo.

echo This will force push your code to GitHub.
echo.
set /p confirm="Continue? (yes/no): "

if /i not "%confirm%"=="yes" (
    echo Cancelled.
    pause
    exit /b
)

echo.
echo Force pushing to GitHub...
echo.

git push -f origin main

echo.
echo ========================================
echo  Done! Check your repository:
echo  https://github.com/rajkumarlabhana/GxP-Validation-Assistant
echo ========================================
echo.
pause
