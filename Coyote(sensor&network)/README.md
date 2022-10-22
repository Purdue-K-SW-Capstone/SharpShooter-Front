
# Coyote Team 1: IoT & Network

## LoRaWAN implementation in acoustic and visual detection of coyotes

### Problem Statement

---

In United States, cases of human injuries, loss of pets and livestocks caused by wild coyotes are reported every year. Since wild coyotes usually inhabit in rural area, pets and livestocks in those places are more vulnerable to coyote attacks. However, there are few specialized solution or devices created to solve this problem. 

### Novelty

---

### LoRaWAN
Similar studies whose purpose is to detect animals use WiFi. However to cover large areas such as farmland, it's range of communication is too short. (45 meters at 2.4GHz, 15 meters at 5GHz) Also devices for its communication have high cost, making it totally unaffordable to use in any agricultural solution. This is why LoRaWAN is implemented in this project. It has wider communication range, especially in rural area. (5 kilometers in urban area, 15 kilometers in rural area) And the equipment cost is lower than WiFi.

### Project Overview

---

<img width="633" alt="2022-10-15_architecture" src="https://user-images.githubusercontent.com/48752329/196007372-09234210-6f14-482a-977b-478603fe76ab.png">

### Environment Settings

---

### Sensors
Heltec ESP32 WiFi LoRa 32 (V2)

- ESP32 (dual-core 32-bit MCU + ULP cor) with LoRa node chip SX1276/SX1278

Arduino IDE

- version: 2.0.0 (available on Windows)

- Installation guide: https://docs.heltec.org/en/node/esp32/quick_start.html#via-arduino-board-manager

- board manager for Heltec ESP32 WiFi LoRa 32 (V2) : https://github.com/Heltec-Aaron-Lee/WiFi_Kit_series/releases/download/0.0.6/package_heltec_esp32_index.json 

- end device - server communication guide: https://www.aeq-web.com/lorawan-ttn-mit-heltec-esp32-lora-board-abp-mode/?lang=en

- library used for communication between end device and tts(the things stack): https://github.com/mcci-catena/arduino-lmic

- FFT on ESP32 guide: https://medium.com/swlh/how-to-perform-fft-onboard-esp32-and-get-both-frequency-and-amplitude-45ec5712d7da

MAX4466 Electret Microphone Amplifier

- Datasheet: https://cdn-shop.adafruit.com/datasheets/MAX4465-MAX4469.pdf

### Gateway
RAK7249 WisGate Edge Max from RAKwireless

- User Manual: https://docs.rakwireless.com/Product-Categories/WisGate/RAK7249/Quickstart/

- Configuration Setting to Connect to the TTS(the things stack) server: https://www.thethingsnetwork.org/forum/t/setting-up-basic-station-protocol-on-rak7240-and-rak7249-industrial-gateways/37011/11

### Network

The Things Stack Community Edition v3.22.1

### Group Members

---

- Hyemin Lim
    
    Dept. of Computer Science and Engineering
    
    Chung-Ang University
    
    Seoul, Republic of Korea
    
    lhye9130@gmail.com
    
- Hyeongjun Kim
    
    Computer Engineering
    
    Daegu Catholic University
    
    Gyeongsan-si, Republic of Korea
    
    kim27978965@gmail.com
    
- Jaehui Boo
    
    Computer Engineering
    
    Dankook University
    
    Yongin, Republic of Korea
    
    yeppyboo@gmail.com
    
- Nayoun Kim
    
    Information Technology Convergence
    
    Woosong University
    
    Daejeon, Republic of Korea
    
    nayounkim797@gmail.com
    
- WeiChieh Chin
    
    Computer and Information Technology
    
    Purdue University
    
    West Lafayette, Indiana
    
    victochinr900630@gmail.com
    
- Justin Anderson
    
    Computer and Information Technology
    
    Purdue University
    
    West Lafayette, Indiana
    
    ande1013@purdue.edu
