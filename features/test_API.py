import json
import pytest
from endPoint.EndPointFactory import EndPoint,TestData
from endPoint.API import Password
from getpass import getpass
import requests


#-------------------------------------------Tests-------------------------------------------------------

@pytest.mark.parametrize("oldPassword,newPassword",TestData.Password)
def wtest_case1(oldPassword,newPassword):

    result = Password.ChangePassword(oldPassword, newPassword)
    if result == 1:
        #EndPoint.systemPassword = newPassword

        response = requests.post(EndPoint.BASE_URI_API, data=TestData.Password ,verify=False)
        print("\nPassword changed successfully")

    else:
        print("\nNew Password condition fails, Please check the password requirement and try again")



@pytest.mark.parametrize("oldPassword,newPassword",TestData.Password)
def test_UnitTests(oldPassword,newPassword):

    result = Password.ChangePassword(oldPassword, newPassword)
    if result == 1:

        data = {'oldPassword': oldPassword, 'newPassword': newPassword}
        headers = {"Content-Type": "application/json"}
        response = requests.post(EndPoint.BASE_URI_API, headers=headers, data=json.dumps(data) ,verify=False)
        print("\nStatus Code = ", response.status_code)
        print("Request URL = ", response.url)
        print(response.text)
        print("\nPassword changed successfully")

    else:
        print("\nNew Password condition fails, Please check the password requirement and try again")

@pytest.mark.parametrize("oldPassword,newPassword",TestData.Password)
def test_ApiTests(oldPassword,newPassword):

    result = Password.ChangePassword(oldPassword, newPassword)
    if result == 1:

        data = {'oldPassword': oldPassword, 'newPassword': newPassword}
        headers = {"Content-Type": "application/json"}
        response = requests.post(EndPoint.BASE_URI_API, headers=headers, data=json.dumps(data) ,verify=False)
        print("\nStatus Code = ", response.status_code)
        print("Request URL = ", response.url)
        print(response.text)
        print("\nPassword changed successfully")

    else:
        print("\nNew Password condition fails, Please check the password requirement and try again")

def SystemTest():
    oldPassword = getpass(prompt='Enter current password:')
    newPassword = getpass(prompt='Enter new password:')
    result = Password.ChangePassword(oldPassword, newPassword)
    if result == 1:
        EndPoint.systemPassword = newPassword
        print("Password changed successfully")

    else:
        print("New Password condition fails, Please check the password requirement and try again")