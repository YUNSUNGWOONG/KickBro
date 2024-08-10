from flask import Flask, render_template
import subprocess
import threading

app = Flask(__name__)                  

@app.route('/')                                     
def hello():       
    return render_template('index.html')

@app.route('/countdown')
def about():
    return render_template('countdown.html')
	
@app.route('/<kickboard_id>')
def hello_user(kickboard_id):
    return render_template('connect.html', user_id=kickboard_id)


# 터미널에서 "mjpg프로그램을 구동하는" 명령어를 실행
def run_mjpg_streamer():
    command = 'mjpg_streamer -i "input_uvc.so -d /dev/video0" -o "output_http.so -w /usr/local/share/mjpg-streamer/www/"'
    
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()
    
    if process.returncode == 0:
        print("Command executed successfully.")
        print(stdout.decode())
    else:
        print("Error executing command.")
        print(stderr.decode())    

if __name__ == '__main__':
    # MJPG Streamer를 별도의 쓰레드로 실행
    mjpg_thread = threading.Thread(target=run_mjpg_streamer)
    mjpg_thread.start()

    # Flask 앱은 메인 스레드에서 실행
    app.run(debug=True, port=80, host='0.0.0.0')

    # MJPG Streamer 쓰레드가 종료되기를 기다림
    mjpg_thread.join()
