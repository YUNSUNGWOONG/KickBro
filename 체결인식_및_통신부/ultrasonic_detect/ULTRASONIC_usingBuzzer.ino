#define TRIG 9 // TRIG 핀 설정 (초음파 보내는 핀)
#define ECHO 8 // ECHO 핀 설정 (초음파 받는 핀)
#define BUZZER 7 // BUZZER 핀 설정 (부저 핀)

// LED사용 대신에 부저를 사용하도록 수정한 코드

void setup() {
  Serial.begin(9600);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(BUZZER, OUTPUT);

  digitalWrite(BUZZER, LOW); // 부저를 처음에는 꺼둡니다
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
    for (int i = 0; i < 10; i++) { // 부저 울림
      // 거리 재측정
      digitalWrite(TRIG, LOW);
      delayMicroseconds(2);
      digitalWrite(TRIG, HIGH);
      delayMicroseconds(10);
      digitalWrite(TRIG, LOW);

      duration = pulseIn(ECHO, HIGH);
      distance = duration * 17 / 1000;

      if (distance <= 10) {
        digitalWrite(BUZZER, LOW); // 거리 10cm 이하로 측정되면 부저 끔
        break;
      }

      digitalWrite(BUZZER, HIGH);
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
        digitalWrite(BUZZER, LOW); // 거리 10cm 이하로 측정되면 부저 끔
        break;
      }

      digitalWrite(BUZZER, LOW);
      delay(500);
    }
  }
}
