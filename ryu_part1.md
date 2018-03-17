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


# References

https://en.wikipedia.org/wiki/OpenFlow

http://ryu.readthedocs.io/en/latest/

http://ryu.readthedocs.io/en/latest/writing_ryu_app.html

https://osrg.github.io/ryu/resources.html

https://github.com/osrg/ryu/tree/master/ryu

