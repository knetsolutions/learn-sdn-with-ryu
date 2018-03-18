RYU Part5:
=========

In this exercise, We are going to include the flow expiry/timeouts (hard timeout and  idle timeout) in  the simple_switch_13.py(Layer 2 Switch). 



*Idle Timeout:*

If the flow is Idle(no packets hitting this flow) for the specified time(Idle Time), the flow will be expired.


*Hard Timeout:*

Flow entry must be expired in the specified number of seconds regardless of whether or not packets are hitting the entry


In simple_switch.py, the default timeout values(for idle and hard) are not set(0). it means, the flows are permanent. it will never expiry.



## High level Steps:

1. in the flow addition function, specify the timeouts


## Code changes:

Copy the simple_switch_13.py to ex4_flow_timeout.py file
```
cp simple_switch_13.py ex4_flow_timeout.py
```

Modify the ex4_flow_timeout.py file as below,

1. In the add_flow function, include idle, hard parameters with default value as 0.
2. OFPFlowMod API include the idle_timeout,hard_timeout parameters.

```    
            mod = parser.OFPFlowMod(datapath=datapath, buffer_id=buffer_id,
                                    idle_timeout=idle, hard_timeout=hard, priority=priority, match=match,
                                    instructions=inst)

```
3. Call the add_flow function with idle, hard value


Note : The default command is command=ofproto.OFPFC_ADD



## Test



Ryu Application

```
ryu-manager ex4_flow_timeout.py
```

Mininet Topology

```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=single,4  
```

Lets Ping and watch the flows


OVS flows
```
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```



# Reference:

1. https://www.opennetworking.org/software-defined-standards/specifications/

page 155 contains timeout details.

2. API details
http://ryu.readthedocs.io/en/latest/ofproto_v1_3_ref.html?highlight=OFPFlowMod
