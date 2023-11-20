# Users and Permissions

# Piping
![](https://www.testingdocs.com/wp-content/uploads/Pipe-command-Linux-1.png)
- [2022 Piping Vulnerability](https://arstechnica.com/information-technology/2022/03/linux-has-been-bitten-by-its-most-high-severity-vulnerability-in-years/)

# Grep
- https://www.redhat.com/sysadmin/how-to-use-grep
```sh
# Output the lines in the file that have the username in them
cat auth.log | grep <username>

# Match all lines that do not have the keyword (case insensitive) error.
cat syslog | grep -vi error

# Find all the processes that have firefox in them. Give me line numbers too.
ps aux | grep -in firefox

# Find out if 443 is a listening port
netstat -tlnp|grep LISTEN|grep :443

# Search in all files in the current directory that have the username
grep -i <username> *

# Find lines that start with "d".  This would return directories.  (you can do this with just ls too)
ls –al | grep ‘^d’
```

# AWK
- https://phoenixnap.com/kb/awk-command-in-linux#awk-command-syntax
```sh
cat /etc/passwd
awk -F ":" '{print $1 $6}' /etc/passwd
awk -F ":" '{print $1 " - " $6}' /etc/passwd
```

# Additional Commands
```sh
# sort
# Create file with months not in order.
echo -e "Feb\nDec\nMar\nOct\nMay\nJun\nNov\nAug\nSep\nApr\nJan\nJul" > months

# Does this sort as you expect?
cat months | sort

# This is better
cat months | sort -M

# cut
# Use cut to parse the IP
ip -c a | grep inet | grep brd | cut -d " " -f 6 | cut -d "/" -f 1
```

# Users
- https://linuxhandbook.com/useradd-vs-adduser/
![](resources/images/adduser_or_useradd.png)

# Groups
```sh
# Find groups user belongs to
groups
id

# Delete students group
groupdel students

# Create new group with GUID 101
groupadd -g 101 students

# Add group students to supplementary group of user
usermod -a -G students <user>

# Find out who is members of the sudo group
sudo groupmems -lg sudo
```


# Password Management - login.defs
- https://man7.org/linux/man-pages/man5/login.defs.5.html


# Sudo
- https://www.howtogeek.com/447906/how-to-control-sudo-access-on-linux/
- https://opensource.com/article/19/10/know-about-sudo
- https://www.computerhope.com/unix/visudo.htm

- `visudo`
- `sudo -l`  Get info about my access
- `sudo -i`  same as `sudo  su -`  Logs into root


# Permissions
![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flinuxhandbook.com%2Fcontent%2Fimages%2F2020%2F06%2Ffile-permission-explanation-2.png&f=1&nofb=1&ipt=ccf81e166e4d78b6dff56e6a0b7d345c41d006ca23782912ec6db87338eb4073&ipo=images)

- `chmod`  # Modify permissions
- `chown`  # Modify ownership

# SUID, SGID
- https://tbhaxor.com/demystifying-suid-and-sgid-bits/
- https://www.redhat.com/sysadmin/suid-sgid-sticky-bit

```sh
touch myfile
chmod 4764 myfile
ls -l
```

- `find . -perm -6000` #  Way to find files with suid or sgid set

# PATH
- https://linuxconfig.org/linux-path-environment-variable
- `echo $PATH`

# Hard and Soft links
- https://www.redhat.com/sysadmin/linking-linux-explained
```sh
# Create Hard Link
touch file
ln file hardfile
ll -i
echo "hello" >> file
cat hardfile
rm file
ll
rm hardfile

# Create Soft Link
ln -s file softfile
ll -i
rm file
ll
rm softfile
```