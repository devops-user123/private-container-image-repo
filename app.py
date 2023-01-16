from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return f"Hello {os.environ['DEPLOY_ENV']} Kube!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)