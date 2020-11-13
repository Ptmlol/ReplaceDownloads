# ReplaceDownloads

Linux Terminal program used to replace download files from a website and trick the target into downloading your own malware files located on another URL.
Change  "Download URL for exe" on line 30 with your own download URL.

Only works on HTTP/Linux at the moment.
Python2.7 + compatible.
Windows/HTTPS coming soon..
Used well with MITM programs.


You need to enable port forwarding on Linux and queue iptables
Use:
>iptables -I FORWARD -j NFQUEUE --queue-num 0    

without the # for queueing iptables.

Use:
>iptables -I INPUT -j NFQUEUE --queue-num 0

>iptables -I OUTPUT -j NFQUEUE --queue-num 0

in the terminal instead of the "forward" command if you want to use your own computer for testing and not another computer connected to the same network.

>echo 1 > /proc/sys/net/ipv4/ip_forward 

enables portforwarding
