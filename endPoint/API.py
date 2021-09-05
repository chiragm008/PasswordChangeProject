from flask import Flask,request,jsonify
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)

changePass = [{ 'oldPassword': 'Password@1', 'newPassword': 'NewPassword@12345' }]


@app.route('/password')
def get_pass():
  return jsonify(changePass)


@app.route('/password', methods=['POST'])
def add_pass():
  changePass.append(request.get_json())
  return 'SUCCESS', 200


if __name__ == '__main__':
    app.run()
