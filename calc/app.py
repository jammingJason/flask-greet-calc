# Put your app in here.
"""
Simple calculator app

"""
import operations
from flask import Flask, request

app = Flask(__name__)


@app.route('/calc/<operator>', methods=['GET'])
def add_nums(operator):
    args = request.args
    a = args.get('a')
    b = args.get('b')
    if operator == 'add':
        answer = operations.add(a,b)
    if operator == 'sub':
        answer = operations.sub(a,b)
    if operator == 'mult':
        answer = operations.mult(a,b)
    if operator == 'div':
        answer = operations.div(a,b)
    return str(answer)

# @app.route('/calc/sub', methods=['GET'])
# def sub_nums():
#     args = request.args
#     a = args.get('a')
#     b = args.get('b')
#     answer = operations.sub(a,b)
#     return str(answer)

# @app.route('/calc/mult', methods=['GET'])
# def mult_nums():
#     args = request.args
#     a = args.get('a')
#     b = args.get('b')
#     answer = operations.mult(a,b)
#     return str(answer)

# @app.route('/calc/div', methods=['GET'])
# def div_nums():
#     args = request.args
#     a = args.get('a')
#     b = args.get('b')
#     answer = operations.div(a,b)
#     return str(answer)