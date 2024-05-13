# Computer Networks
- A set of nodes(computers) connected by communication links.
- A network can be defined as a group of computers and other devices connected in some way so as to be able to exchange data. Each of the devices on the network can be thought of as a node, each node has a unique address.
- A computer network has three components:
    - Nodes
        - End nodes: Computers, printer, etc
        - Intermediate nodes: Switches, bridges
    - Transmission media
        - Wired/ Guided
            - Ethernet: Data transferred as electrical signals
            - Fibre optics: As light waves, fastest
            - Coaxial: For video and audio. As electricity
            - USB cable: Universal serial bus. 
        - Wireless/ Unguided
            - IR: Short
            - Radio: Bluetooth, Wifi
            - Microwaves: Cell phone. Longer
            - Sattelite communication
    - Services
        - Instant messaging, file sharing, Information and web services, entertainment, etc. 

![Alt text](<Screenshot from 2023-11-19 11-33-34.png>)

# Properties of CN
1. Fault Tolerance: Ability of network to work regardless of failures. ie, if a failure occurs in a path the network has to find another path to get the information through.
2. Scalability: Ability of netowork to grow based on needs, and still retain its performance
2. QoS: Quality of Service refers to ability to set priorities and manage traffic.
3. Security and privacy
  
# Types of Networks
1. PAN - Personal Area Network
   - one person in a building
   - Eg: Wireless keyboard, printers, etc.
2. LAN - Local Area Network
   - Privately owned network in a building
   - To share resources and exchange information
   - Also called enterprise networks
   - Comes as:
     - Wired LAN - Ethernet
     - Wireless LAN - WiFi
3. MAN - Metropolitian Area Network
   - Spans an entire geographical area (like a city)
   - Used to connect LANs
   - Eg: Cable TV
4. WAN - Wide Area Network
   - Even larger geographical area (like a country or a continent)
5. Internetworks
   - A collection of interconnected networks is called an internetwork or internet.

# Network protocols
They are a set of rules that define how the communication between two nodes takes place.
It determines:
 - Message encoding
 - Formatting and encapsulation(of source, destination information)
 - Message delivery option
   - Unicast: Sender sends to exactly one reciever
   - Bicast: More than one reciever, but not all
   - Broadcast: To all revievers.
 - Timing
 - Size, etc.
Eg: TCP, IP, HTTP, HTTPS, SSH, DNS etc.

### SSH
SSH, or Secure Shell, is a network protocol that provides a secure way to access and manage a remote computer or server over an unsecured network. It is widely used for secure remote administration, file transfer, and tunneling of network services.

### HTTP
HTTP, or Hypertext Transfer Protocol, is a fundamental protocol used for communication on the World Wide Web. It is an application layer protocol that facilitates the transfer of information between clients (typically web browsers) and servers. HTTP is the foundation of any data exchange on the web and is often associated with the transfer of hypertext documents, which include resources like HTML files, images, and multimedia content.

### HTTPS
HTTPS, or Hypertext Transfer Protocol Secure, is an extension of HTTP (Hypertext Transfer Protocol) designed to provide secure communication over a computer network, typically the internet. The primary goal of HTTPS is to ensure the confidentiality and integrity of data exchanged between a user's web browser and a website's server. It achieves this through the use of encryption and other security measures.