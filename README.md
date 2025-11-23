---------------- Router-----------------
Connecting to device...
Connection established.

---------------- Router running-config -----------------
Building configuration...

Current configuration : 3292 bytes
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
hostname Router
!
interface GigabitEthernet0/0
 ip address 192.168.181.20 255.255.255.0
 duplex auto
 speed auto
!
interface GigabitEthernet0/1
 no ip address
 shutdown
!
ip route 0.0.0.0 0.0.0.0 192.168.181.1
!
line vty 0 4
 login local
 transport input ssh
!
end

---------------- Router interfaces -----------------
GigabitEthernet0/0 is up, line protocol is up
  Hardware is iGbE, address is 00a1.b2c3.d4e5
  Internet address is 192.168.181.20/24
  MTU 1500 bytes
  Full-duplex, 1000Mb/s

GigabitEthernet0/1 is administratively down, line protocol is down
  Hardware is iGbE, address is 00a1.b2c3.d4e6
  MTU 1500 bytes

Loopback0 is up, line protocol is up
  Internet address is 10.10.10.1/32

---------------- Switch -----------------
Connecting to device...
Connection established.

---------------- Switch running-config -----------------
Building configuration...

Current configuration : 2478 bytes
!
version 15.0
hostname Switch
!
interface Vlan1
 ip address 192.168.181.30 255.255.255.0
 no shutdown
!
interface FastEthernet0/1
 switchport mode access
!
interface FastEthernet0/2
 switchport mode access
!
vlan 1
 name default
!
vlan 10
 name Users
!
vlan 20
 name Servers
!
end

---------------- Switch interfaces ----------------
FastEthernet0/1 is up, line protocol is up
  Hardware is Fast Ethernet
  MTU 1500 bytes
  Full-duplex, 100Mb/s
  MAC address 00a1.b2c3.d400

FastEthernet0/2 is down, line protocol is down
  Hardware is Fast Ethernet
  MTU 1500 bytes
  MAC address 00a1.b2c3.d401

Vlan1 is up, line protocol is up
  Internet address is 192.168.181.30/24

---------------- Switch vlan ----------------
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2
10   Users                            active
20   Servers                          active
4    vlan4                            active

Switch(config)#no vlan 4
Switch(config)#end
Switch#

---------------- Switch vlan ----------------
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2
10   Users                            active
20   Servers                          active

Configuring VLAN...
Entering configuration commands:
vlan 4
 name vlan4
 ip 192.168.144.2 255.255.255.0
end

---------------- Switch vlan ----------------
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2
4    vlan4                            active
10   Users                            active
20   Servers                          active

---------------- Switch ARP -----------------
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.181.1        2      00a1.b2c3.d4f1  ARPA   Vlan1
Internet  192.168.181.20       0      00a1.b2c3.d4e5  ARPA   Vlan1
Internet  192.168.181.30       -      00a1.b2c3.d400  ARPA   Vlan1

---------------- Switch mac address-table -----------------
          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
1       00a1.b2c3.d4e5    DYNAMIC     Fa0/1
1       00a1.b2c3.d4f1    DYNAMIC     Fa0/1
4       00a1.b2c3.d410    STATIC      Vlan4
10      00a1.b2c3.d420    DYNAMIC     Fa0/2
20      00a1.b2c3.d430    DYNAMIC     Fa0/1
