# Team: SharpShooter

## Title

Outdoor Long Range Ubiquitous Projectiles Tracking System Using P-MPLR and Computer Vision

### Group Members

| Name             | University                 | Department                                   | Email                 | Contact                           |
| ---------------- | -------------------------- | -------------------------------------------- | --------------------- | --------------------------------- |
| Donghyeon Na     | Sangmyung University       | Dept. of Human Centered AI                   | skehdgus401@gmail.com | https://github.com/xialGuri       |
| Hansu Jeong      | Sangmyung University       | Dept. of Computer Science                    | 7471919@naver.com     | https://github.com/8471919        |
| Minjae Kim       | KyungHee University        | Dept. of Software Convergence                | kmj5596@khu.ac.kr     | https://github.com/MinJaeKim2796  |
| Jeongwon Moon    | Kyungpook Nat’l University | Dept. of Computer Science & Engineering      | bella7365@knu.ac.kr   | https://github.com/gaarden        |
| Woojin Choi      | Sun Moon University        | Dept. of Computer Science & Engineering      | twinsno119@gmail.com  | https://github.com/woojin-choi518 |
| Ethan O'Sullivan | Purdue University          | Dept. of Computer and Information Technology | ethanext17@gmail.com  | https://github.com/ethanext       |
| Sophia Kim       | Purdue University          | Dept. of Computer and Information Technology | phia9130@gmail.com    | https://github.com/lee3155        |

---

## Problem Statement

Shotmarker is a program designed for a F-class shooting competition, which is conducted from 300 to 1000 yards only using prone position. This system has several complications, initially, it is overpriced. Secondly, this system depends on environmental factors such as wind and rain. The average error in an ideal state is within 2~3mm, but an error rate can be higher when the weather is not at its best for shooting. Lastly, this system is dedicated to a specific type of gun, a gun that uses supersonic bullet. In other words, if the gun does not use a supersonic bullet Shotmarker is not functional. For the gunshot detection, ShotSpotter is used to detect gunshots in cities such as New York and Chicago, however it has a low accuracy issue. In effect, around 50,000 alerts for probable gunshots has been notified with only 9.1% resulting in evidence of a gun-related offense. Also, LoRa is the fastest growing technology that researchers are interested in these days, the benefits of LoRa are long battery life, long distance communication, and low cost of the application. However, LoRa is not the best in outdoors because there are chances of having packet loss using LoRa due to various environmental factors.

## Novelty

This program presents a new approach to the projectile mark detecting system. The proposed system shows high accuracy without any environmental constraints by using LoRa, Computer Vision and sound detection. Similarly to Shotmarker, this system uses LoRa networks to facilitate at a long-range. However, transmitting large data using LoRa, takes a while due to low power. Therefore, instead of transmitting an image or video, this system transmits coordinates. Also, unlike ShotSpotter, the proposed module starts only when a gun shot sound is detected; this method is also cost-effective. Therefore, the gunshot detection system that derives high accuracy is developed by this program. In this program, the proposed system applies the handshaking algorithm to ensure that transferring data is successful. Additionally, this algorithm is beneficial when LoRa network transfers large data such as images or videos.

## Project Overview

<img align="center" width="800" alt="도식화" src="https://user-images.githubusercontent.com/77319785/196273713-43df42f2-068c-4285-ab9c-fec79f087b1b.png">

## ~Environment Settings~ -> Technologies used

| Division        | Stack                                                                                                                                                                                                                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client          | <img src="https://img.shields.io/badge/React-blue?style=for-the-badge&logo=React&logoColor=61DAFB">                                                                                                                                                                                                                               |
| Server          | <img src="https://img.shields.io/badge/NodeJs-green?style=for-the-badge&logo=Node.js&logoColor=339933"/> <img src="https://img.shields.io/badge/Express-grey?style=for-the-badge&logo=Express&logoColor=000000"/> <img src="https://img.shields.io/badge/TypeScript-black?style=for-the-badge&logo=TypeScript&logoColor=3178C6"/> |
| Code Management | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=black"/> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"/>                                                                                                                         |
| Formatting      | <img src="https://img.shields.io/badge/prettier-F7B93E?style=for-the-badge&logo=prettier&logoColor=black"> <img src="https://img.shields.io/badge/ESLint-purple?style=for-the-badge&logo=ESLint&logoColor=4B32C3">                                                                                                                |
| Computer Vison  | <img src="https://img.shields.io/badge/OpenCV-purple?style=for-the-badge&logo=OpenCV&logoColor=5C3EE8"/> <img src="https://img.shields.io/badge/Python-skyblue?style=for-the-badge&logo=Python&logoColor=3776AB"/>                                                                                                                |
| IoT             | <img src="https://img.shields.io/badge/Raspberry Pi-red?style=for-the-badge&logo=Raspberry Pi&logoColor=A22846">                                                                                                                                                                                                                  |
| Deep Learning   | <img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=Python&logoColor=3776AB"/> <img src="https://img.shields.io/badge/Pytorch-Gray?style=for-the-badge&logo=Pytorch&logoColor=EE4C2C"/>                                                                                                                   |

## Environment

### Raspberry pi 1 (For camera)

- This Raspberry pi is placed near by target.

- Raspberry pi model : Raspberry pi 4B 8G RAM

- LoRa Hat : Waveshare SX1262 915M LoRa HAT(915M model is for USA)

- Camera : Raspberry pi HQ Camera

- OS : Raspberry pi OS 64bit(Raspbian)

- Language : Python(3.9.2)

- **Before you read, you should make a directory for setting and all cloned files/directories must be in that directory.**

**Camera Setting**

1. put camera into Raspberry pi
2. After turn on Raspberry pi, Menu -> Preferences -> Raspberry pi configuration -> Interfaces -> select `Camera : Enable`

**LoRa Hat Setting**

1. Set the LoRa mode using jumpers

- Using the Yellow jumpers on photo, place the jumper like photo.
  <img width="474" alt="LoRa hat" src="https://user-images.githubusercontent.com/27190776/208315417-e3962ef9-8917-48e3-ab4b-d9282e87832e.png">

2. Enable Serial port

- In terminal, run command `sudo raspi-config` -> Interfacing Options -> Serial -> No -> Yes

**LoRa Setting**

1. Install Python version 3.9.2

2. clone the LoRa(pi1) code from Github.

```linux
git clone https://github.com/Purdue-K-SW-Capstone/SharpShooter-pi1
```

3. change working directory

```
cd SharpShooter-pi1
```

4. Install python dependencies

```
pip install -r requirements.txt
```

5. Run

```
python main.py
```

---

### Raspberry pi 2 (For sound sensor)

- This Raspberry pi is placed near by shooter.

- Raspberry pi model : Raspberry pi 4B 8G RAM

- LoRa Hat : Waveshare SX1262 915M LoRa HAT(915M model is for USA)

- Microphone : HP-DK40(SIZHENG)

- OS : Raspberry pi OS 64bit(Raspbian)

- Language : Python(3.7.15), Node.js(16.17.1)

- **Before you read, you should make a directory for setting and all cloned files/directories must be in that directory.**

- \*\*Every setting must be run in separate terminal window

**Microphone setting**

- just put microphone into Raspberry pi

**Access Point(Wifi generator) Setting**

**1. Setting up Network Manager for Wi-Fi Access Point**

1. Set up a Raspberry Pi if you don't have one already. See our guide on how to set up a Raspberry Pi.

2. Connect your Raspberry Pi to an Ethernet connection. Our Pi will become a wireless access point, but our connection to a router will be via Ethernet. This provides the strongest connection and ensures the highest speed possible.

3. Open a terminal window on the Pi or an SSH connection to the Raspberry Pi.

4. Make sure your Raspberry Pi is up to date, by running the latest update commands. This isn’t strictly necessary, as the latest Raspberry Pi OS release will already be fairly up-to-date. Consider this a best practice.

```
sudo apt update
sudo apt upgrade -y
```

5. Use raspi-config to edit the configuration of your Raspberry Pi. The network manager option is currently only available via raspi-config, and not via the GUI editor.

```
sudo raspi-config
```

6. Using the cursor keys, navigate to Advanced Options and press Enter.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/GVR6DX7eQeh5eby6dj4Vy5-1200-80.jpg.webp">

7. Navigate to Network Config and press Enter.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/DsBsXcUXtoUEpWCx5b7J56-1200-80.jpg.webp">

8. Select Network Manager and then click OK.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/hTZV2XxHochik27RnQXc86-1200-80.jpg.webp">

9. Click on OK.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/kmVfBpJLWDtJku93JqY7C6-1200-80.jpg.webp">
10. Click Finish.
    <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/pqtWzdNBv4FeBmfAU3BMG6-1200-80.jpg.webp">
11. Select Yes to reboot.
    <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/btor3BHwrmisYDsBd92HL6-1200-80.jpg.webp">

**2. Setting up the Access Point on Raspberry Pi**

- Our access point will provide Wi-Fi access using the Raspberry Pi’s onboard Wi-Fi chip. In this section, we will set up the name and security for the access point. Note that our Raspberry Pi will need to be connected to our home Internet connection via Ethernet. This provides us with the best possible connection.

1. Left click on the Network icon, select Advanced Options and then Create Wireless Hotspot.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/EdeeuPECto6TZHj9ATApb6-1200-80.jpg.webp">

2. Set the Network name of the access point, Wi-Fi security to WPA2, and then set the password for the AP. Click create to save.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/cuJ8FqaqSRV9v6zG9E8Vg6-1200-80.jpg.webp">

3. Reboot the Raspberry Pi.

4. Click on the Network icon to check that the access point is active.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/xTThJDpeqbd32X84n4x7k6-1200-80.jpg.webp">

**3. Setting the Raspberry Pi Access Point to start on boot**

- We want to turn this project into an appliance, a device that will power up and just work. For that we need to tweak the access point settings so that it starts when our Raspberry Pi powers up. Luckily this only takes a few steps.

1. Click on the Network icon and click on Advanced Options >> Edit Connections. This will enable us to make changes to the access point configuration.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/BN2RCDzDumLdCXBG7vzjk5-1200-80.png.webp">

2. Select the wireless access point name, and click on the settings cog to make changes.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/5Qn7YCn3P8cNoNVM6ZpKq5-1200-80.jpg.webp">

3. Under the General tab, check the “Connect automatically with priority” box and set the priority to 0. Click save to make the change. This will set our access point to start whenever the Pi starts.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/T3GLG5WB3BMTfe4fmDL9u5-1200-80.jpg.webp">

**4. Connecting to the Raspberry Pi Access Point**
The access point works just like any other Wi-Fi router / access point.

1. Connect your computer / mobile device to the new access point. It will appear under the name that we have given it.

2. Alternatively on the Raspberry Pi click on the Network icon, and select Advanced Options >> Connection Information.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/RUfoBoKJFshDLabmQfCwP6-1200-80.png.webp">

3. Using a compatible device, scan the QR code to automatically connect to the access point. The information dialog contains all of the information necessary for our access point.
   <img align="center" width="500" src="https://cdn.mos.cms.futurecdn.net/JGmzGHUJWDRaUBUy3kf5U6-1200-80.jpg.webp">

- **Client IP Address setting (necessary)**
  - Go to SharpShooter-Front/src/components/InfoModal.jsx line 16 and SharpShooter-Front/src/components/StorageModal.jsx line 9 and SharpShooter-Front/src/pages/TargetPage.jsx line 236 replace the code with IPv4 IP address shown in the picture (your access point) above instead of localhost.

```
ex)
  const client = new W3CWebSocket(`ws://localhost:3030`);
  ->
  const client = new W3CWebSocket(`ws://10.42.0.1:3030`);

  ws.current = new WebSocket(`ws://localhost:3030`);
  ->
  ws.current = new WebSocket(`ws://10.42.0.1:3030`);

```

SharpShooter-Front/src/components/InfoModal.jsx

- **LoRa Hat Setting**

1. Set the LoRa mode using jumpers

- Using the Yellow jumpers on photo, place the jumper like photo.
  <img width="474" alt="LoRa hat" src="https://user-images.githubusercontent.com/27190776/208315417-e3962ef9-8917-48e3-ab4b-d9282e87832e.png">

2. Enable Serial port

- In terminal, run command `sudo raspi-config` -> Interfacing Options -> Serial -> No -> Yes

**Server setting**

- Server is made with node.js.
- In server, There are many secret keys. so we creat `.env`file and push that into github repository
- `.env`file must be placed on root directory(SharpShooter-Server directory)

1. Install node.js version 16.17.1

2. clone the server code from Github

```
git clone https://github.com/Purdue-K-SW-Capstone/SharpShooter-Server
```

3. change working directory

```
cd SharpShooter-Server
```

4. Install node.js dependencies

```
npm install
```

5. Run

```
npm start
```

**LoRa Setting**

- Before setting this, You must finish Server setting first.

1. Install python version 3.7.15

2. clone the LoRa(pi2) code from Github

```
git clone https://github.com/Purdue-K-SW-Capstone/SharpShooter-pi2
```

3. change working directory

```
cd SharpShooter-pi2
```

4. Install python dependencies

```
pip install -r requirements.txt
```

5. Run

```
python main.py
```

**Client server setting**

- Client server is made with react.
- Before setting this, You must finish Server setting first.

1. Install node.js version 16.17.1

2. clone the front code from Github

```
git clone https://github.com/Purdue-K-SW-Capstone/SharpShooter-Front
```

3. change working directory

```
cd SharpShooter-Front
```

4. Install node.js dependencies

```
npm install
```

5. Run

```
npm start
```
