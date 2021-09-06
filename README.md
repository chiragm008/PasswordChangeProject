1. Run this command from the terminal (Project Location:.\PasswordChangeProject\endPoint) to start the API server:
->   **_python API.py_**
2. To Execute the tests, Run the following commands (from the Project Location:.\PasswordChangeProject\features):
->   **_pytest -v --html=report.html_**
    It will run all the tests (Unit/API/System) and generate a report at the same location.
   1. To run individual tests, use markers (unittest/apitest/systemtest):
->   **_pytest -v -m unittest --html=report.html_**
->   **_pytest -v -m apitest --html=report.html_**
->   **_pytest -v -m systemtest --html=report.html_**



