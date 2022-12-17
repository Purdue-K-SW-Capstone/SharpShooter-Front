# Team: SharpShooter

## Title

Outdoor Long Range Low Latency Shot Tracking System Using LoRa and Computer Vision

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

## Environment Settings

| Division        | Stack                                                                                                                                                                                                                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client          | <img src="https://img.shields.io/badge/React-blue?style=for-the-badge&logo=React&logoColor=61DAFB">                                                                                                                                                                                                                               |
| Server          | <img src="https://img.shields.io/badge/NodeJs-green?style=for-the-badge&logo=Node.js&logoColor=339933"/> <img src="https://img.shields.io/badge/Express-grey?style=for-the-badge&logo=Express&logoColor=000000"/> <img src="https://img.shields.io/badge/TypeScript-black?style=for-the-badge&logo=TypeScript&logoColor=3178C6"/> |
| Code Management | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=black"/> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"/>                                                                                                                         |
| Formatting      | <img src="https://img.shields.io/badge/prettier-F7B93E?style=for-the-badge&logo=prettier&logoColor=black"> <img src="https://img.shields.io/badge/ESLint-purple?style=for-the-badge&logo=ESLint&logoColor=4B32C3">                                                                                                                |
| Computer Vison  | <img src="https://img.shields.io/badge/OpenCV-purple?style=for-the-badge&logo=OpenCV&logoColor=5C3EE8"/> <img src="https://img.shields.io/badge/Python-skyblue?style=for-the-badge&logo=Python&logoColor=3776AB"/>                                                                                                                |
| IoT             | <img src="https://img.shields.io/badge/Raspberry Pi-red?style=for-the-badge&logo=Raspberry Pi&logoColor=A22846">                                                                                                                                                                                                                  |
| Deep Learning   | <img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=Python&logoColor=3776AB"/> <img src="https://img.shields.io/badge/Pytorch-Gray?style=for-the-badge&logo=Pytorch&logoColor=EE4C2C"/>                                                                                                                   |
