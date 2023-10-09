# Computer Network
A network can be defined as a group of computers and other devices connected in some way so as to be able to exchange data.Each of the devices on the network can be thought of as a node, each node has a unique address.

# 1. Types of CN
1. PAN - Personal Area Network
   - one person in a building
   - Eg: Wireless keyboard, printers, etc.
2. LAN - Local Area Network
   - Privately owned network in a building
   - To share resources and exchange information
   - Also called enterprise networks
   - Wired LAN - Ethernet
   - Wireless LAN - WiFi
3. MAN - Metropolitian Area Network
   - Spans an entire geographical area (like a city)
   - Eg: Cable TV
4. WAN - Wide Area Network
   - Even larger geographical area (like a country or a continent)
5. Internetworks
   - A collection of interconnected networks is called an internetwork or internet.

# Some Terms
1. VPN: Extends private network across public network to provide improved security and anonymity.
2. Internet Service Provider(ISP): Organisation that provide services for using the internet. 

# 2. NETWORK SOFTWARE
 - Protocol hierarchies
 - Interface & Service
 - Service Primitives
 - Design issues for the layers

# Network protocols 
Network protocols are a set of rules and conventions that define how data is transmitted and received over a computer network.

To reduce their design complexity, most networks are organized as a stack of layers or levels, each one built upon the one below it. The number of layers, the name of each layer, the contents of each layer, and the function of each layer differ from network to network. The purpose of each layer is to offer certain services to the higher layers, shielding those layers from the details of how the offered services are actually implemented. 
Each layer passes data and control information to the layer immediately below it, until the lowest layer is reached. Actual communication occurs when the information passes layer-1 and reaches the Physical medium.

<!-- Protocol img -->

Between each pair of adjacent layers is an **interface**. The interface defines which  primitive operations and services the lower  layer makes available to the upper one.
A set of layers and protocols is	called a **network architecture**. A list of the protocols used by a certain system, one protocol per layer, is called a **protocol stack**.

# Service Primitives

**Service:** In network communication, a service defines the interface between two layers, where the lower layer acts as the service provider, and the upper layer acts as the service user. The service specifies what operations the lower layer is ready to perform on behalf of its users but doesn't detail how these operations are implemented. Services abstract the functionality offered by one layer to the layer above it.

**Service Primitives:** Service primitives are a set of high-level communication operations or functions provided by a network service to its users. These primitives serve as a standardized way for users to request and interact with network services. Common service primitives include: 
It includes Listen, Accept, Connect, Disconnect, Send, Recieve.

# Network reference models
Network reference models are conceptual frameworks used to standardize and describe the functions and interactions of various networking components and protocols within a computer network.
Eg: OSI Reference Model, TCP/IP Reference Model 

Pg 58