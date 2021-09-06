import json
import pytest
from endPoint.EndPointFactory import EndPoint,TestData
from endPoint.API import Password
from getpass import getpass
import requests


#-------------------------------------------Unit Tests-------------------------------------------------------

@pytest.mark.unittest
@pytest.mark.parametrize("oldPassword,newPassword",TestData.UnitTestSuccess)
def test_UnitTestsSuccess(oldPassword,newPassword):
    result = Password.ChangePassword(oldPassword, newPassword)
    assert result==1
    print('\nPassword Changed Successfully')

@pytest.mark.unittest
@pytest.mark.parametrize("oldPassword,newPassword",TestData.UnitTestFail)
def test_UnitTestsFail(oldPassword,newPassword):
    result = Password.ChangePassword(oldPassword, newPassword)
    assert result==0
    print('\nPassword is Invalid, Please try again')

#-------------------------------------------API Tests-------------------------------------------------------

@pytest.mark.apitest
@pytest.mark.parametrize("oldPassword,newPassword",TestData.UnitTestSuccess)
def test_ApiTests_200(oldPassword,newPassword):
    data = {'oldPassword': oldPassword, 'newPassword': newPassword}
    headers = {"Content-Type": "application/json"}
    response = requests.post(EndPoint.BASE_URI_API, headers=headers, data=json.dumps(data), verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    print(response.text)
    assert response.status_code == 200

@pytest.mark.apitest
@pytest.mark.parametrize("oldPassword,newPassword",TestData.UnitTestFail)
def test_ApiTests_404(oldPassword,newPassword):
    data = {'oldPassword': oldPassword, 'newPassword': newPassword}
    headers = {"Content-Type": "application/json"}
    response = requests.post(EndPoint.BASE_URI_API, headers=headers, data=json.dumps(data), verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    print(response.text)
    assert response.status_code==404

@pytest.mark.apitest
@pytest.mark.parametrize("oldPassword,newPassword",TestData.ApiTestData)
def test_ApiTests_400(oldPassword,newPassword):
    headers = {"Content-Type": "application/json"}
    response = requests.post(EndPoint.BASE_URI_API, headers=headers, data=json.dumps(TestData.ApiTestData), verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    print(response.text)
    assert response.status_code==400


@pytest.mark.systemtest
def stest_SystemTest():
    oldPassword = getpass(prompt='Enter current password:')
    newPassword = getpass(prompt='Enter new password:')
    result = Password.ChangePassword(oldPassword, newPassword)
    if result == 1:
        EndPoint.systemPassword = newPassword
        print("Password changed successfully")

    else:
        print("New Password condition fails, Please check the password requirement and try again")