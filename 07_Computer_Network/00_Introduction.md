# Computre Networks

- A set of nodes connected be communication links.
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

# Properties of CN
1. Fault Tolerance: Ability of network to work regardless of failures. ie, if a failure occurs in a path the network has to find another path to get the information through.
2. Scalability: Ability of netowork to grow based on needs, and still retain its performance
3. QoS: Quality of Service refers to ability to set priorities and manage traffic.
4. Security
   
# 1. TYPES OF COMPUTER NETWORK
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

# Network Topology
Arrangement of nodes in a network.
 - Physical Topology: Placement of nodes
 - Logical Topology: Deals with data flow in network

The various topologies are:
 1. Bus: All data is transmitted over a common medium
    - Bidirectional data flow.  
    - Less expensive
    - For temperory purposes only
    - No security
    - Node failure is fine, but medium failure is not. So not fault tolerant(only one path)
    - Limited cable length
 2. Ring: Bus in a closed loop
    - peer to peer
    - Unidirectional
    - Connection to neighbouring nodes only
    - Transmission happens with the help of a token
    - Node failure can affect whole network
    - No security
    - As load increases, performance decreases
 3. Star: Every node is connected to each other with a central node, which generally is a hub or a switch
    - 

# Communication
Transfer of data between two nodes
Three types of data flow:
1. Simplex: Unidirectional. Eg: Keyboard, mouse
2. Half duplex: Both directions, but not at the same time. Eg: Walkie-talkies
3. Duplex/ Full duplex: Both directions simultaneously. Eg: Telephone


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

![Alt text](<Screenshot from 2023-11-19 11-33-34.png>)


## Peer to peer network
- No centralised administration
- All peers are equal 
- Simple sharing
- Not scalable

## Client Server network
- Centralised administraton
- Request-response model
- Scalable
- Server can be overloaded - too dependent on the server