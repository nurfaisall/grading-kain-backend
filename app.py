from flask import Flask
from routes.main import main_bp
import services.init
from flask_cors import CORS

ALLOWED_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"]

app = Flask(__name__)

CORS(app)
# CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
# CORS(
#     app,
#     resources={r"/main/*": {"origins": ALLOWED_ORIGINS}},
#     supports_credentials=True,
# )
services.init.get_db()
app.register_blueprint(main_bp, url_prefix="/main")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
