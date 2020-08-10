from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보기
@app.route('/')
def homework():
    return render_template('index.html')

# 주문하기(POST) API
@app.route('/client', methods=['POST'])
def get_client():
    name = request.form['name_give']
    count = request.form['count_give']
    address = request.form['address_give']
    phone = request.form['phone_give']

    db.homework.insert_one({
        'name': name,
        'count': count,
        'address': address,
        'phone': phone
    })

    return jsonify({'result': 'success','msg': 'POST 연결되었습니다!'})

@app.route('/client',methods=['GET'])
def post_client():
    clients=list(db.homework.find({},{'_id':False}))
    return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!','clients':clients})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)