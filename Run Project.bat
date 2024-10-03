@echo off
start powershell -NoExit -Command "$Host.UI.RawUI.WindowTitle = 'Islamic App1'; & code .; cd Docker; docker-compose up"
