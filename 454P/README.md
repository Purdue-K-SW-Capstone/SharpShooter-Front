# Evaluating LoRaWAN performance in intentional and unintentional DoS attacks by legacy 900MHz network devices
## 🧾 Project Overview
Due to the growth of AI and network technology that complement the Internet of Things(IoT), the IoT market is gradually growing, and the supply of IoT devices is expanding. Compared to other network technologies used in IoT, such as Wi-Fi, Bluetooth, and NB-IoT, LoRa provides benefits which are low-power and long-distance data transmission with long-lasting batteries.

While investigating prior studies, security issues and vulnerabilities in LoRaWAN were found. However, the easiest and most effective attack method is jamming. Jamming is a technology that prevents the operation of specific frequencies by disrupting radio waves. Since LoRa is based on the Chirp Spread Spectrum(CSS) and operates in the predetermined frequency band, attackers are able to exploit the chirp frequency to make LoRa more vulnerable to wideband jamming attacks.

For these reasons, the goal of 454P is to evaluate the performance of LoRaWAN by conducting intentional and unintentional Denial of Service(DoS) attacks with legacy 900MHz network devices.

The experiments are divided into indoor and outdoor to simulate real-world industrial sites. The experiment result demonstrates the potential risk to the security of LoRaWAN against jamming attacks.

---
## 💣 Problem Statement
Jamming is a fundamental problem of wireless networks that have been researched in various radio technologies. As LoRaWAN in the United States uses a predetermined US915 band, anyone including attackers is available to transmit data in this frequency band without permission. Additionally, LoRa is based on CSS, which makes LoRaWAN more vulnerable to jamming attacks. A jammer is able to sweep the same chirp frequency at the same speed, which makes data communication fail if the jammer finds the tuning slope of the chirp frequency. Even though narrowband jamming can be prevented since the jammer affects the chirp receiver for a short period, it is still vulnerable to wideband jamming.

This weakness results in human and property damage since several data in high-risk industries transmitted over LoRaWAN are susceptible to information loss. For example, LoRaWAN applied in the medical area needs to monitor patients continuously who require real-time and always-on systems that are dangerous if packet loss occurs. In addition, agricultural production will suffer if farmers receive inaccurate soil and water data information.

---
## 💡 Novelty
This research aims to assess the network performance of LoRaWAN according to jamming by conducting indoor and outdoor experiments.

The indoor experiment was conducted in a complex building to simulate the medical field where the LoRa end devices are applied. The outdoor experiment was conducted on the farm to simulate the environment in agriculture.

There are several prior studies measuring the performance of LoRaWAN in urban environments or tree farms which have a lot of obstacles. However, few studies have analyzed how jamming affects performance in real-world industrial sites. Therefore, this research concentrates on evaluating the network performance of LoRaWAN according to intentional and unintentional Denial of Service(DoS) attacks by conducting experiments.

---
## ⚙ Method

Two experiments are designed to prove the vulnerability of LoRaWAN applied in the industries to jamming attacks, whether intentional or unintentional. The definition of intentional and unintentional attacks is defined for experiments. Intentional attack is defined as one pair of jammers sending a signal toward the gateway next to each other. Unintentional attack is defined as one pair of jammers sending a signal to each other without a purpose that affects the gateway.

### Indoor Experiment

The indoor experiment aims to prove the possibility of damage in medical facilities induced by the jamming attack. The indoor experiment was conducted by dividing whether the end nodes were placed on the same floor and whether the attack was intentional.

### Outdoor Experiment

The outdoor experiment aims to demonstrate whether a LoRaWAN gateway for outdoor IoT commercial deployment is interrupted by unintentional jamming attacks.

---
## Implementation

### Indoor Experiment

The indoor experiment is divided into Close-in attack, Intentional attack, and Unintentional attack. Close-in attack showed perfect performance that any single packet was not received. Intentional attack proved that the far from a jammer to a gateway, the bigger JE happens. If end nodes were placed on different floors, JE was bigger than the experiment with the same floor. During unintentional attack, jamming was successfully conducted. This means that jamming is more effective if the distance between jammers is far enough.

### Outdoor Experiment

The outdoor experiment was conducted on the farm. End nodes were fixed at 100m, 200m, and 500m from the gateway. Jammers were located on 10m, 50m, and 100m from the gateway. The experiment checked Jamming Effect (JE) using the average Packet Delivery Rate (PDR). Jamming was more effective than indoor experiments because there were no obstacles. Therefore, jamming in outdoor environment, on the farm, was effective.

---
## Conclusion
This research aims to evaluate the performance of LoRaWAN against jamming attacks and to inform the security vulnerability in the physical layer of LoRaWAN, with both intentional and unintentional attacks.

These experiments verify the existence of jamming threats by legacy 900MHz network devices, even in unintended situations.

These experiments were conducted on indoor and outdoor environments that reflect the real environment of the medical and agricultural industries, like hospitals and farms that employ LoRaWAN.

In addition, the metrics are suggested for more accurate performance evaluation, which indicates the effect of jamming under wireless networks that diverge packets through RF signals without a destination.

Experiment results show high JE, which suggests that the security vulnerability of LoRaWAN needs to be reconsidered.

Therefore, this research demonstrates the security vulnerability in LoRaWAN on the physical layer and the countermeasures that should arise for the LoRaWAN.

---
## 🌎 Environment
### LoRaWAN
On [Raspberry Pi OS](https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2022-09-26/)

Using Chirpstack v3
- [Chirpstack v3 gateway bridge@Latest](https://www.chirpstack.io/gateway-bridge/install/debian/)
    - Mosquitto @Latest
- [Chirpstack v3 Network Server@Latest](https://www.chirpstack.io/network-server/) & [Chirpstack v3 Application Server@Latest](https://www.chirpstack.io/application-server/)
    - Mosquitto @Latest
    - Redis 5.0.
    - Postgresql 9.5.

### Arduino
[Docker](https://www.docker.com/) is used to compile / upload the code to ESP32

Arduino code is located in 'arduino/volumes/Arduino/ESPCounter'

Dockerfile for compiling the code is located in /arduino

To compile the code, run the following command in /arduino
```bash
docker build -t arduino .
```

To run the docker image
```bash
docker run -it --rm -v $PWD/volumes/Arduino:/Arduino arduino
```
- To stop the container, type in
    ```bash
    exit
    ```
- inside the container

To compile the code, type in
```bash
arduino-cli compile --fqbn esp32:esp32:heltec_wifi_lora_32_V2 --verbose ESPCounter.ino
```
Inside the container, and the code in /volume/Arduino/ESPCounter will be compiled

To upload the code, the [ESP32](https://heltec.org/project/wifi-kit-32/) device must be connected to the computer, and device should be connected with docker

To connect the device with docker, for ubuntu, type in
```bash
docker run -it --rm -v $PWD/volumes/Arduino:/Arduino --device=/dev/ttyUSB0 arduino
```
- Then, inside the container, type in
```bash
arduino-cli upload -p /dev/ttyUSB0 --fqbn esp32:esp32:heltec_wifi_lora_32_V2 --verbose ESPCounter.ino
```
- For the other OS, please refer to [this](https://docs.docker.com/engine/reference/commandline/run/#add-host-device-to-container---device) page

### Jamming Analysis
Jamming analysis is located in 'jammingAnalysis'

Dockerfile and docker compose file for running the code is located in /jammingAnalysis

To run the docker container, run the following command in /jammingAnalysis
```bash
docker compose up
```
- Ctrl+C will stop the container
- To enter Jupyter Notebook, type in
  ```bash
  localhost:10000
  ```
- in your browser, or click the link [localhost:10000](http://localhost:10000/notebooks/jamming_analysis.ipynb)

---
## 👼 Collaborator

       😿 Seokhyeon Bang
       - Chungang University
       - School of Computer Science and Engineering
       - kzrt0123@cau.ac.kr
       - https://github.com/KZRT
       
       🐤 Minju Ro
       - Chungang University
       - School of Computer Science and Engineering
       - romj98@cau.ac.kr
       - https://github.com/ori5r2
      
       🦂 Junyoung Jang
       - Chungang University
       - School of Computer Science and Engineering
       - junjang99@cau.ac.kr
       - https://github.com/Amuguna
       
       🎃 Yuseon Choi
       - Chonnam National University
       - Department of Software Engineering
       - 181133@jnu.ac.kr
       - https://github.com/YuseonChoi
    
       🐺 Doyong Kwon
       - Kyungpook National University
       - School of Computer Science and Engineering
       - doyong365@knu.ac.kr
       - https://github.com/doyong123
    
       🐁 Kangyeon Lee
       - Purdue University
       - Department of Computer and Information Technology
       - lee3245@purdue.edu
       - https://github.com/dkssud2496
