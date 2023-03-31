import json
from flask import jsonify, Flask , request
from flask_cors import CORS
app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/',methods = ['GET'])
def Index():
    return "Everything originates here"

@app.route('/api/health')
def health():
    resp = jsonify(health = "healthy")
    resp.status_code = 200
    return resp

 
@app.route('/api/products/',methods = ['GET'])
def allProducts():
    if request.method == 'GET':
        file = open('products.json')
        data = json.load(file)
        file.close()
        return jsonify({
            'status' : 'success',
            'products':data
                        })
    else:
        new_product = request.get_json()
        print(new_product)
        return jsonify({'status' : 'success'})
      
@app.route('/api/products/',methods = ['POST'])
def addProduct():
    response_object = {'status': 'success'}
    new_product = request.get_json()
    with open('products.json','r') as f :
        data = f.read()
    if not data:
        products = [new_product]
    else:
        products = json.loads(data)
        products.append(new_product)
    with open('products.json','w') as f :
        json.dump(products,f)
    response_object['message'] = 'Prodcut added!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(host = 'localhost', port="3000")
#app.run()