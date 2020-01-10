#!/usr/bin/python
# -*- coding: utf-8 -*-

# O módulo subprocess é necessário para executar comandos externos ao Python
import subprocess 

#A função return_code é usada para chamar o comando ifconfig e retorna sua saída
return_code = subprocess.call('sudo zypper lu', shell=True) 
return_code = subprocess.call('sudo zypper ref', shell=True) 
return_code = subprocess.call('sudo zypper addrepo --refresh https://download.opensuse.org/repositories/system:/snappy/openSUSE_Leap_15.0 snappy', shell=True) 
return_code = subprocess.call('sudo zypper --gpg-auto-import-keys refresh', shell=True) 
return_code = subprocess.call('sudo zypper in -y snapd ', shell=True) 
return_code = subprocess.call('sudo systemctl enable snapd', shell=True)
return_code = subprocess.call('sudo systemctl start snapd', shell=True)
return_code = subprocess.call('sudo snap install code --classic', shell=True)