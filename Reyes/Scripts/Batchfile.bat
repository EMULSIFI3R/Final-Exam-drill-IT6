@echo off
setlocal enabledelayedexpansion

start "CRUD API" cmd /k "python api.py"

:main

curl http://127.0.0.1:5000/

choice /c 12345E /N

if %ERRORLEVEL% == 1 (
    
    goto add_ven
)

if %ERRORLEVEL% == 2 (
    
    goto venue_ven
)

if %ERRORLEVEL% == 3 (
    
    goto update_ven
)

if %ERRORLEVEL% == 4 (
    
    goto delete_ven
)

if %ERRORLEVEL% == 5 (
    
    goto end
)

goto main

:add_ven

set /p "address=Enter address: "
set /p "comment=Enter comment: "
set /p "rental_fee=Enter rental fee:"

curl -X POST -F "address=!address!" -F "comments=!comment!" -F "rental_fee=!rental_fee!" http://127.0.0.1:5000/add

goto main

:venue_ven

echo [1] venue all venue
echo [2] venue a specific venue

choice /c 12 /N

if %ERRORLEVEL% == 1 (
    
    echo [1] JSON
    echo [2] XML
    choice /c 12 /N

    if %ERRORLEVEL% == 1 (
        
        curl http://127.0.0.1:5000/venue
    )

    if %ERRORLEVEL% == 2 (
        
        curl http://127.0.0.1:5000/venue?format=xml
    )
)

if %ERRORLEVEL% == 2 (
    goto specificID
)

goto main

:specificID

set /p "idvenue=Enter venue ID: "

if "%idvenue%" == "" (
    
    echo Please enter a venue ID
    pause
    goto specificID
)

set /a validID=%idvenue%

if %validID% LSS 1 (
    
    echo Please enter a valid venue ID
    pause
    goto specificID
)

echo Choose format
echo [1] JSON
echo [2] XML

choice /c 12 /N

if %ERRORLEVEL% == 1 (
    
    curl http://127.0.0.1:5000/venue/%idvenue%
    pause
    goto again
)

if %ERRORLEVEL% == 2 (
    
    curl http://127.0.0.1:5000/venue/%idvenue%?format=xml
    pause
    goto again
)

:again

echo [Y\N] Would you like to retrieve another venue?

choice /c YN /N

if %ERRORLEVEL% == 1 (
    
    goto specificID
)

if %ERRORLEVEL% == 2 (
    
    goto main
)

goto main

:update_ven

set /p "idvenue=Enter venue ID: "

if "%idvenue%" == "" (
    
    echo Please enter a venue ID
    pause
    goto update_ven
)

set /a validID=%idvenue%

if %validID% LSS 1 (
    
    echo Please enter a valid venue ID
    pause
    goto update_ven
)

set /p "address=Enter address: "
set /p "comment=Enter comment: "
set /p "rental_fee=Enter rental fee:"

curl -X PUT -F "address=!address!" -F "comments=!comment!" -F "rental_fee=!rental_fee!" http://127.0.0.1:5000/venue/%idvenue%

goto main

:delete_ven

set /p "idvenue=Enter venue ID: "

if "%idvenue%" == "" (
    
    echo Please enter a venue ID
    pause
    goto delete_ven
)

set /a validID=%idvenue%

if %validID% LSS 1 (
    
    echo Please enter a valid venue ID
    pause
    goto delete_ven
)

curl -X DELETE http://127.0.0.1:5000/venue/%idvenue%

goto main

:end

echo Thank you for using the CRUD API
pause
