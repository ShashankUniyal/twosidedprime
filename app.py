from flask import Flask, jsonify, request
import Utility
import math

app = Flask(__name__)

def isprime(num):
    no = int(num)
    if no <= 1:
        return False
    elif (no == 2) or (no == 3):
        return True
    elif (no % 2 == 0) or (no % 3 == 0):
        return False
    else:
        for i in range(2, math.floor(no / 2)):
            if no % i == 0:
                return False
            continue
        return True


def twosidedprime(number):
    # num = input('Enter the number:')
    num = str(number)
    num_length = len(num)
    print(num_length);
    if num_length == 1:
        return isprime(num)
    else:
        print('')
        return isprime(num) and truncateleft(num, num_length) and truncateright(num, num_length)


def truncateleft(num, num_length):
    if num_length == 1:
        return isprime(num)
    i = num[1: num_length + 1]
    return isprime(i) and truncateleft(i, len(i))


def truncateright(num, num_length):
    if num_length == 1:
        return isprime(num)
    j = num[0: num_length - 1]
    return isprime(j) and truncateright(j, len(j))



@app.route('/', methods=['GET', 'POST'])
def home():
    data = "hello world"
    return jsonify({'data': data})


@app.route("/doublesidedprime/<input>")
def doublesidedprime(input):
    try:
        num = int(input)
        result = twosidedprime(num)
        print(result)
        return {"StatusCode": "200", "Result": str(result)}
    except:
        return {"Result": "Wrong Input! Enter the number value"}


# main driver function
if __name__ == '__main__':
    app.run()