from flask import Flask, request

app = Flask(__name__)
items = [
    {
        "name": "Apple",
        "price": 120
    },
    {
        "name":"pizza",
        "price": 150
    },
    {
        "name":"Burger",
        "price": 170
    }
] 
@app.get('/get-items')
def get_items():
    return {"Items": items}

@app.get('/get-item/<string:name>') #dynamic url for the string we are going to receive
def get_item(name):
    for item in items:
        if name == item['name']:
            return item
    return {"Error during retrival!"}

@app.put('/update-item')
def update_item():
    pass




# @app.put('/update-item')
@app.post('/add-items')
def add_items():
    request_data = request.get_json()
    items.append(request_data)
    return {"message":"Items added successfully"}

if __name__ == "__main__":
    app.run(debug=True)
