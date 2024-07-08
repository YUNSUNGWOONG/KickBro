#define TRIG 9 // TRIG 핀 설정 (초음파 보내는 핀)
#define ECHO 8 // ECHO 핀 설정 (초음파 받는 핀)
#define LED 7 // LED 핀 설정 (LED 핀)

// 초음파 센서가 계속 거리를 탐지하여 헬멧을 벗었을 때, 10초이상 유지되면 LED가 켜지고,

// LED가 깜빡이는 동안 초음파 센서가 다시 10cm 미만이 되는 순간 LED를 즉시 끄는 코드입니다.

// 헬멧착용을 탐지하는 코드입니다.

void setup() {
  Serial.begin(9600);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(LED, OUTPUT);

  digitalWrite(LED, LOW); // LED를 처음에는 꺼둡니다
}

void loop() {
  long duration, distance;
  unsigned long startTime = millis();
  bool isAboveThreshold = false;

  while (millis() - startTime < 10000) { // 10초 동안 반복
    digitalWrite(TRIG, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);

    duration = pulseIn(ECHO, HIGH);
    distance = duration * 17 / 1000;

    Serial.println(duration);
    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");

    if (distance > 10) {
      isAboveThreshold = true;
    } else {
      isAboveThreshold = false;
      break; // 10센티미터 이하로 측정되면 반복 종료
    }

    delay(1000); // 1초 간격으로 측정
  }

  if (isAboveThreshold) {
    for (int i = 0; i < 10; i++) { // LED 깜빡임
      // 거리 재측정
      digitalWrite(TRIG, LOW);
      delayMicroseconds(2);
      digitalWrite(TRIG, HIGH);
      delayMicroseconds(10);
      digitalWrite(TRIG, LOW);

      duration = pulseIn(ECHO, HIGH);
      distance = duration * 17 / 1000;

      if (distance <= 10) {
        digitalWrite(LED, LOW); // 거리 10cm 이하로 측정되면 LED 끔
        break;
      }

      digitalWrite(LED, HIGH);
      delay(500);

      // 거리 재측정
      digitalWrite(TRIG, LOW);
      delayMicroseconds(2);
      digitalWrite(TRIG, HIGH);
      delayMicroseconds(10);
      digitalWrite(TRIG, LOW);

      duration = pulseIn(ECHO, HIGH);
      distance = duration * 17 / 1000;

      if (distance <= 10) {
        digitalWrite(LED, LOW); // 거리 10cm 이하로 측정되면 LED 끔
        break;
      }

      digitalWrite(LED, LOW);
      delay(500);
    }
  }
}
