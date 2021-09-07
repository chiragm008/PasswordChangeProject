1. Run this command from the terminal (Project Location:.\PasswordChangeProject\endPoint) to start the API server:
->   **_python API.py_**


2. To Execute the tests, Run the following command (from the Project Location:.\PasswordChangeProject\features):
->   **_pytest -v --html=report.html_**

    It will run all the tests (Unit/API) and generate a report at the same location.


3. To run individual tests, use markers (unittest/apitest):
->   **_pytest -v -m unittest --html=report.html_**
->   **_pytest -v -m apitest --html=report.html_**


NOTE: Framework Used: Flask and Pytest
NOTE: Function Code and API creation Code is present at: .\endPoint\API.py
NOTE: All the test scenarios and logic is present in TDD format at: .\features\test_API.py
NOTE: All the test Data and server info is present at: .\endPoint\EndPointFactory.py
NOTE: Report will be generated at: .\features\report.html
NOTE: We need to connect to the local API server in order to run the API tests.
