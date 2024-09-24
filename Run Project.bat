@echo off

start powershell -NoExit -Command "$Host.UI.RawUI.WindowTitle = 'Home and Search Service 9000'; & '.\venv\Scripts\activate'; code .; cd '.\HomeAndSearch_repo\HomeAndSearch'; python manage.py runserver 9000"

cd "E:\Programing\django_projects\Board pins"
start powershell -NoExit -Command "$Host.UI.RawUI.WindowTitle = 'Authentication Service 8080'; & '.\venv\Scripts\activate'; cd '.\authentication_repo\authentication_service'; python manage.py runserver 8080"

cd "E:\Programing\django_projects\Board pins"
start powershell -NoExit -Command "$Host.UI.RawUI.WindowTitle = 'Single Service Provider 9001'; & '.\venv\Scripts\activate'; cd '.\SingleServiceProvider_repo\SingleServiceProvider'; python manage.py runserver 9001"

cd "E:\Programing\django_projects\Board pins"
start powershell -NoExit -Command "$Host.UI.RawUI.WindowTitle = 'Tasks Management Service 9002'; & '.\venv\Scripts\activate'; cd '.\TasksManagement_repo\TasksManagement'; python manage.py runserver 9002"

cd "E:\Programing\django_projects\Board pins"
start powershell -NoExit -Command "$Host.UI.RawUI.WindowTitle = 'Bidding_and_Compare 9003'; & '.\venv\Scripts\activate'; cd '.\Bidding_and_Compare'; python manage.py runserver 9003"