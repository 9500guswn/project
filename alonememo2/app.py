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
@app.route('/receive', methods=['POST'])
def post_receive():
    n = request.form['n_give']
    c = request.form['c_give']
    a = request.form['a_give']
    p = request.form['p_give']

    db.home.insert_one({
    'n':n,
    'c':c,
    'a':a,
    'p':p
    })

    return jsonify({'result': 'success','msg': 'POST 연결되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/receive', methods=['GET'])
def get_receive():
    receive=list(db.home.find({},{'_id':False}))
    return jsonify({'result': 'success','msg': 'GET 연결되었습니다!','receive':receive})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)