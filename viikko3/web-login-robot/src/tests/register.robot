*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalevi
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register
    Register Should Succeed
    
Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register
    Register Should Fail With Message  Username is invalid


Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  kal1
    Set Password Confirmation  kal1
    Submit Register
    Register Should Fail With Message  Password is invalid


Register With Nonmatching Password And Password Confirmation
    Set Username  uolevi
    Set Password  kal1
    Set Password Confirmation  password
    Submit Register
    Register Should Fail With Message  Password is invalid

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Create User And Go To Register Page
    #Create User  matti  matti123
    Go To Register Page
    Register Page Should Be Open

