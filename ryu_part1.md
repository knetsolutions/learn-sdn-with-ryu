# RYU Basic Usage:


## 1. How to start the ryu controller 

```
ryu-manager  <application file name>

```
Example applications are available in ryu.app.<application file name> or we can specify the filename(with absolute path).
  


Check the running process details.

```
ps -ef | grep ryu-manager
```

RYU Manager listens on openflow ports(6653,6633) are in listening state.


Check the port statistics

```
netstat -ap 
netstat -ap | grep python

```


## 2. How to stop the ryu controller

```
CTRL + C (Kill the Process)

( or )
pkill -9 ryu-manager

```

Please check the running process by  ps -ef | grep ryu-manager


## 3. RYU Controller command line options


```
ryu-manager --help

```

```
ryu-manager --verbose  <application>

```


## 4. How to run the Application

Example Application is installed in ryu/app folder.

Specify the filename as ryu.app.<filename>

Example:


```
ryu-manager --verbose  ryu.app.simple_switch_13

```

Download the file  and run it.

```
ryu-manager --verbose  simple_switch_13.py

```

# RYU Application overview:




## Step1 : Import the base classes / library

```
from ryu.base import app_manager

from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls

from ryu.ofproto import ofproto_v1_3

from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
```

**app_manager :**   main entry point for the application.

**set_ev_cls, ofp_event, Dispatcher :**   used for capturing openflow event, when the openflow packet received

**ofproto_v1_3 :** Specifies which Openflow version to be used.

**packet, ethernet, ether_types :**  packet processing library



## step2:  Define your application class (derived from app_manager):


class SimpleSwitch13(app_manager.RyuApp):









# References

https://en.wikipedia.org/wiki/OpenFlow

http://ryu.readthedocs.io/en/latest/

http://ryu.readthedocs.io/en/latest/writing_ryu_app.html

https://osrg.github.io/ryu/resources.html

https://github.com/osrg/ryu/tree/master/ryu

