from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        league = request.form['league']
        season = request.form['season']
        
        # Make a request to the API using user input
        response = requests.get(f"https://api-football-standings.azharimm.dev/standings/{league}/{season}")
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Pass the data to the template
            return render_template('display_data.html', data=data)
        else:
            return "Error fetching data from the API"

if __name__ == '__main__':
    app.run(debug=True)