@echo off
setlocal enabledelayedexpansion

for %%F in (*) do (
    set "nombre=%%F"
    set "nuevo=!nombre:minecraft_=!"
    
    if not "!nombre!"=="!nuevo!" (
        ren "%%F" "!nuevo!"
    )
)

echo Listo.
pause