
class EndPoint:
    BASE_URI_API = "http://127.0.0.1:5000/password"
    systemPassword = "Password@1"

#Unit Test Cases--------------------------------------------------------------------------------
class TestData:
    Password = [('Password@1','Change!200Password@#'),
                ('password@1','Change!200Password@#'),
                ('Password@123','Change!200Password@#'),
                ('Password@1','change!200Password@#'),
                ('Password@1','Change!abcPassword@#')]




