from flask import Flask, render_template      #플라스크 모듈에서 클래스와 함수 불러오기
from gpiozero import LEDBoard                #gpiozero라이브러리에서 LEDBoard 클래스 불러오기

app = Flask(__name__)                        # 앱생성


leds = LEDBoard(14, 15, 18)                 #leds 객체 생성

led_states = {                            # leds의 상태 정보 저장을 위한 데이터
    'red':0,
    'green':0,
    'blue':0
}

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/<color>/<int:state>')
def led_switch(color, state):
    led_states[color] = state
    leds.value=tuple(led_states.values())
    return render_template('index.html', led_states=led_states)




if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')


