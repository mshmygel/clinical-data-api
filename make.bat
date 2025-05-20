@echo off
IF "%1"=="build" (
    docker-compose build
) ELSE IF "%1"=="start" (
    docker-compose up
) ELSE IF "%1"=="stop" (
    docker-compose down
) ELSE IF "%1"=="restart" (
    docker-compose down
    docker-compose up --build
) ELSE (
    echo.
    echo Usage:
    echo    make.bat build
    echo    make.bat start
    echo    make.bat stop
    echo    make.bat restart
)
