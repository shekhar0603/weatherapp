from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')
# check by URL : {URL}:{PORT}{route}

@app.route('/weatherapp', methods =['POST','GET'])
def weatherapp():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q' :request.form.get('city'),
        'units' :request.form.get('units'),
        'appid' :request.form.get('apiid'),
        }
    
    response = requests.get(url,params=params)
    data = response.json()
    return f"data: {data} , city : {request.form.get('city')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)