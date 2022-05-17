from flask import Flask, request

app = Flask('__main__')

'''
Now we put this diccionary to see in postman.
'''
device = {
    "code":"11233",
    "descrip":"Temp. Sensor",
    "value":67
}

'''Now the route is changed and the return too '''
@app.route('/devices', methods=['GET'])
def go_home():
    return device

''' This is to save a user '''
@app.route('/users', methods=['POST'])
def save_user():
    user = request.json
    print(user)
    return user

''' This is to save a device '''
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    return device


if __name__ == '__main__':
    app.run(debug=True, port=5000)