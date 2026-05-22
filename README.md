# Smart Lock System Using Fingerprint

## Overview
This project is a **Fingerprint-Based Smart Door Lock System** developed using **Arduino Uno** and a **Fingerprint Sensor** for secure biometric authentication. The system replaces traditional keys with fingerprint verification, allowing only authorized users to unlock the door.

This project improves security, convenience, and access control by using embedded systems and biometric technology.

---

## Features
- Fingerprint-based biometric authentication
- Secure door locking/unlocking mechanism
- Unauthorized access prevention
- Automatic locking after access
- Fast fingerprint recognition
- Easy user enrollment and deletion
- Arduino-based embedded security system

---

## Components Used
### Hardware
- Arduino Uno
- R307 Fingerprint Sensor Module
- Solenoid Door Lock (12V)
- Single Channel Relay Module
- 12V DC Power Adapter
- Connector Jack
- Jumper Wires
- Breadboard

### Software
- Arduino IDE
- Embedded C/C++
- Adafruit Fingerprint Library

---

## Working Principle
1. User places finger on the fingerprint sensor.
2. Sensor captures the fingerprint image.
3. Arduino compares the fingerprint with stored templates.
4. If fingerprint matches:
   - Relay activates
   - Solenoid lock unlocks the door
   - Access remains open for 3 seconds
   - Door locks automatically
5. If fingerprint does not match:
   - Access is denied
   - Door remains locked

---

## Block Diagram
```text
Fingerprint Sensor → Arduino Uno → Relay Module → Solenoid Lock
                           ↑
                    Power Supply