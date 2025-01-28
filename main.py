import flask
from compiler import API
app = flask.Flask(__name__)

client = API("test")

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route("api/save", methods=["POST"])
def save():
    return flask.make_response(client, 200)
if __name__ == '__main__':
    app.run(port=3000)

