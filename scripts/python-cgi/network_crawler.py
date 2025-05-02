#!/usr/bin/python3

import paramiko
import nmap
import socket
from datetime import datetime
import subprocess

socket.setdefaulttimeout(5)
nmALL = nmap.PortScanner()
nmONE = nmap.PortScanner()
nmALL.scan(hosts='192.168.1.0/24', arguments='-sP -n -PE --max-parallelism 100')
host_list = nmALL.all_hosts()


def testport(oneIP,Port):
   nmPORT = nmap.PortScanner()
   nmPORT.scan(hosts=oneIP, arguments='-p T:'+Port)
   host_list = nmPORT.all_hosts()
   for host in host_list:
      for OnePort in Port.split(","):
         if OnePort == "22" :
            print("<td>")
            if nmPORT[host]['tcp'][int(OnePort)]['state'] != "closed" :
               if nmPORT[host]['tcp'][int(OnePort)]['state'] == "open" :
                  try:
                     ssh = paramiko.SSHClient()
                     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                     ssh.connect(hostname=oneIP, port=22, username="ivo", password="heslo123")
                     ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("hostname")
                     output = ssh_stdout.readlines()
                     print("<b> "+output[0]+"</b><br>")
                  except:
                     print(" ")
               if nmPORT[host]['tcp'][int(OnePort)]['state'] == "filtered" :
                  print("<small>Un-open</small><br>")
            print("</td>")
         if OnePort == "80":
            if nmPORT[host]['tcp'][int(OnePort)]['state'] == "open" :
               print("<td><small><a href=http://"+oneIP+">http://"+oneIP+"</a></small></td>")
            else:
               print("<td>-</td>")
         if OnePort == "443":
            if nmPORT[host]['tcp'][int(OnePort)]['state'] == "open" :
               print("<td><small><a href=https://"+oneIP+">https://"+oneIP+"</a></small></td>")
            else:
               print("<td>-</td>")
         if (OnePort == "22"):
            if nmPORT[host]['tcp'][int(OnePort)]['state'] == "open" :
               print("<td><small>ssh -p  22 "+oneIP+"</small></td>")
            else:
               print("<td>-</td>")

print("Content-type: text/html\n")
print("<html><head><title>Network lists</title></head>")
print("<body><h1>Network lists</h1>")

print("<table border=1>")
for host in host_list:
   print("<tr>")
   try:
      match nmALL[host]['addresses']['ipv4']:
         case "192.168.1.100":
            print("<td>"+nmALL[host]['addresses']['ipv4']+"<br><small>THERE server</small></td>")
         case "192.168.1.99":
            print("<td>"+nmALL[host]['addresses']['ipv4']+"<br><small>wiko</small></td>")
         case "192.168.1.98":
            print("<td>"+nmALL[host]['addresses']['ipv4']+"<br><small>toll</small></td>")
         case "192.168.1.97":
            print("<td>"+nmALL[host]['addresses']['ipv4']+"<br><small>fark</small></td>")
         case "192.168.1.111":
            print("<td>"+nmALL[host]['addresses']['ipv4']+"<br><small>partkd</small></td>")
         case _:
            if "hostnames" in nmALL[host]:
               print("<td>"+nmALL[host]['addresses']['ipv4']+"<br><small>")
               for hostname in nmALL[host]['hostnames']:
                  print(hostname["name"]+"<br>")
               print("</small></td>")
            else:
               print("<td>"+nmALL[host]['addresses']['ipv4']+"</td>")

   except:
      print("<td>-</td>")

   try:
      print("<td>"+nmALL[host]['addresses']['mac']+"</td>")
   except:
      print("<td>-</td>")
   testport(nmALL[host]['addresses']['ipv4'],"22,80,443")

   print("</tr>")

print("</table></body></html>")
