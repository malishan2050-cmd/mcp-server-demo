from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "name": "Render MCP Demo",
        "tools": []
    })

if __name__ == "__main__":
    # 这里读取环境变量 PORT，Railway 会传 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
