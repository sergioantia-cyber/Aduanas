@echo off
echo Limpiando datos del Excel...
python preparar.py
echo.
echo Iniciando servidor del Panel...
start http://localhost:8000/index.html
python -m http.server 8000
pause