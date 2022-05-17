#include <Arduino.h>
#include <Servo.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>
#include <Chrono.h>

#define SS_PIN 10
#define RST_PIN 9
Chrono mychrono;

Servo servo;
LiquidCrystal_I2C lcd(0x27, 20, 4);
MFRC522 rfid(SS_PIN, RST_PIN);

String UID = "43 12 9F 94", UID_2 = "B3 E5 F 95";
bool lock = true;

void lcd_print(
    String message,
    int x, int y,
    int sdelay,
    bool clear=false,
    bool s_clear=false
  )
{
  if (clear)
  {
    lcd.clear();
  }

  lcd.setCursor(x, y);
  lcd.print(message);

  if (sdelay != 0)
  {
    delay(sdelay);
  }

  if (s_clear)
  {
    lcd.clear();
  }
}

void setup()
{
  Serial.begin(9600);
  servo.write(70);
  lcd.init();
  lcd.backlight();
  servo.attach(3);
  SPI.begin();
  rfid.PCD_Init();
}

void loop()
{
  lcd_print("Welcome!", 6, 1, 0);
  lcd_print("Please scan the card", 0, 2, 0);

  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
  {
    return;
  }

  String ID = "";
  for (byte i = 0; i < rfid.uid.size; i++)
  {
    ID.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
    ID.concat(String(rfid.uid.uidByte[i], HEX));
  }

  ID.toUpperCase();

  lcd_print("Scanning", 0, 0, true);
  lcd_print("Please wait", 0, 1, false);

  // start rfid card recognition
  if (lock)
  {
    if (ID.substring(1) == UID || ID.substring(1) == UID_2)
    {
      lcd_print("Door opened.", 4, 1, true);
      servo.write(160);

      if (rfid.PICC_ReadCardSerial() || mychrono.hasPassed(3000))
      {
        lcd_print("lock here 2.", 4, 1, 0, true, true);
        delay(2000);

      }
      lock = true;
    }
    else
    {
      lcd_print("Access denied.", 4, 1, 0, true, true);
      delay(3000);
    }
  }

}
