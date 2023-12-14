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
  ### 3. Install 
  Open a terminal, and type in:
  ```
  sudo apt-get install python3-flask
  ```
  In the new Raspi OS, it is very likely for you to encounter an error called "externally-managed-environment". This is because in the latest release of Raspi OS, PEP 668 was updated: https://realpython.com/python-virtual-environments-a-primer/?ref=yaolong.net
  Because this project is only a prototype, we will overwrite this by:
  ```
  sudo rm -f /usr/lib/python3.X/EXTERNALLY-MANAGED
  sudo rm -f /usr/lib/python3.X/EXTERNALLY-MANAGED.orig
  ```
  Then we will install some dependencies for the Lidar and the DHT11 environment sensor. 
  For Lidar: https://github.com/TFmini/TFmini-RaspberryPi/tree/master
  For DHT11: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup

  I encountered some issues due to the new PEP 668 policy. For example, the following code didn't work for me:
  ```
  sudo apt-get install libgpiod2
  ```
  but
  ```
  sudo apt install libgpiod2
  ```
  worked! I think the Raspi OS is in a transient state and is not stable. Feel free to drop me an email if the setup didn't work out.
  
  Once you have FLASK installed, just go to the folder where the web server is hosted and type:
  ```
  sudo python3 app.py
  ```
  Then the webapp will be started.
</details>

## Web App UI
![image](https://github.com/KotobukiYuki/XW-SIOT/assets/52342831/09a79fce-365c-4f9f-af98-e60213448fd7)
![image](https://github.com/KotobukiYuki/XW-SIOT/assets/52342831/898e355d-ef50-42dd-bef2-3d93b05ab567)



