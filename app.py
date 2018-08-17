from flask import Flask
from apis import blueprint as api
from apiv2 import blueprint as api2
from apiv3 import blueprint as api3

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(api, url_prefix='/api/1')
app.register_blueprint(api2)
app.register_blueprint(api3)

# load configuration
app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
