from flask import Flask, jsonify
from flask_restful import Api, reqparse
import re
from collections import Counter
from difflib import SequenceMatcher

app = Flask(__name__)
api = Api(app)

# ----------------------------------------------Hardcoded Test Data---------------------------------------------

systemPassword = 'Password@1textqu#*'
changePass = []


# ---------------------------------------------Change Password Function--------------------------------------

class Password:
    def ChangePassword(oldPassword, newPassword):
        if not (oldPassword == systemPassword):
            print('Old Password is not same as system Password')
            return 0
        if not (int(SequenceMatcher(None, oldPassword, newPassword).ratio() * 100) < 80):
            return 0

        l = list((dict(Counter(newPassword))).values())
        l1 = [i for i in l if i != 1]

        if (len(newPassword) >= 18) and (re.search('[a-z]', newPassword)) and (
                re.search('[A-Z]', newPassword)) and (
                re.search('[0-9]', newPassword)) and (
                re.search('[!@#$&*]', newPassword)) and (len(re.findall('[!@#$&*]', newPassword)) <= 4) and (
                len(newPassword) / 2 > len(re.findall('[0-9]', newPassword))) and (len(l1) <= 4):
            print('SUCCESS')
            return 1
        else:
            print(
                "New Password condition is not matching (Password length should be 18, 1 each of (uppercase,"
                "lowercase,digit,special chars-> !@#$&* (Max can be 4)), Duplicate repeat char not more tha 4, "
                "50% of password should not be number")
            return 0


# --------------------------------API to Change Password-----------------------------------------------------

@app.route('/password')
def get_pass():
    return jsonify(changePass)


@app.route('/password', methods=['POST'])
def add_pass():
    parser = reqparse.RequestParser()
    parser.add_argument('oldPassword', required=True)
    parser.add_argument('newPassword', required=True)
    args = parser.parse_args()

    func = Password.ChangePassword(args['oldPassword'], args['newPassword'])

    if args['oldPassword'] == '':
        return {
                   'message': "Old Password cannot be blank"
               }, 404
    elif args['oldPassword'] != systemPassword:
        return {
                   'message': "Old Password is not matching the system Password"
               }, 404
    elif args['newPassword'] == systemPassword:
        return {
                   'message': "New Password cannot be same as the Existing Password."
               }, 404
    elif args['newPassword'] == '':
        return {
                   'message': "New Password cannot be blank"
               }, 404
    elif func == 0:
        return {
                   'message': "New Password is Invalid"
               }, 404
    else:
        changePass.append(args)

    return {'data': args}, 200


if __name__ == '__main__':
    app.run()
