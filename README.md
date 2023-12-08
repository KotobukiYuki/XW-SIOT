# Xianghao's SIOT coursework
A SMART FUTURE  FOR THE WELL-BEING  OF DESKBOUND CREATORS

## Device Setup
<details>
  
<summary>Device setup process</summary>

### 1. Install Raspberry Pi OS (64bit is RAM over 4GB)
You will need a Pi4 (any RAM size) to run this SIOT project. First of all, install an official release of raspi-OS, instruction here: https://www.raspberrypi.com/software/. Remember to enable SSH access when installing the system, otherwise you won't be anble to run the whole setup headless and you will need to connect the Pi4 to a screen, a mouse and a keyboard to perform the setup. 

### 2. Deploy FTP server on the Pi.
Open up a terminal, and establish SSH connection to the Pi. Operation various depending on the OS you use, I'll shown windows demo here:
  1. Open CMD
  2. Type in：
  ```
  ssh <username>@<ip_address_of_Pi>
  ```
  And type in YES if asked and login with your username and password of the Pi4.
  3. Install the FTP server: <br>
  ```
  sudo apt-get install vsftpd
  sudo service vsftpd start
  ```
  Then change some default configs.
  ```
  sudo nano /etc/vsftpd.conf
  ```
  Once the config file is opened, uncomment the following lines:
  ```
  anonymous_enable=NO
  write_enable=YES
  utf8_filesystem=YES
  ```
</details>
  

