* GPS Clock

Displays the time on a 7-segment display
Uses GPS to determine the timezone
Also runs a local ntp server

Easy install using ansible
Setup BBB with fresh debian install, this guide helps - https://github.com/IEEERobotics/bot/wiki/BBB-Setup
You may need to install drivers for USB Networking to work - http://beagleboard.org/getting-started

Install ansible on your local machine, plug network into the BBB, then run
ansible-playbook playbook.yml -i hosts.yml
