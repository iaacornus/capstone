#include <Arduino.h>
#include <Servo.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>
#include <Chrono.h>

#define SS_PIN 10
#define RST_PIN 9

Chrono timer;
Servo servo;
LiquidCrystal_I2C lcd(0x27, 20, 4);
MFRC522 rfid(SS_PIN, RST_PIN);

String UID = "43 12 9F 94", UID_2 = "B3 E5 F 95"; // reference UID
bool lock = true;

void lcd_print(
        String message,
        int x, int y,
        int sdelay,
        bool clear=false,
        bool s_clear=false
    ) {
    if (clear) {
        lcd.clear();
    }

    lcd.setCursor(x, y);
    lcd.print(message);

    if (sdelay != 0) {
        delay(sdelay);
    }

    if (s_clear) {
        lcd.clear();
    }

}

void setup() {
    Serial.begin(9600);
    servo.write(70);
    lcd.init();
    lcd.backlight();
    servo.attach(3);
    SPI.begin();
    rfid.PCD_Init();

}

void loop() {
    lcd_print("Welcome", 6, 1, 0);
    lcd_print("Please scan the card", 0, 2, 0);

    if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial()) {
        return;
    }

    String ID = "";
    for (byte i = 0; i < rfid.uid.size; i++) {
        ID.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
        ID.concat(String(rfid.uid.uidByte[i], HEX));
    }
    ID.toUpperCase();

    if (ID.substring(1) == UID || ID.substring(1) == UID_2) {
        lock = false;
        lcd_print("Door opened.", 4, 1, 3000, true, true);

        if (timer.hasPassed(3000) || rfid.PICC_ReadCardSerial()) {
            timer.restart();
            lcd_print("Door locked.", 4, 1, 3000, true, true);
            lock = true;

        }

    } else {
        lcd_print("Access denied.", 4, 1, 5000, true, true);
    }

}
