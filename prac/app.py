from flask import Flask, render_template, request, jsonify

app=Flask(__name__)

@app.route('/')
def hyeon_ju():
    return render_template('index.html')

@app.route('/text', methods=['GET'])
def text_get():
    title_recive = request.args.get('title_give')
    print(title_recive)
    return jsonify({'result':'success','msg':'이 요청은 GET입니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

