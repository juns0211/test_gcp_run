from flask import redirect, Flask
from flasgger import Swagger

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title':'test',
    'openapi':'3.0.0',
    'version':'2.0.1',
    'specs_route':'/'
}
swagger = Swagger()
import test
app.register_blueprint(test.bp)
swagger.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
