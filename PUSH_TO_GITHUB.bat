@echo off
echo ========================================
echo  Push to GitHub - Setup Helper
echo ========================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed!
    echo.
    echo Please install Git first:
    echo 1. Go to: https://git-scm.com
    echo 2. Download Git for Windows
    echo 3. Install with default settings
    echo 4. Restart this script
    echo.
    pause
    exit /b
)

echo Git is installed! ✓
echo.

REM Initialize repository if not already done
if not exist ".git" (
    echo Initializing Git repository...
    git init
    echo.
)

echo Adding files to Git...
git add .
echo.

echo Committing changes...
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Initial commit - GxP Validation Assistant
git commit -m "%commit_msg%"
echo.

echo ========================================
echo  Next Steps:
echo ========================================
echo.
echo 1. Create repository on GitHub:
echo    - Go to: https://github.com/new
echo    - Name: GxP-Validation-Assistant
echo    - Click "Create repository"
echo.
echo 2. Copy your GitHub username and run:
echo.
set /p github_user="Enter your GitHub username: "
echo.

if "%github_user%"=="" (
    echo No username entered. Please run this script again.
    pause
    exit /b
)

echo Adding remote repository...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/%github_user%/GxP-Validation-Assistant.git
echo.

echo Pushing to GitHub...
echo.
echo IMPORTANT: When prompted for password, use your Personal Access Token!
echo (Not your GitHub password)
echo.
echo To create token:
echo 1. Go to: https://github.com/settings/tokens
echo 2. Generate new token (classic)
echo 3. Select 'repo' scope
echo 4. Copy and use as password
echo.
pause

git branch -M main
git push -u origin main

echo.
echo ========================================
echo  Done! Your code is now on GitHub!
echo ========================================
echo.
echo View at: https://github.com/%github_user%/GxP-Validation-Assistant
echo.
pause
