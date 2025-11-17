*** Settings ***
Resource          resource.robot
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser

*** Test Cases ***
When counter has a nonzero value and it is reset the value becomes zero
    Go To    http://127.0.0.1:5001
    Click Button    Paina
    Click Button    Paina
    Element Text Should Be    id=counter    2
    Click Button    Nollaa
    Element Text Should Be    id=counter    0
