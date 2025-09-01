from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "MCP Server is running!"

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
