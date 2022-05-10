#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

String UID = "43 12 9F 94", UID_2 = "B3 E5 F 95";
bool lock = true, check;

Servo servo;
LiquidCrystal_I2C lcd(0x27, 20, 4);
MFRC522 rfid(SS_PIN, RST_PIN);


void lcd_print(String message, int x, int y, bool clear) {
    if (clear == true) {
        lcd.clear();
    }

    lcd.setCursor(x, y);
    lcd.print(message);

}

bool checker(bool init_) {
    if (init_ == true) {
        if ( ! rfid.PICC_IsNewCardPresent() || ! rfid.PICC_READ_CARD_SERIAL()) {
            return false;
        } 
    } else {
        if ( ! rfid.PICC_IsNewCardPresent() || ! rfid.PICC_READ_CARD_SERIAL()) {
            return false;
        } else {
            return true;
        }
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
    lcd_print("Welcome!", 6, 1, false);
    lcd_print("Please scan the card", 0, 2, false);
    check = checker();

    if (check == false) {
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


    // start rfid card recognition
    if (ID.substring(1) == UID || ID.substring(1) == UID_2) {
        servo.write(160);
        lock = false;
        
        while (lock != true) {
            if (lock == false) {
                break;
            
            }

            lcd_print("Door opened.", 4, 1, true);
            delay(1500);
            check_2 = checker();
            if (check == true) {
                lock = false;
                servo.write(70);
                continue;

            }

        }
    } else {
        lcd_print("Access denied.", 4, 1, true);

    }

}
