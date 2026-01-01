@echo off
echo ========================================
echo  Update GitHub with requirements.txt
echo ========================================
echo.

echo Adding new file...
git add requirements.txt

echo Committing...
git commit -m "Add requirements.txt for Streamlit deployment"

echo Pushing to GitHub...
git push

echo.
echo ========================================
echo  Done! Streamlit will auto-redeploy
echo ========================================
echo.
echo Wait 1-2 minutes for Streamlit to rebuild your app.
echo.
pause
