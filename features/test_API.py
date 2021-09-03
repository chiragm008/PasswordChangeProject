import pytest
from endPoint.EndPointFactory import EndPoint,TestData
from endPoint.PasswordChange import Password
from getpass import getpass

def working_code():
    oldPassword = getpass(prompt='Enter current password:')
    newPassword = getpass(prompt='Enter new password:')
    result = Password.ChangePassword(oldPassword, newPassword)
    if result == 1:
        EndPoint.systemPassword = newPassword
        print("Password changed successfully")

    else:
        print("New Password condition fails, Please check the password requirement and try again")

@pytest.mark.parametrize("oldPassword,newPassword",TestData.Password)
def test_case1(oldPassword,newPassword):

    result = Password.ChangePassword(oldPassword, newPassword)
    if result == 1:
        EndPoint.systemPassword = newPassword
        print("\nPassword changed successfully")

    else:
        print("\nNew Password condition fails, Please check the password requirement and try again")