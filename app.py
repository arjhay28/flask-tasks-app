from flask import Flask
from routes import task_routes
from database import  engine
from models import Base

app = Flask(__name__)

Base.metadata.create_all(engine)

app.register_blueprint(task_routes)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
