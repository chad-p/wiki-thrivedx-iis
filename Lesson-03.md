# Networking and System Management

- [Check out explainshell.com - trust me.](https://explainshell.com/explain?cmd=apt-get+update+%26%26+apt-get+upgrade)
- [Bash hotkeys - yes, please!](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)

# Ping and Jobs
- https://www.redhat.com/sysadmin/jobs-bg-fg
```sh
ping 8.8.8.8
# ctrl z (send process to background)

ps
jobs -l
fg 1

kill -l
kill -9 <pid>

fg
# ctrl c

ping -c 4 8.8.8.8
```

# Traceroute
- tracert(windows) will use ICMP echo requests.
- traceroute(linux) defaults to UDP echo requests.
```sh
traceroute google.com
mtr google.com
```

# IP
```sh
# These are all the same
ip a
ip addr
ip address
ip address show

ip link
ip route
ip neigh  # ARP
sudo ip address add 192.168.121.45/24 dev enp0s3
sudo ip address del 192.168.121.45/24 dev enp0s3

ip route get 1.1.1.1
ip link set enp0s3 down
```

# Dhclient
```sh
cd /etc/dhcp
dhclient 
```

# Setting Static IP
- [Set IP in Debian 10](https://linuxconfig.org/how-to-set-a-static-ip-address-on-debian-10-buster)
- [Set IP in Debian 11](https://www.linuxtechi.com/configure-static-ip-address-debian/)
- [Set IP in RHEL/CentOS 8](https://www.tecmint.com/set-static-ip-address-in-rhel-8/)

# Route
```sh
man route # Checkout flags
route

sudo ip route add 192.168.121.0/24 dev enp0s3
sudo ip route del 192.168.121.0/24
```

# DNS
```sh
nslookup example.com 8.8.8.8
watch !!  # Will rerun the last command ever few seconds. Good for waiting for DNS up propagate.

# Replacement for nslookup
dig example.com

# Resolved
cat /etc/resolve.conf
ll /etc/resolve.conf
sudo systemctl status systemd-resolved
systemd-resolve --status
cat /etc/systemd/resolved.conf

# Hosts file
cat /etc/hosts
```

# Netstat and SS
- https://computingforgeeks.com/netstat-vs-ss-usage-guide-linux/
```sh
# see established connections on specified port
ss -n -o state established '( dport = :21 or sport = :21 )'

# List all connections
ss -a 
# List listening sockets
ss -l 

netstat
netstat -naob
# What is running on port 80
netstat -tulpn | grep 80
```

# lsof
- https://www.geeksforgeeks.org/lsof-command-in-linux-with-examples/
```sh
lsof -u <user>
lsof -i # all network connections
lsof -i :80
```

# apt and dpkg
- https://www.tecmint.com/linux-package-managers/
```sh
apt update
apt upgrade
apt search nmap
apt install nmap apache2
apt remove nmap
apt purge nmap

/var/log/apt/history.log  # Find apt history

apt list
apt list --installed

apt show apache2

#####
dpkg --help
dpkg -l
wget http://archive.ubuntu.com/ubuntu/pool/universe/c/cowsay/cowsay_3.03+dfsg2-4_all.deb
dpkg -c cowsay*
dpkg -I <package.deb>  #Info
dpkg -i <package.deb>  #Install
```

# yum and rpm
```sh
yum history
yum updateinfo
yum updateinfo list
yum updateinfo list --sec-severity=Critical

man yum-secuirty
yum update --security

# Signed Packages
rpm --import /tmp/<some key>
rpm -qa gpg-pubkey*
rpm -qi <key>

# Download a package then verify key
rpm -K *.rpm

# Install local package
yum localinstall <package>
rpm -i <package>  # or with rpm
rpm -e <package>  # remove

# Search with RPM
rpm --help
rpm -q cowsay
rpm -ql cowsay  # List all files from that package
rpm -qi cowsay  # Package summary
```

# Services | Daemons
- https://web.yueh.dev/learning/init-vs-systemd-what-is-an-init-daemon
```sh
# Service is SysV
server --status-all
service sshd status
cat /etc/initab

# Systemctl
systemctl list-units
systemctl list-units --type service --state running
systemctl list-units --type service --state running --no-legend
systemctl list-units --type service --state failed --no-legend
systemctl --no-pager | grep service | grep running | column -t
systemd-analyze blame

systemctl status sshd
systemctl start sshd
systemctl enable sshd
systemctl disable sshd
#Disable services for hardening

cat /usr/lib/systemd/system/sshd.service
systmctl cat sshd
systemctl daemon-reload
systemctl --no-pager show --property=UnitPath
```
# Journald
- [Man Page](https://www.freedesktop.org/software/systemd/man/journald.conf.html)
- https://gist.github.com/sergeyklay/f401dbc8286f732783e05072f03ecb61
```sh
# follow the ssh service
journalctl -u ssh -f
```

# dmesg
```sh
dmesg -H
```
# nginx
```sh
cd /etc/nginx/sites-enabled/default
```

# Bash Scripting

- [Site to check shell scripts](https://www.shellcheck.net/)

# Alias
- https://linuxize.com/post/how-to-create-bash-aliases/


# Bash Scripting
- https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html
- https://www.redhat.com/sysadmin/formatting-date-command
- https://www.networkworld.com/article/2694433/unix-good-coding-practices-for-bash.html
- https://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html
- https://tldp.org/LDP/abs/html/options.html
- https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Conditional-Constructs

```bash
echo “What is your favorite dish?”  
read dish
echo “I like $dish also!”
```

```bash
#!/bin/bash  
WHO_AM_I=$(whoami)  
LIST=`ls -a`  
echo $WHO_AM_I; echo $LIST
```

#### Logical Operators
- AND = Please go to the store AND purchase some milk
- OR = Please go to bed OR you will be grounded.


```sh
#!/bin/bash  
num=3  
read -ep "Enter a number: " userNum  
if [ $userNum -gt $num ]; then  
	echo "Your number is greater than the number in the variable"  
else  
	echo "The number in the variable is greater or equal to your number"  
fi
```

```sh
#!/bin/bash  
for i in {1..255};
do
    echo "i var is: $i"
done
```

```sh
#!/bin/bash  
# Clear file at the beginning of the process  
cd ~/Desktop  
echo "" > liveHost;  
# Loop in the range 1 to 255  
for i in {1..255};  
do  
    echo "[+] pinging 10.71.0.$i";  
    ping -c 1 10.71.0.$i | grep "bytes from" >> liveHost;  
done  
echo "Done!"
```

```sh
#!/bin/bash    
x=1  
#A loop that will run as long as the value of $x is less than 5  
while [ $x -lt 5 ]  
do  
    echo “Execution times count: $x”  
    x=$(( $x + 1 ))  
done
```

```sh
test 2 -gt 3; echo $?
```

```sh
#!/bin/bash  
touch /root/file.txt  
if [ $? -lt 1 ]  
then  
    echo “File created."  
else  
    echo “An error has occurred."  
fi
```

```sh
#!/bin/bash  
for i in {1..255};
do
    let sum=$i*$i
    echo "$i multiplied by itself equals: $sum"
done
```

# Arithmetic
- https://phoenixnap.com/kb/bash-math#ftoc-heading-16
- https://askubuntu.com/questions/939294/difference-between-let-expr-and

```sh
y=5 
x=10

let sum=2+2
echo "This is the sum $sum"  # This is the sum 4

let sum+=2
echo $sum

expr $x+$y # > 5+10
expr $x + $y # > 15
expr 5 * 5 # error because * needs to be \*
expr 11 / 5  # Still floor division

echo $x+$y  # > 5+10
echo $(($x+$y)) # > 15
echo $((x+y)) # > 15
echo $((x/y)) # > Floor result... Update x to 11 and rerun

expr $x+$y # > 5+10
expr $x + $y # > 15
expr 11 / 5  # Still floor division


echo "1 / 5" | bc
echo "scale=2; 11 / 5" | bc  # bc stands for basic calculator
```

# Tar
![](https://imgs.xkcd.com/comics/tar.png)
- https://www.interserver.net/tips/kb/use-tar-command-linux-examples/
- https://catchchallenger.herman-brule.com/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO

  - [c]reate an archive and write it to a [f]ile:
    `tar cf target.tar file1 file2 file3`

  - [c]reate a g[z]ipped archive and write it to a [f]ile:
    `tar czf target.tar.gz file1 file2 file3`

  - [c]reate a g[z]ipped archive from a directory using relative paths:
    `tar czf target.tar.gz --directory=path/to/directory .`

  - E[x]tract a (compressed) archive [f]ile into the current directory [v]erbosely:
    `tar xvf source.tar[.gz|.bz2|.xz]`

  - E[x]tract a (compressed) archive [f]ile into the target directory:
    `tar xf source.tar[.gz|.bz2|.xz] --directory=directory`

  - [c]reate a compressed archive and write it to a [f]ile, using [a]rchive suffix to determine the compression program:
    `tar caf target.tar.xz file1 file2 file3`

  - Lis[t] the contents of a tar [f]ile [v]erbosely:
    `tar tvf source.tar`

  - E[x]tract files matching a pattern from an archive [f]ile:
    `tar xf source.tar --wildcards "*.html"`


# bzip2/bunzip2 - A block-sorting file compressor.
  - Compress a file:
    `bzip2 path/to/file_to_compress`

  - Decompress a file:
    `bzip2 -d path/to/compressed_file.bz2`

  - Decompress a file to standard output:
    `bzip2 -dc path/to/compressed_file.bz2`

# gzip
  - Compress a file, replacing it with a gzipped compressed version:
    `gzip file.ext`

  - Decompress a file, replacing it with the original uncompressed version:
    `gzip -d file.ext.gz`

  - Compress a file, keeping the original file:
    `gzip --keep file.ext`

  - Compress a file specifying the output filename:
    `gzip -c file.ext > compressed_file.ext.gz`

  - Decompress a gzipped file specifying the output filename:
    `gzip -c -d file.ext.gz > uncompressed_file.ext`

  - Specify the compression level. 1=Fastest (Worst), 9=Slowest (Best), Default level is 6:
    `gzip -9 -c file.ext > compressed_file.ext.gz`


# zip

`zip -e “locked.zip” file1 file2 file3`   or --encrypt

  - Add files/directories to a specific archive:
    `zip -r path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...`

  - Remove files/directories from a specific archive:
    `zip --delete path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...`

  - Archive files/directories e[x]cluding specified ones:
    `zip path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ... --exclude path/to/excluded_files_or_directories`

  - Archive files/directories with a specific compression level (`0` - the lowest, `9` - the highest):
    `zip -r -0-9 path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...`

  - Create an encrypted archive with a specific password:
    `zip -r --encrypt path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...`

  - Archive files/directories to a multi-part [s]plit zip file (e.g. 3 GB parts):
    `zip -r -s 3g path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...`
  
  - Print a specific archive contents:
	`zip -sf path/to/compressed.zip`


# xz

  - Compress a file to the xz file format:
	`xz file`

  - Decompress a xz file:
    `xz -d file.xz`

  - Compress a file to the LZMA file format:
    `xz --format=lzma file`

  - Decompress an LZMA file:
    `xz -d --format=lzma file.lzma`

  - Decompress a file and write to stdout:
    `xz -dc file.xz`

  - Compress a file, but don't delete the original:
    `xz -k file`

  - Compress a file using the fastest compression:
    `xz -0 file`

  - Compress a file using the best compression:
    `xz -9 file`


# Hasing
- https://codesigningstore.com/hash-algorithm-comparison
- https://www.redhat.com/sysadmin/hashing-checksums


# Cron
https://crontab.guru