import requests
from pprint import pprint
from flask import Flask , render_template

# get github username here
username = "princu09"

# Github API
url = f"https://api.github.com/users/{username}"

# get User data
user_data = requests.get(url).json()

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template("index.html" , user_data=user_data)

if __name__ == "__main__":
    app.run(debug=True)