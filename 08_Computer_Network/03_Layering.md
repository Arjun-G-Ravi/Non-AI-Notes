# Layering
Layering in computer networks involves organizing communication protocols into a series of abstraction layers. Each layer has a specific function and interacts with the layers above and below it. The layers are designed to be modular, allowing for easier development, maintenance, and interoperability of network protocols.

A set of layers and protocols is	called a **network architecture**. A list of the protocols used by a certain system, one protocol per layer, is called a **protocol stack**.

**Interface**: An interface in network software defines how different layers or components communicate with each other. It specifies the rules and protocols for interaction between entities in adjacent layers. 

**Service:** In network communication, a service defines the interface between two layers, where the lower layer acts as the service provider, and the upper layer acts as the service user. The service specifies what operations the lower layer is ready to perform on behalf of its users but doesn't detail how these operations are implemented. Services abstract the functionality offered by one layer to the layer above it.

# Layer Architectures
1. OSI Reference model
2. TCP/IP model

# OSI Reference model
- Open System Interconnection
- Not a protocol - just a guideline for a flexible, robust network architecture. Hence called reference model
- Intended to show a way to faciliate communication without changing the underlying logic in hardware. 
- Never fully implemented. It is used for education and testing though.
- Very modular, and easy to troubleshoot
- 7 Layers of OSI model: `All People Should Try New Dominos Pizza`.

![Alt text](OSI-7-layers.jpg)
- The communication between two hosts, using the osi model is shown
![Alt text](<Interaction between layers in the OSI Model.JPG>)
- The intermediate nodes will conly have access to the phy, data link and network layer information.

## Functions of Layers in OSI model

![Alt text](<Screenshot from 2023-11-23 08-09-45.png>)

**Principles applied to create the seven layers are**
![Alt text](image.png)

#### Layer 7: Application Layer:
   - Provides an interface between application and user. This might be a https request to a server.
   - It generates the data. This is where the user gives in the 'to-network' data
   - In TCP/IP model, the application layer contains the presentation and session layer also

#### Layer 6: Presentation Layer:
   - Encrypt and Compress
   - Data formatting and translation

#### Layer 5: Session Layer:
   - Establishes, maintains and synchronises interation btw communicating devices 

#### Layer 4: Transport Layer:
   - Responsible for transporting the messages. There are two ways
       - TCP: Reliable
       - UDP: Fast
   - It does:
       - Port adressing (Port Adress)
       - Segmentaion and reassembly
       - Connectio and flow control
       - Error control
   - A layer4 header (containing port address) is added to the incoming data packet, and is passed down
   

#### Layer 3: Network Layer:
   - The layer 3 address is added to the incoming data
   - This is the IP address of the sender and reciever IP address.
   - This new message is called packets

#### Layer 2: Data Link Layer:
   - The source and destination MAC address is appended to the incoming message. This is now called frames.
   - Responsible for moving data(frames) from one layer to another
   - Framing
   - Physical adressing (MAC)
   - Flow, Access and error control

#### Layer 1: Physical Layer:
   - Responsible for physically transmitting the data from data link layer through any medium. 
   - It looks at the MAC address from the message, and compares it to the port address in a lookup table it has, and sends the message.
   - Data rate, Representation and sync of bits
   - Physical topology


# TCP/IP model

- Transmission Control Protocol/ Internet Protocol
- This model is used for networking all over the world, and OSI model is used just as reference
- 4 layers in the TCP/IP model: Network Access Layer, Network/ Internet layer, Transport layer and Application layer.

![Alt text](image-6.png)

- Sometimes, it is split into 5 layers by splitting Network access layer into phy and data link layer 
- The layers work just like the OSI model, but the application layer in TCP/IP model does the work of Application, Presentation and Session layers.

`Even though TCP/IP model is used everywhere, the OSI model is used for naming conventions and all. Thus the application layer for both models is called Layer 7.`

## PDU
![Alt text](<Screenshot from 2023-11-23 12-23-53.png>) 