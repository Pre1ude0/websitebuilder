import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route()

if __name__ == '__main__':
    app.run(port=3000)

