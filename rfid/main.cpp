#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

String UID = "43 12 9F 94";
bool lock = true;

Servo servo;
LiquidCrystal_I2C lcd(0x27, 20, 4);
MFRC522 rfid(SS_PIN, RST_PIN);


int lcd_print(String message, int x, int y, bool clear) {
    if (clear == true) {
        lcd.clear();
    }

    lcd.setCursor(x, y);
    lcd.print(message);

    return 0;

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
    lcd_print("Welcome!", 6, 1, false);
    lcd_print("Please scan the card", 0, 2, false);
    
    if ( ! rfid.PICC_IsNewCardPresent()) {
        return;
    }

    if ( ! rfid.PICC_READ_CARD_SERIAL()) {
        return;
    }

    lcd_print("Scanning", 0, 0, true);
    lcd_print("Please wait", 0, 1, false);
    Serial.print("UID tag is: ");

    String ID = "";
    for (byte i = 0; i < rfid.uid.size(); i++) {
        lcd.print(".");
        ID.concat(String(rfid.uid.uidByte[i] < 0x10? " 0" : " "));
        ID.concat(String(rfid.uid.uidByte[i], HEX));
        delay(300);

    }

    ID.toUpperCase();

    if (ID.substring(1) == UID) {
        servo.write(160);
        lock = false
        
        while (lock != true) {
            lcd_print("Door opened.", 4, 1, true);
            delay(1500)

        }
    } else {
        lcd_print("Access denied.", 4, 1, true);

    }

}
