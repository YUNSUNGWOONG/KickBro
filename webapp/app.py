from flask import Flask, render_template

app = Flask(__name__)                  

@app.route('/')                                     
def hello():       
    return render_template('index.html')

@app.route('/countdown')
def about():
    return render_template('countdown.html')
    
# @app.route('/contact')
# def contact():
#     return 'This is contact page'
	
@app.route('/<kickboard_id>')
def hello_user(kickboard_id):
    return render_template('connect.html', user_id=kickboard_id)

if __name__ == '__main__':  
    app.run(debug=True, port=80, host='0.0.0.0')
