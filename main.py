import flask
from file_exchanger import API
app = flask.Flask(__name__)

client = API("test")

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route("/api/load", methods=["GET"])
def save():
    inc_data = flask.request.json["json"]
    client.write_json(inc_data)
    return flask.make_response(client.read_json(file="test"), 200)

@app.route("/api/get", methods=["POST"])
def send():
    return flask.make_response(client.read_json(file="test"), 200)

if __name__ == '__main__':
    app.run(port=3000)

