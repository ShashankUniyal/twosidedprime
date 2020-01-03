from flask import Flask, jsonify, request
import Utility

app = Flask(__name__)

@app.route("/doublesidedprime/<input>")
def doublesidedprime(input):
    try:
        num = round(float(input))
        result = Utility.twosidedprime(num)
        print(result)
        return {"StatusCode": "200", "Result": str(result)}
    except:
        return {"Result": "Wrong Input! Enter the number value"}


# main driver function
if __name__ == '__main__':
    app.run()