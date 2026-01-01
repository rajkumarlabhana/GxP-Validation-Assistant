@echo off
echo ========================================
echo  GxP Validation Assistant - Setup
echo ========================================
echo.
echo Step 1: Installing dependencies...
echo.
pip install -r requirements_openai.txt
echo.
echo ========================================
echo Setup complete!
echo.
echo Next steps:
echo 1. Make sure your OPENAI_API_KEY is set in .env file
echo 2. Run: initialize_db.bat (if not done already)
echo 3. Run: run_app.bat to start the application
echo ========================================
pause
