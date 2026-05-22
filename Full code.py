Fingerprint Enrollment Code:
#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

uint8_t id;

void setup()
{
  Serial.begin(9600);
  finger.begin(57600);

  if (finger.verifyPassword())
  {
    Serial.println("Fingerprint sensor found");
  }
  else
  {
    Serial.println("Fingerprint sensor not found");
    while (1);
  }
}

uint8_t readnumber()
{
  uint8_t num = 0;

  while (num == 0)
  {
    while (!Serial.available());
    num = Serial.parseInt();
  }

  return num;
}

void loop()
{
  Serial.println("Enter ID (1 to 127):");
  id = readnumber();

  if (id == 0)
    return;

  enrollFingerprint();
}

uint8_t enrollFingerprint()
{
  int p = -1;

  Serial.print("Place finger for ID ");
  Serial.println(id);

  while (p != FINGERPRINT_OK)
  {
    p = finger.getImage();
  }

  p = finger.image2Tz(1);
  if (p != FINGERPRINT_OK)
    return p;

  Serial.println("Remove finger");
  delay(2000);

  p = 0;
  while (p != FINGERPRINT_NOFINGER)
  {
    p = finger.getImage();
  }

  Serial.println("Place same finger again");

  p = -1;
  while (p != FINGERPRINT_OK)
  {
    p = finger.getImage();
  }

  p = finger.image2Tz(2);
  if (p != FINGERPRINT_OK)
    return p;

  p = finger.createModel();
  if (p != FINGERPRINT_OK)
    return p;

  p = finger.storeModel(id);
  if (p == FINGERPRINT_OK)
  {
    Serial.println("Fingerprint Stored Successfully");
  }

  return p;
}

Working Code for Fingerprint Lock System:
#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

#define RELAY_PIN 4
#define ACCESS_DELAY 3000

void setup()
{
  finger.begin(57600);
  delay(5);

  if (finger.verifyPassword())
  {
    Serial.begin(9600);
    Serial.println("Fingerprint sensor detected");
  }
  else
  {
    Serial.begin(9600);
    Serial.println("Fingerprint sensor not found");
    while (1)
    {
      delay(1);
    }
  }

  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH);
}

void loop()
{
  if (getFingerprintID() != -1)
  {
    digitalWrite(RELAY_PIN, LOW);
    delay(ACCESS_DELAY);
    digitalWrite(RELAY_PIN, HIGH);
  }

  delay(50);
}

int getFingerprintID()
{
  int p = finger.getImage();
  if (p != FINGERPRINT_OK)
    return -1;

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK)
    return -1;

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)
    return -1;

  Serial.print("Access Granted. Finger ID: ");
  Serial.println(finger.fingerID);

  return finger.fingerID;
}