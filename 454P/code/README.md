## Codes
### Arduino
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

To upload the code, the device must be connected to the computer, and device should be connected with docker

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