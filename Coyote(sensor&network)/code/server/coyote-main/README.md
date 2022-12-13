# Node.js server for coyote one

## installation

- install docker desktop
- clone this repository
- docker build . -t <your username>/coyote-main
- docker run -p 8081:8081 -p 3333:3333 -d <your username>/coyote-main

server is running on your localhost.

POST http://localhost:8081/api/sensors/getSound1Coord : get the coordinate information of sound 1 sensor
  
POST http://localhost:8081/api/sensors/getSound2Coord : get the coordinate information of sound 2 sensor
  
POST http://localhost:8081/api/sensors/getSound3Coord : get the coordinate information of sound 3 sensor
  
POST http://localhost:8081/api/coyotes/getInitialCoyotes : get the coordinate information of last 5 detected coyotes

websocket connection

ws://127.0.0.1:3333
