@echo off
echo User ....
net localgroup /add "Users"
echo Authenticated Users ....
net localgroup /add "Authenticated Users"

echo Agregar Admin a los grupos ....
set /p name=Escribe nombre del admin. 
net localgroup "Users" /add %name%
net localgroup "Authenticated Users" /add %name%
pause