from app import app
import os
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
if __name__ == '__main__':
    # app.secret_key = os.urandom(12)

    # app.config["FLASK_APP"] = run.py
    # export FLASK_APP=run.py
    app.run(host='127.0.0.1', port=5000)
