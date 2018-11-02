#define POT_PIN A0

int rotation = 0;

void setup() {
    pinMode(POT_PIN, INPUT);
    Serial.begin(9600);
}

void loop() {
    rotation = analogRead(POT_PIN);
    Serial.println(rotation);
    delay(200);
}