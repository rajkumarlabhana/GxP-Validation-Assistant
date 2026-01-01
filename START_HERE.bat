@echo off
color 0A
echo.
echo  ========================================================
echo   GxP Validation Assistant - IIT Guwahati Capstone
echo  ========================================================
echo.
echo   Welcome! Choose an option:
echo.
echo   1. Run Application (OpenAI RAG - Recommended)
echo   2. Setup / Install Dependencies
echo   3. Initialize Database
echo   4. Exit
echo.
echo  ========================================================
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto run_app
if "%choice%"=="2" goto setup
if "%choice%"=="3" goto init_db
if "%choice%"=="4" goto end

echo Invalid choice! Please try again.
pause
goto start

:run_app
echo.
echo Starting GxP Validation Assistant (OpenAI RAG)...
call run_app.bat
goto end

:setup
echo.
echo Running setup...
call setup.bat
goto end

:init_db
echo.
echo Initializing database...
call initialize_db.bat
goto end

:end
echo.
echo Thank you for using GxP Validation Assistant!
pause
