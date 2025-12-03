from flask import Flask
from routes.main import main_bp
import services.init

app = Flask(__name__)

services.init.get_db()
app.register_blueprint(main_bp,url_prefix='/main')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
