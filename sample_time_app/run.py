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
<<<<<<< HEAD
=======

>>>>>>> 82dd82d3795a36321f3e431e65542adbe53493b9
# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)

