@echo off
echo Waking up the Viral Brainrot Factory...

:: 1. Navigate to the project directory
cd /d "C:\Users\ranab\OneDrive\Desktop\AutoContent"

:: 2. Run the Main Pipeline (Phase 1, 2, 3)
"C:\Users\ranab\AppData\Local\Programs\Python\Python313\python.exe" main_pipeline.py

echo Pipeline execution complete. 
echo Running inventory check and alert system...

:: 3. Run your custom Reminder Script
"C:\Users\ranab\AppData\Local\Programs\Python\Python313\python.exe" reminder.py

echo Factory shutdown sequence complete.
pause