# Introduction to Linux

# History
* [History of Linux](https://www.computerhope.com/history/unix.htm)
* [Prettier History of Linux](https://historydraft.com/story/linux/timeline/533)
* [Linus first post](https://fossbytes.com/linus-torvaldss-famous-email-first-linux-announcement/)
* [Youtube: The Unix Operating System](https://www.youtube.com/watch?v=tc4ROCJYbm0)
* [Linux Statistics](https://hostingtribunal.com/blog/linux-statistics/)
* [Supercomputers](https://www.top500.org/statistics/sublist/)
* [IOT running linux](https://www.itprotoday.com/iot/survey-shows-linux-top-operating-system-internet-things-devices)
* [27 Facts about linux](https://www.omgubuntu.co.uk/2018/08/interesting-facts-about-linux)
* [GNU](https://www.gnu.org/)

![](resources/images/use_linux.jpg)

## Kernel
* [Linux Kernel](https://kernel.org/)
* [Tutorials Point - Linux OS](https://www.tutorialspoint.com/operating_system/os_linux.htm)

![image](https://www.tutorialspoint.com/operating_system/images/linux_architecture.jpg)

# Distributions
* [Wiki Distro Timeline](https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg)
* [Distribution Comparison](https://linuxhint.com/linux_distribution_comparison/)
![](resources/images/many_distros.jpg)

## Desktop Environments
* [Top Desktop Environments](https://www.linuxandubuntu.com/home/desktop-environments-for-linux)
* [Gnome](https://www.gnome.org/)
* [KDE](https://kde.org/)

## A few popular distributions
Server
* [Debian](https://www.debian.org/)
    * [Ubuntu](https://ubuntu.com/download/server)
* [RHEL](https://www.redhat.com/en)
    * [CentOS](https://www.centos.org/)
    * [Rocky](https://rockylinux.org/)

Desktop
* [Fedora](https://getfedora.org/)
* [Ubuntu](https://ubuntu.com/download/desktop)
* [Arch](https://archlinux.org/)
* [Mint](https://linuxmint.com/)

Pentesting
* [Kali](https://www.kali.org/)
* [Parrot](https://parrotlinux.org/)

DIFR
* [Tsurugi](https://tsurugi-linux.org/) 
* [SANS Sift Workstation](https://www.sans.org/tools/sift-workstation/)
* [Paladin](https://sumuri.com/software/PALADIN/)

Misc
* [Proxmox](https://www.proxmox.com/en/)
* [RetroPie](https://retropie.org.uk/)
* [Open Media Vault](https://www.openmediavault.org/)


# Open-Source Philosophy
* [Opensource.org - About Licenses](https://opensource.org/licenses)
* [Mend.io - Open Source Licenses Explained](https://www.mend.io/resources/blog/open-source-licenses-explained/)

# Linux Installation
* [Linux Handbook - Directories](https://linuxhandbook.com/linux-directory-structure/)
* [Wiki - Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
* `man hier`

### Troubleshooting
* If slow (turtle icon) try turning off [windows core isolation setting](https://www.pcworld.com/article/1069899/windows-11s-performance-stealing-security-feature-is-now-on-by-default.html). 

# CLI Fundamentals

# Additional CLI trainings
- https://linuxjourney.com/
- https://www.linuxcommand.org/lc3_learning_the_shell.php
- https://www.reddit.com/r/linuxupskillchallenge/
- https://overthewire.org/wargames/bandit/


# Cheatsheet
- https://cheatography.com/davechild/cheat-sheets/linux-command-line/
- [Crazy Big Linux Mindmap Command Cheatsheet](resources/pdfs/linux_mindmap_command_cheatsheet.pdf)

# Gathering System Information
`ls -lah`
![](resources/images/ls_command.jpg)

```bash
# What user is running
whoami

# List block devices
lsblk
fdisk -l

# System Resources
lscpu  # or cat /proc/cpuinfo
lsmem  # or cat /proc/meminfo

# What distro am I on
cat /etc/os-release

# Processes that are running
ps aux

# What services are running
service --status-all
systemctl list-units --type service --state running

# Open ports
ss -atu

# Network Information
ifconfig
ip -c a

# Kernel info
uname -vr
```

# Shell
![](https://upload.wikimedia.org/wikipedia/commons/8/8f/Ken_Thompson_%28sitting%29_and_Dennis_Ritchie_at_PDP-11_%282876612463%29.jpg)
![](https://steemitimages.com/DQmaLG5aMZJwwEEayyUCE1GW36r2KvimNjgQxduNFYbjS8i/LearADA3.jpg)
![](https://developer.ibm.com/developer/tutorials/l-linux-shells/images/figure1.gif)

```sh
# Find what shell you are using
echo $0
```
- [ZFS vs Bash](https://www.educba.com/zsh-vs-bash/)


# Command Help
- `<command> --help`
- `man <command>`
- `info <command>`
- `type <command>`

# Working with files
```sh
# Remove everything but one file
rm -v !("file_to_keep")
```

# Using Find
- https://www.tecmint.com/35-practical-examples-of-linux-find-command/
- https://linuxconfig.org/locate-vs-find-what-is-the-difference
```sh
find . -name myfile.txt
```


## Input/Output
![](https://www.putorius.net/wp-content/uploads/2019/02/standard-streams.jpg)
- https://linuxhandbook.com/redirection-linux/

```sh
echo "redirect this to a file" > file.txt
echo "append this to a file" > file.txt

ls zepplin 2>errors.txt
ls zepplin 2>/dev/null

tr a-z A-Z < filename.txt
```

# Vim
![](resources/images/chatgpt-exit-vim.png)

# Globbing
- https://linuxhint.com/bash_globbing_tutorial/
```sh
ls ????.*

egrep '*-0[56]-*'  # Find all dates in May or Jone
grep '[Mm]ate' file  # Match lines with Mate or mate
```


# Brace Expansion
- https://sodocumentation.net/bash/topic/3351/brace-expansion
```sh
echo {1..10}
echo {0001..10}
echo {0..10..2}
mkdir 20{09..11}-{01..12}

mkdir -p toplevel/sublevel_{01..09}/{child1,child2,child3}
```