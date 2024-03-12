from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
	return '这是index页面。123456'


@app.route('/hello')
def hello_world():
	return 'Hello, World!'


@app.route('/verify', methods=['POST', 'GET'])
def verify():
	return "这是第 5 个测试。"


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)
