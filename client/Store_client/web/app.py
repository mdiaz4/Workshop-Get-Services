from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/new_store', methods=['GET'])
def person():
    return render_template('new_store.html')


@app.route('/store_detail', methods=['POST'])
def store_detail():
    api_url = "http://127.0.0.1:5000/store"
    name = request.form['name']
    item = request.form['item']
    new_data = {
                    "item": item,
                    "category": {
                        "item": [],
                        "name": "string"
                    },
                    "name": name,
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                            "item": [],
                            "name": "string"
                        }
                    ],
                 
                }
    response = requests.post(api_url, json=new_data)
    return render_template('store_detail.html', value=(name, item))

@app.route('/new_item', methods=['GET'])
def item():
    return render_template('new_item.html')


@app.route('/item_detail', methods=['POST'])
def item_detail():
    api_url = "http://127.0.0.1:5000/item"
    name = request.form['name']
    price = request.form['price']
    new_data = {
                    "price": price,
                    "category": {
                        "item": 0,
                        "name": "string"
                    },
                    "name": name,
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                            "price": 0,
                            "name": "string"
                        }
                    ],
                    
                }
    response = requests.post(api_url, json=new_data)
    return render_template('item_detail.html', value=(name, price))



if __name__ == '__main__':
    app.run(host='127.0.0.1', _Host=800)