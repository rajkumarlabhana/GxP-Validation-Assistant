@echo off
echo ========================================
echo  GxP Validation Assistant
echo  Database Initialization (OpenAI)
echo ========================================
echo.
echo This will process all PDF documents and create embeddings.
echo This process takes about 10-15 minutes.
echo.
echo Make sure your OPENAI_API_KEY is set in .env file!
echo.
pause
echo.
echo Starting initialization...
echo.
python initialize_db_openai.py
echo.
echo ========================================
echo Database initialization complete!
echo You can now run: run_app.bat
echo ========================================
pause
