# AutoCleanTempFiles.py

## Description

AutoCleanTempFiles.py is a Python script that helps you automatically clean temporary files from your Windows PC, freeing up disk space and improving system performance.

## Usage

1. Download the AutoCleanTempFiles.py script to your computer.

2. Open a command prompt or terminal.

3. Navigate to the directory where the script is located:
   cd path\to\script\directory

4. Run the script by executing the following command:
   python AutoCleanTempFiles.py
   The script will clean the temporary files in your local temp folder.

5. The script can be scheduled to run at specific intervals to keep your system clean.

## Author

Margitoh

## Creating an Executable

To create an executable (.exe), use PyInstaller:

In a Visual Studio Code terminal or PowerShell, use the following command:
python -m PyInstaller --onefile AutoCleanTempFiles.py

Make sure you're in the same directory where the script (AutoCleanTempFiles.py) is, e.g., user\Desktop\file_name.

## Scheduling Automated Cleaning

To schedule the script to run at specific intervals and keep your system clean, follow these steps:

1. Open Task Scheduler:
   -Press Windows + S, type "Task Scheduler," and press Enter.
2. Create a Basic Task:
   -In the Task Scheduler, click on "Create Basic Task..." on the right-hand side.
3. Give the Task a Name and Description:
   -Provide a name and an optional description for your task, then click "Next."
4. Choose the Trigger:
   -Select how often you want your script to run. Choose "Daily," "Weekly," or "Monthly," depending on your preference. Click "Next."
   -Follow the prompts to set up the trigger details, like the start date and time, and how often you want the task to repeat.
5. Select the Action:
   -Choose "Start a Program" as the action type and click "Next."
6. Browse for Your Python Script:
   -Click "Browse..." and navigate to your AutoCleanTempFiles.py script, and then click "Next."
7. Review and Finish:
   Review the task settings, and if everything looks correct, click "Finish."
8. Enter Your Windows Password:
   -If you're prompted for your Windows password, enter it. This is necessary because the task scheduler may run the task even if you're not logged in.
9. Task Created:
   -Once you complete the wizard, your task will be created, and it will run at the specified intervals to clean temporary files.
