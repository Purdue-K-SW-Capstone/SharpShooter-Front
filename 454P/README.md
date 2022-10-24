# Analysis of LoRaWAN’s packets to demonstrate vulnerability of LoRaWAN
## 🧾 Project Overview
LoRa provides benefits such as low-power and long-distance data transmission with long-lasting batteries. While investigating prior studies, security issues and vulnerabilities in LoRaWAN were found. For example, in the join procedure of LoRa, a random generator may generate the same devNonce even if there is no attack which results in Denial of Service. It has also been found that jamming, replay attack, and bit-flipping attack are possible. The goal of our project is identifying and analyzing vulnerabilities in LoRaWAN within the configured network by trying some attacks such as jamming or sniffing the packet of LoRaWAN. These attacks will be implemented in detail within the local LoRaWAN that simulates the real environment. In the future, further investigations might be conducted to solve these vulnerabilities found in this project.

## 💣 Problem Statement
LoRaWAN networks have several vulnerabilities of security. As LoRaWAN is wireless network system using RF(Radio Frequency) to send data, it has general vulnerabilities same as other wireless networks. Thus, several security vulnerabilities like sniffing, jamming and so on exists on LoRaWAN. To be specific, LoRaWAN has two vulnerabilities that can be hacked.

1. The join request is not encrypted.
When end-nodes want to join the server, end-nodes send a join request to gateway to make authentication of this device. In LoRaWAN, join request is not encrypted. Since, it can be hacked by the other listening device like HackRF.
2. The Nonce is fixed.
Nonce is an arbitrary number that can be used just once in a cryptographic communication. In LoRa, this nonce number is fixed after it is set at first time.

 Since of these vulnerabilities of security, there are six methods to hack LoRaWAN that are generally known.

1. Jamming: making a big noise to interfere sending the data.
2. Replay Attack: repeating the transmission of valid data by intercepting and retransmitting data, resulting in Denial of Service(DoS) attack.
3. ACK spoofing: exploiting the fact that it does not specify which message is confirmed
4. Eavesdropping: repeating reset, attacker can get plaintext
5. Bit-Fipping: changing the context of the packet
6. LoRa class B attack: accelerating battery exhaustion by increasing the power consumption of the sensor.

## 💡 Novelty

This research aims to demonstrate vulnerabilities of LoRaWAN security under an experiment environment similar to the real-world specification.

LoRaWAN network uses multichannel radio frequency for communication, to jam LoRaWAN in the real-world specification, all of the channels should be jammed at once. As previous studies did not provide detailed information about jamming multiple channels at once or used single channels. Thus, this research fills the gap by jamming in multichannel using LoRa versions used in real-world environments with achievable equipment with details.

Also, this research covers details about how to build a local network for hacking LoRaWAN. By describing the specifications about local LoRaWAN, this research provides a flexible environment where multiple hacking methods are able to be attempted with few constraints.

## ⚙ Progress

### Building Local LoRaWAN

- The whole network consists of gateway, gateway bridge, network server, application server, and two Database servers.
- Using Raspberry Pi as a network server and an application server. RAK7249 as a gateway
- Local LoRaWAN was a mandatory because this project aims to hack a LoRaWAN, which might cause legal problems, which might cause a problem once hacking is operated in Layer 2 or higher layers.

### Jamming

#### Jamming using SDR

- Jamming was conducted by Software Defined Radio(SDR). HackRF one and USRP B200 were used as SDR.
- dBm of SDR was not as much powerful as signals sent by a node device. It can not conduct jamming successfully.

#### Jamming using Motorola canopy

- Canopy has two types which are Access Point(AP) and subscriber. It can be connected with external antennas. Subscriber sent tremendous packets to AP.
- The analyzer proved that there was a noise like a waterfall which can offset all signals near 900MHz.
- Additionally, all join requests from node devices in range of 902.8 to 914Hz could not reach to the gateway as a join request did not show up on Chirpstack interface of the application server and network server. This points to Jamming comes to fruition. Since commercial LoRaWAN has more channels, jamming more channels can be done by using more canopy at once, or jamming different frequency of LoRaWAN in multiple region using under type of canopy.

#### Packet Sniffing

- Using GNU radio and HackRF, LoRaWAN packets which are sent by node devices were sniffed by HackRF one. Packets were shown on the laptop which was connected to HackRF.
- When a join request of LoRaWAN is sent, packets are not encrypted. Therefore Packet sniffing of LoRaWAN is successfully conducted using gr-lora and LoRa_Craft.

## 🌎 Environment
### LoRaWAN
On Raspberry Pi OS
([https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2022-09-26/](https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2022-09-26/))

Using Chirpstack v3
- Chirpstack v3 gateway bridge@Latest
([https://www.chirpstack.io/gateway-bridge/install/debian/](https://www.chirpstack.io/gateway-bridge/install/debian/))
    - Mosquitto @Latest
- Chirpstack v3 Network Server@Latest ([https://www.chirpstack.io/network-server/](https://www.chirpstack.io/network-server/)) & Chirpstack v3 Application Server@Latest ([https://www.chirpstack.io/application-server/](https://www.chirpstack.io/application-server/))
    - Mosquitto @Latest
    - Redis 5.0.
    - Postgresql 9.5.

### Gnu Radio & LoRa Packet UDP Reader
On Ubuntu 20.04

- LoRa_Craft
([https://github.com/PentHertz/LoRa_Craft](https://github.com/PentHertz/LoRa_Craft))
    - Python 2.7
        - Scapy
    - Gnu Radio 3.8
    - gr-LoRa 0.6.2
    ([https://github.com/rpp0/gr-lora](https://github.com/rpp0/gr-lora))
        - `python2-numpy`, `python2-scipy`, `swig`, `cppunit`, `fftw`, `gnuradio`, `libvolk`, `log4cpp`, `cmake`, `wx,
        liquid-dsp([https://github.com/jgaeddert/liquid-dsp](https://github.com/jgaeddert/liquid-dsp))`
- Gnu Radio 3.9
    - gr-osmosdr([https://github.com/osmocom/gr-osmosdr](https://github.com/osmocom/gr-osmosdr))
    - hackrf@latest
    - ettus uhd driver(`[https://kb.ettus.com/Building_and_Installing_the_USRP_Open-Source_Toolchain_(UHD_and_GNU_Radio)_on_Linux](https://kb.ettus.com/Building_and_Installing_the_USRP_Open-Source_Toolchain_(UHD_and_GNU_Radio)_on_Linux))`

- Golang 1.13

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
      
       🚽 Junyoung Jang
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
