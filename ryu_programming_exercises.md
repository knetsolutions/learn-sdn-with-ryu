# RYU Practices:


## Policy based switch:


Flow rate limit (flows per host)
1.  Write a RYU switching application using L4 match and limit the number of flows per host(only egress direction) in to five.  Dont create new flow if the flow count is five.


2. Write a RYU switching application using L4 match(ip,tcp/udp/icmp,srcport ,dstport ) and always mainintain one flow per host. Whenever new flow is created, remove the old flow if exists.

3. 
   policy file:  
     - Allow/Deny policy between the hosts or subnets:  
       Based on IP, Protocol, Ports and  based on time (or full access)


## Statistics collection:

1. Measure the port utilization in Mbps and Kbps
2. Measure the flows utilization in Mbps and Kbps

# Packet geneartion:
1. ARP Proxy
2. DNS Proxy



