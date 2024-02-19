from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

# New route for the /time path
@app.route('/time')
def current_time():
    # Returns the current time in a string format
    return datetime.now().strftime("%H:%M:%S")

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)

