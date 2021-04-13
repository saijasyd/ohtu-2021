*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User




*** Test Cases ***
Register With Valid Username And Password

    Input Credentials  errki  kalle123
    Output Should Contain  New user registered
# ...

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials   ka  kalle123
    Output Should Contain  Username is invalid
# ...

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle
    Output Should Contain   Password is invalid
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallepassword
    Output Should Contain   Password is invalid
# ...


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123