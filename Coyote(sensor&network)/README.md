
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

<img width="633" alt="2022-10-15_architecture" src="https://user-images.githubusercontent.com/48752329/207974403-54748460-8ba1-49e5-918d-5d0020049919.png">

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

### Node.js Server

dependencies
- body-parser 1.20.1
- cors 2.8.5
- dotenv 16.0.3
- express 4.18.2
- moment 2.29.4
- mongoose 6.7.3
- nodemon 2.0.20
- websocket 1.0.34
- ws 8.11.0

start server
- type 'npm start'

### Unity

version
- 2021.3.9f1

Imported files and assets
- Jobs
- NodeJS plugins for Unity
- MapBox SDK (https://docs.mapbox.com/unity/maps/guides/)
- websocket-sharp.dll (https://github.com/sta/websocket-sharp)
- simple Android notifications free (https://assetstore.unity.com/packages/tools/integration/simple-android-notifications-free-68626)
- Clean Setting UI (https://assetstore.unity.com/packages/tools/gui/clean-settings-ui-65588)
- Loading screen animation (https://assetstore.unity.com/packages/tools/loading-screen-animation-98505)
- TextMesh Pro (download: Unity Editor -> window -> asset)

Configuration before executing

 1. Make sure to insert the Unity Scene File before running
 2. Unity Editor → File → Build setting → Putting a Assets/Scenes/LoadingScene, Assets/Scenes/Coyote inside ‘Scenes in Build’
 3. Unity Editor → Edit → Project settings → Player → Android → OtherSettings → Identification → Set ‘Minimum API Level’ to Android 7.0 ‘Nougat’ (API Level 24), Set ‘Target API Level’ to Automatic(highest installed)
 4. Unity Editor → File → Build setting → Platform →Set to ‘Android’
 5. If you downloaded MapBox SDK again, change the SDK script `DeviceLocationProvider.cs` to code/unity/DeviceLocationProvider.cs
        
 6. How to set up a Mobile Phone Connection Environment for Project Run
 
        1. Install the Unity Remote5 app on your phone device
        2. Go to your phone developer options → Set USB Debugging Permissions to Allow
        3. Unity Editor → Edit → Project settings → Editor → Unity Remote → Set ‘Device Settings’ to ‘Any Android Device’
        4. Run the Unity Remote5 app on your phone → Connect your phone to your computer (data cable) → Project Run

 7. Android only (version: Android 7.0 'Nougat', API Level 24 or higher)

Error debugging
- "namespace name does not exist" during MapBox SDK import": an error related to Mapbox AR, resolved after deleting all AR-related files in Mapbox.
- "warning: the option setting 'android.enabler8=false' is deprecated. it will be removed in version 5.0 of the android gradle plugin. you will no longer be able to disable r8", "starting a gradle daemon, 1 incompatible daemon could not be reused, use --status for details": an error due to android gradle file, resolved after changing version from com.android.tools.build:gradle:3.6.0 to 3.4.0 inside the 'baseProjectTemplate.gradle' file.
- "manifest merger failed 22 cannot be smaller than version 24 declared in library error": an error related to version error of minSDK and targetSDK in the AndroidManifest.xml in the Unity library file.
- "Import error: the name 'heading' does not exist in the current context": an error in DeviceLocationProvider.cs script file due to encoding issue. Change encoding method from ISO-8859 to UTF-8 or ASCII.

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
