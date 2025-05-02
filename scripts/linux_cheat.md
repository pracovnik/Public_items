echo "nameserver 8.8.8.8" >> /etc/resolv.conf


 ----
 

cat <<EOF > ./etc/network/interdace.d/eth2.interface

allow-hotplug eth2

iface eth2 inet static

address 192.168.1.101

netmask 255.255.255.0

gateway 192.168.1.9

EOF

----

auto eth1

allow-hotplug eth1

iface eth1 inet dhcp


----

/etc/init.d/networking restart

/etc/init.d/networking stop

/etc/init.d/networking start

systemctl restart networking


----

du -a -h --max-depth=1 | sort -hr	

----

date --set="2012-6-29 11:59 AM"

date --set='+2 minutes'

----

find /home/program/ -name *2024*.gz -type f -exec rm -f {} \;

find /home/program/main -name main.*.log -type f -exec rm -f {} \;

----

Subor v /etc/netplan/01network.yaml

network:

  ethernets:
  
    enp1s0:
    
      dhcp4: false
      
      addresses:
      
      - 192.168.1.101/24
      
      routes:
      
      - to: default
      
        via: 192.168.1.1
        
      nameservers:
      
        adresses:
        
        - 8.8.8.8
        
