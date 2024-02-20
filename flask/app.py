from flask import Flask

## creating a simple flask application

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)