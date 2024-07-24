from flask import Flask              

app = Flask(__name__)                  

@app.route('/')                                     
def hello():       
    return '킥보드 이용이 시작되었습니다!<br>헬멧을 손잡이로부터 분리해주십시오!'

@app.route('/countdown')
def about():
	return 'This is countdown page'

@app.route('/unlock')
def about():
	return 'This is unlock page'

@app.route('/temp_lock')
def about():
	return 'This is temp_lock page'


if __name__ == '__main__':  
    app.run(debug=True, port=80, host='0.0.0.0')
