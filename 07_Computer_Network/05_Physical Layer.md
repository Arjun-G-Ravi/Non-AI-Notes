# THE PHYSICAL LAYER
This is the layer which actually transfers the data between devices. It takes in the data from the data link layer and convert it into binary data that can be transported.

# Physical Network Topology
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
    - Centralised management
    - All traffic pass though the central node
    - Easy to design and implement
    - Scalable
    - Failure/ Overloading in central node can be fatal
    - High cost for hub/ switch
 4. Mesh topology: All nodes connected to each other
    - Fault tolerant and reliable
    - Expensive, and impractical for large networks
    - Issues with broadcast messages
    - Least traffic
 5. Hybrid Topology: Mixing multiple topologies as per need
    - Probably the best

# Data Flow 
Transfer of data between two nodes
Three types of data flow:
1. Simplex: Unidirectional. Eg: Keyboard, mouse
2. Half duplex: Both directions, but not at the same time. Eg: Walkie-talkies
3. Duplex/ Full duplex: Both directions simultaneously. Eg: Telephone

# Network Types - by Connection

#### Peer to peer network
- No centralised administration
- All peers are equal 
- Simple sharing
- Not scalable

#### Client Server network
- Centralised administraton
- Request-response model
- Scalable
- Server can be overloaded - too dependent on the server