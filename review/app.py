from flask import Flask, render_template, request, jsonify
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/name',methods=['GET'])
def my_name():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result':'sueccss','msg': '요청은 GET이다.'})

@app.route('/age',methods=['GET'])
def my_age():
    give_recevie=request.args.get('give_give')
    print(give_recevie)
    return jsonify({'name':'hyeonju','msg':'나야나!'})

@app.route('/age',methods=['POST'])
def my_age2():
    give_recevie=request.form['give_give']
    print(give_recevie)
    return jsonify({'name':'hyeonju','msg':'나는 황현주다!'})

@app.route('/age22',methods=['POST'])
def my_age33():
    give_recevie=request.form['give2_give2']
    print(give_recevie)
    return jsonify({'name':'hyeonju','msg':'요청은 POST고, 나는 황현주다.'})

if __name__=='__main__':
    app.run('localhost', port=5000, debug=True)