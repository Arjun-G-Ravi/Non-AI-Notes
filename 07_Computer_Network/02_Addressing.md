# IP Address
 - The internet protocol address is used to identify every node in a computer network
 - It is a logical address - an abstract address, that doesn't depend on the node devices.
 - It is not even dependent on the physical location of the devices. But the physical location can be approximated using the IP address.
 - Router assigns an ip address to every device that connects to it, creating a LAN
 - An IPv4 address is represented as decimals, as 4 octets. Each octet is a number between 0 and 255.
 - It is of the form 192.168.1.12, where the first 3 octets refer to the network address and last one is host address 
 - Can be assigned manually

# MAC address
 - Media Access Control address is used to identify each node in a network (just like IP address)
 - It is permanent, and cannot be changed as they are physical/ hardware address
 - Unique for any other devices. Assigned by the manufacturer
 - Represented as hexadecimals, separated by hyphen, period or colon. Eg: 70-20-84-00-ED-FC 

Routers need IP address and switches need MAC address to transfer data.
# Port Address
- Decides which process has to get the communicated data in the particular node
- Port is the communication endpoint.

Thus for proper communication between nodes in a network, we need to attach these three addresses of both the reciever and the sender along with the data to be communicated. 

# Switching 
- Helps deciding the best route for data transmission in a computer network
- Switching Techniques:
  - Circuit Switching: A dedicated path will be established first before data transfer
  - Message Switching: Each node will wait till the whole data is recieved. Then it will pass it to the next node. This happens till the reciever is reached. But this can't be used for real time applications.
  - Packet Switching: Message is broken into packets and send individually. It will also have sequence number. Acknowledgement is also send by the reciever, if any particular particle failed to reach the destination.
      - Datagram approach: No fixed path for communication
      - Virtual circuit approach: A fixed path for communication