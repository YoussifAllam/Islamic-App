@echo off

start powershell -NoExit -Command "$Host.UI.RawUI.WindowTitle = 'Islamc App'; & '.\venv\Scripts\activate'; code .;  python manage.py runserver"

