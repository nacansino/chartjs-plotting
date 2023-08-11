import time
import random
from flask import Flask, render_template, jsonify

# Create the Flask instance
app = Flask(__name__)
# Secret key for sessions
app.secret_key = 'your_secret_key'

# Build the main UI

@app.route('/')
def index():
    return render_template('index.html', title='ChartJS sample')

# make a post request that returns a pair of numbers
# the first number shall be a timestamp and the second number shall be a random number
# the timestamp shall be the current time
# the random number shall be between 0 and 100
# the post request shall be made every 200ms
@app.route('/data', methods=['GET'])
def data():
    # get current time
    timestamp = time.time()
    # get random number
    random_number = random.randint(0, 100)
    # return the pair of numbers
    return jsonify({'x': timestamp, 'y': random_number})

if __name__ == "__main__":
    app.run()

