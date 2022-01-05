#include <ArduinoJson.h>

DynamicJsonDocument json(1024);

volatile int count = 0;

void pctr() {
  count++;
}

void setup() {
  // put your setup code here, to run once:
  json["type"] = "HE";
  json["ID"] = 0;
  Serial.begin(9600);
  pinMode(2, INPUT);
  attachInterrupt(digitalPinToInterrupt(2), pctr, FALLING);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(60000);
  serialize_reset_data();
}

void serialize_reset_data() {
  json["count"] = count;
  count = 0;
  serializeJson(json, Serial);
  Serial.println();
}