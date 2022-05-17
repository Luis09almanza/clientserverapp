''' Import the libraries '''
from flask import Flask, request

''' This is to run our application with flask'''
app = Flask('__main__')

''' This is the route of our application with the method in this case GET ''' 
@app.route('/', methods=['GET'])
def go_home():
    return 'Hola mundo'

''' We defined a point of entrance to run our application in the port 5000 '''
if __name__ == '__main__':
    app.run(debug=True, port=5000)