package main

import (
	"fmt"
	"net"
)

func main() {
	conn, err := net.ListenPacket("udp", ":30000") // Opens UDP Port
	fmt.Println("Listening on %s", conn.LocalAddr())
	if err != nil {
		fmt.Println(err)
	}
	defer func(conn net.PacketConn) { // Close port when exit (Ctrl+c)
		err := conn.Close()
		if err != nil {
			fmt.Println(err)
		}
	}(conn)
	for {
		buf := make([]byte, 65535)
		_, _, err := conn.ReadFrom(buf) // Always listen to the port, discard any buffers
		print("Packet Received")
		if err != nil {
			fmt.Println(err)
			continue
		}
	}
}
