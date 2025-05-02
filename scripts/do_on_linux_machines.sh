declare -a arr=(
"192.168.1.2"
"192.168.1.3"
"192.168.1.4"
"192.168.1.5"
)



cat <<EOF > /tmp/script.sh
#!/bin/bash

#prepare:
cd /tmp
rm -rf /tmp/export_files /tmp/export_files.tar
mkdir -p /tmp/export_files

#Linux logs
cp /var/log/xlog.* /tmp/export_files/ 2>/dev/null

#hostname
hostname > /tmp/export_files/hostname.txt   2>/dev/null

#prepare for out-sending
tar -cvf /tmp/export_files.tar /tmp/export_files/*

EOF

echo "first argument is password"

## now loop through the above array
for i in "${arr[@]}"
do
   echo "$i ######################################################"
   #create folder for the IP
   mkdir -p ./$i

   #Transfer the script to the machine
   ssh-pass -p $1 scp /tmp/script.sh "admin@$i:/tmp/"

   #Execute the script on the machine
   ssh-pass -p $1 | ssh "admin@$i" "bash /tmp/script.sh"

   #Fetch the compressed tar with data to the machine
   ssh-pass -p $1 | scp "admin@$i:/tmp/export_files.tar" ./$i/
   
   #Decompress the tar
   tar -xvf ./$i/export_files.tar -C ./$i/
done
