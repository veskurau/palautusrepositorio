*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Create User  kalle2  kalle1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Create User  kalle  kalle123
    Output Should Contain  User with username kalle already exists

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123