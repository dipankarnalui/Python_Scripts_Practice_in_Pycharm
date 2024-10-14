#L2(VLAN, ARP) and L3(OSPF, BGP) Protocol Testing, Routing, Switching, TCP, ARP, Ethernet    
'''
1.	H1----S1----R1----S2---H2

1a.Configure IP address on devices where it is mandatory?

	H1: Private 10.10.1.2/24  MAC: AA - Class A:  
	R1: Private 10.10.1.1/24 Public 74.34.56.2
	H2: Private 10.10.1.3/24 MAC: CC

	Ping 10.10.1.3 
	ICMP Echo 
	H1 - S1 (table) 10.10.1.3  

2.ARP process ? Explain from topology in question 1? 

	IP -> MAC 
	Netstat -nr
	IP MAC 

3.Ethernet Header format for ARP?


	SRC: 10.10.1.2
	DST: 10.10.1.3
	CHECKSUM: 
	Flags:
	Size:
	Frame: 
	PDU: 

	IPv4 - IP
	TCP - Port 

4.TCP handshake between hostA and HOstB

	+------+      +------+      +------+

	|Host A|      |Router|      |Host B|

	+--+---+      ++----++      +---+--+
	  |    	   |    |   	      |
	+--+-----------++  ++-----------+--+



	TCP - 
	connection establishment - 3way 
	Data Trasfer 
	Close - 4Way 

	3WAY 

	TCP Client A —-> TCP server B 
	A —------->      SYN  —-> B
	A <—----------- SYC/ACK —----B
	A <—----------- ACK —----B

	S=1
	+1
	S=2

5.What is MSS in TCP?

	Packets - segments - size 
	Retransmit 
	100 bit 
	Segment = 4 bit 
	25 segment 

6. Explain how to troubleshoot R1 is not working 

R1-------R2
'	     '
'        '
'        ' 
'        '    EBGP
R3-------R4----------R5---(10.1.1.1/32)

R1---R2 ibgp
R1---R3 ibgp
R3---R4 ibgp
R4---R2 ibgp

7. OSPF states ?

8. Explain any customer reported issue , debugged in the production ?

9.Feature with test plan, manual testing, automation ?
'''