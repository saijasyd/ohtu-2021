*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
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

Login After Successful Registration
    Set Username  tiina
    Set Password  tiina123
    Set Password Confirmation  tiina123
    Submit Register
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  tiina
    Set Password  tiina123
    Submit Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  tuija
    Set Password  tii4
    Set Password Confirmation  tii4
    Submit Register
    Register Should Fail With Message  Password is invalid
    Go To Login Page
    Login Page Should Be Open
    Set Username  tuija
    Set Password  tii4
    Submit Credentials
    Login Should Fail With Message  Invalid username or password



    

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

# Set Username
#     [Arguments]  ${username}
#     Input Text  username  ${username}

# Set Password
#     [Arguments]  ${password}
#     Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Create User And Go To Register Page
    #Create User  matti  matti123
    Go To Register Page
    Register Page Should Be Open

