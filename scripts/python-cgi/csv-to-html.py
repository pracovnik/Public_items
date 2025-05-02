#!/usr/bin/python3

import paramiko
import nmap
import socket
from datetime import datetime
import subprocess

print ("Content-type: text/html\n")
print ("<html><head><title>CSV report in html</title></head>")
print ("<body><h1>CSV</h1>")

print ("<table border=1>")
with open('/opt/networkhosts.csv', 'r') as file:
    for line in file:
        xline=line.replace('","',"</td><td>")
        xline=xline.replace("\"\n","</td>")
        xline=xline.replace("\"","<td>")
        print("<tr>"+xline+"</tr>")
print ("</table></body></html>")
