import json
import pytest
from endPoint.EndPointFactory import EndPoint, TestData
from endPoint.API import Password
import requests


# -------------------------------------------Unit Tests-------------------------------------------------------

# Unit Test to check all the success cases (with valid old password which matches system and a valid new password)
@pytest.mark.unittest
@pytest.mark.parametrize("oldPassword,newPassword", TestData.UnitTestSuccess)
def test_UnitTestsSuccess(oldPassword, newPassword):
    result = Password.ChangePassword(oldPassword, newPassword)
    assert result == 1
    print('\nPassword Changed Successfully')


# Unit Test to check all the failure cases (Either invalid old password or invalid new password)
@pytest.mark.unittest
@pytest.mark.parametrize("oldPassword,newPassword", TestData.UnitTestFail)
def test_UnitTestsFail(oldPassword, newPassword):
    result = Password.ChangePassword(oldPassword, newPassword)
    assert result == 0
    print('\nPassword is Invalid, Please try again')


# -------------------------------------------API Tests-------------------------------------------------------

# API Tests to check all the 200 SUCCESS status
@pytest.mark.apitest
@pytest.mark.parametrize("oldPassword,newPassword", TestData.UnitTestSuccess)
def test_ApiTests_200(oldPassword, newPassword):
    data = {'oldPassword': oldPassword, 'newPassword': newPassword}
    headers = {"Content-Type": "application/json"}
    response = requests.post(EndPoint.BASE_URI_API, headers=headers, data=json.dumps(data), verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    print(response.text)
    assert response.status_code == 200


# API Tests to check all the 404 FAILURE:NOT FOUND status
@pytest.mark.apitest
@pytest.mark.parametrize("oldPassword,newPassword", TestData.UnitTestFail)
def test_ApiTests_404(oldPassword, newPassword):
    data = {'oldPassword': oldPassword, 'newPassword': newPassword}
    headers = {"Content-Type": "application/json"}
    response = requests.post(EndPoint.BASE_URI_API, headers=headers, data=json.dumps(data), verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    print(response.text)
    assert response.status_code == 404


# API Tests to check all the 400 FAILURE:BAD REQUEST status
@pytest.mark.apitest
@pytest.mark.parametrize("oldPassword,newPassword", TestData.ApiTestData)
def test_ApiTests_400(oldPassword, newPassword):
    headers = {"Content-Type": "application/json"}
    response = requests.post(EndPoint.BASE_URI_API, headers=headers, data=json.dumps(TestData.ApiTestData),
                             verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    print(response.text)
    assert response.status_code == 400
