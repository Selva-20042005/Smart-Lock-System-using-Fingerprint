# 🔐 Smart Lock System Using Fingerprint

> A biometric door security system built using **Arduino Uno**, **R307 Fingerprint Sensor**, and **Solenoid Lock** for secure access control.

![Arduino](https://img.shields.io/badge/Arduino-Uno-blue)
![C++](https://img.shields.io/badge/Language-C++-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Security](https://img.shields.io/badge/Security-Biometric-red)

---

## 📌 Overview
Traditional lock-and-key systems can be lost, duplicated, or misused. This project solves that problem by implementing a **Fingerprint-Based Smart Lock System** using biometric authentication.

Only authorized fingerprints can unlock the door, making the system secure, fast, and user-friendly.

### ✨ Features
✅ Fingerprint authentication  
✅ Automatic door locking  
✅ Unauthorized access prevention  
✅ Fast recognition system  
✅ Secure biometric verification  
✅ Arduino-based implementation  
✅ Easy enrollment of new users  

---

## 🛠 Hardware Components
| Component | Quantity |
|---------|----------|
| Arduino Uno | 1 |
| R307 Fingerprint Sensor | 1 |
| Solenoid Lock (12V) | 1 |
| Single Channel Relay Module | 1 |
| 12V DC Adapter | 1 |
| Jumper Wires | As required |
| Breadboard | 1 |

---

## 💻 Software Requirements
- Arduino IDE
- Adafruit Fingerprint Sensor Library
- SoftwareSerial Library

---

## 🧠 System Architecture
```text
Fingerprint Sensor
      ↓
Arduino Uno
      ↓
Relay Module
      ↓
Solenoid Lock
```

---

## 🔌 Circuit Connections

### Fingerprint Sensor → Arduino
| Sensor Pin | Arduino Pin |
|----------|-------------|
| VCC | 5V |
| GND | GND |
| TX | D2 |
| RX | D3 |

### Relay Module → Arduino
| Relay Pin | Arduino Pin |
|---------|-------------|
| VCC | 5V |
| GND | GND |
| IN | D4 |

### Solenoid Lock
- Connected via relay COM and NO terminals
- Powered using 12V adapter

---

# 📂 Code Overview

This project contains **two main Arduino programs**:

### 1️⃣ Fingerprint Enrollment Code
Used to register fingerprints into sensor memory.

Functions:
- Detect fingerprint
- Capture fingerprint twice
- Compare fingerprint
- Store template

### 2️⃣ Smart Lock Access Code
Used for real-time authentication.

Functions:
- Scan fingerprint
- Match stored template
- Unlock door
- Auto lock after 3 seconds

---

# 🧾 Code Snippets

## Fingerprint Detection
```cpp
int p = finger.getImage();
if (p != FINGERPRINT_OK)
  return -1;
```

## Fingerprint Matching
```cpp
p = finger.fingerFastSearch();
if (p != FINGERPRINT_OK)
  return -1;
```

## Unlock Door
```cpp
digitalWrite(RELAY_PIN, LOW);
delay(3000);
digitalWrite(RELAY_PIN, HIGH);
```

---

# 🚀 Build & Upload

## Step 1: Install Arduino IDE
Download Arduino IDE and install it.

---

## Step 2: Install Libraries
Install:
- Adafruit Fingerprint Sensor Library
- SoftwareSerial

Arduino IDE:
Sketch → Include Library → Manage Libraries

---

## Step 3: Connect Hardware
Make all hardware connections as shown above.

---

## Step 4: Upload Enrollment Code
Upload fingerprint enrollment code first.

Then:
- Open Serial Monitor
- Enter ID (1–127)
- Place finger twice

---

## Step 5: Upload Lock Code
Upload smart lock access code.

---

## Step 6: Power System
Provide:
- 5V for Arduino
- 12V for Solenoid Lock

---

# 🧪 Testing

## Test Case 1: Authorized Finger
Expected:
✅ Finger detected  
✅ Finger matched  
✅ Relay activates  
✅ Door unlocks for 3 seconds  
✅ Auto locks  

---

## Test Case 2: Unauthorized Finger
Expected:
❌ Finger mismatch  
❌ Relay remains OFF  
❌ Door remains locked  

---

## Test Case 3: No Finger
Expected:
⏳ System waits for input

---

# 🔍 Troubleshooting

## Sensor Not Detected
Possible causes:
- Wrong TX/RX connection
- Loose wires
- Incorrect baud rate

Fix:
```cpp
finger.begin(57600);
```

---

## Fingerprint Not Matching
Possible causes:
- Dirty sensor
- Wet finger
- Improper enrollment

Fix:
- Clean sensor
- Re-enroll fingerprint

---

## Relay Not Working
Check:
- Relay wiring
- D4 connection
- Relay type (LOW trigger)

Fix:
```cpp
digitalWrite(RELAY_PIN, HIGH);
```

---

## Door Not Unlocking
Possible causes:
- Weak power supply
- Solenoid incorrect voltage

Fix:
Use:
12V 2A adapter

---

# 🔐 Security Check

### Strengths
✅ Unique biometric authentication  
✅ No physical keys  
✅ Automatic locking  
✅ Fast access control  

### Risks
⚠ Finger spoofing  
⚠ Power failure disables system  
⚠ Sensor contamination  

### Recommended Improvements
- Add battery backup
- Add buzzer alarm
- Add failed attempt counter
- Add OTP backup unlock
- Add anti-spoof fingerprint detection

---

# 📈 Roadmap

## Version 1.0
✅ Basic fingerprint lock  
✅ Relay-based door control  
✅ Finger enrollment  

---

## Version 2.0
🚀 LCD display integration  
🚀 Buzzer alerts  
🚀 Failed attempt lockout  

---

## Version 3.0
🚀 Wi-Fi connectivity  
🚀 Mobile app control  
🚀 Remote notifications  

---

## Version 4.0
🚀 Face recognition  
🚀 Cloud access logs  
🚀 IoT smart home integration  

---

# 📊 Project Workflow
```text
Start
 ↓
Scan Fingerprint
 ↓
Capture Image
 ↓
Convert Template
 ↓
Search Database
 ↓
Match Found?
 ├── YES → Unlock Door → Delay → Lock
 └── NO  → Access Denied
```

---

# 🎯 Applications
🏠 Home security  
🏢 Office access control  
🔒 Locker security  
🏫 Attendance systems  
🧪 Restricted lab access  

---

# 👨‍💻 Technologies Used
- Arduino Uno
- Embedded C++
- Biometrics
- Relay Control
- Access Control Systems

---

