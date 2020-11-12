# ReplaceDownloads

Linux Terminal Python3 program used to replace download files from a website and trick the target into downloading your own malware files located on another URL.
Change  "Download URL for exe" on line 30 with your own download URL.
Only works on HTTP/Python3Linux at the moment. Windows/Python<2/HTTPS coming soon..
Used well with MITM programs.

You need to enable port forwarding on Linux and queue iptables
Type in the Linux terminal:
>#iptables -I FORWARD -j NFQUEUE --queue-num 0    -without the # for queueing iptables.

>#echo 1 > /proc/sys/net/ipv4/ip_forward    -without the # for ipforwarding
