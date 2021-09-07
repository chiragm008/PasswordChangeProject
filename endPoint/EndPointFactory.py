
class EndPoint:
    BASE_URI_API = "http://127.0.0.1:5000/password"
    systemPassword = "Password@1textqu#*"

# Unit Test Cases--------------------------------------------------------------------------------
class TestData:
    UnitTestSuccess = [('Password@1textqu#*', 'Change!200Password@#'),  # Success: correct password (All condition satisfy)
                       ('Password@1textqu#*', 'change!20Passwhan@#'),   # Success: Repeat chars =4 (with all other satisfy)
                       ('Password@1textqu#*', 'change!#200Password@#')] # Success: Special chars =4 (with all other satisfy)


    UnitTestFail = [('', ''),                                       # Fail: Old=New=NULL
                ('Password@1textqu','Change!200Password@#'),        # Fail: Wrong Old Password
                ('Password@123','Change!200Password@#'),            # Fail: Wrong old password
                ('Password@1textqu#*','change!200password@#'),      # Fail: Upper case missing
                ('Password@1textqu#*', 'change!posPassword@#'),     # fail: Digit missing
                ('Password@1textqu#*', 'change!200@#'),             # Fail: Uppercase missing and Max<18
                ('Password@1textqu#*', 'Change!200@#'),             # Fail: Max<18
                ('Password@1textqu#*', 'change200Passwordtest'),    # Fail: Special char missing
                ('Password@1textqu#*', 'change!20023459966@#'),     # Fail: Digits > 50%
                ('Password@1textqu#*', 'Change!200Change@#'),       # Fail: Repeat chars >4
                ('Password@1textqu#*',''),                          # Fail: New=NULL
                ('Password@1textqu#*', 'change!&*200Password@#'),   # Fail: Special chars >4
                ('', 'Password@1textqu#*'),                         # Fail: Old=NULL
                ('Password@1textqu#*', 'Password@1textqu#*'),       # Fail: Old=New
                ('Password@1textqu#*', 'PASSWORD@12345@#TEST'),     # Fail: Lower case missing
                ('Password@1textqu#*', 'Password@1textqute')]       # Fail: New Password matches more than 80%




    ApiTestData = [{'old': 'Password@1textqu#*', 'newPassword': 'Change@1textqu#*'},    # 1st parameter is wrong/missing
                   {'oldPassword': 'Password@1textqu#*', 'new': 'Change@1textqu#*'},    # 2nd parameter is wrong/missing
                   {'Password': 'Password@1textqu#*', 'Passwordnew': 'Change@1textqu#*'}]   # Both the parameters are wrong




