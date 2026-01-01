@echo off
echo ========================================
echo  Push Updates to GitHub
echo ========================================
echo.

echo Adding fixed files...
git add app_openai.py vector_store_openai.py rag_engine_openai.py chatbot.png

echo Committing...
git commit -m "Fix logging and add custom chatbot image"

echo Pushing to GitHub...
git push

echo.
echo ========================================
echo  Done! Streamlit will auto-redeploy
echo ========================================
echo.
echo Wait 1-2 minutes for your app to rebuild.
echo.
pause
