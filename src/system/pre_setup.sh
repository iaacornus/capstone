# system upgrade: #* pass
echo -e "\e[1;32m> Starting full system upgrade to fix CVE vulnerabilities ...\e[0m\nKindly input the current password : 'root' (no quotations) when prompted, and don't let the system die."
sudo dnf update -y

# check for system utilities: #? likely passing    
echo -e "\e[1;32m> Checking the presence of git, installing if not installed ...\e[0m"    
git_check=$(dnf list installed | grep -i "git")
if [[ $git_check != *"git"* ]]; then
    echo -e "\e[1;32m> Installing git in the system ...\e[0m"
    sudo dnf install git -y

fi

# install pip if not installed: #? likely passing
echo -e "\e[1;32m> Checking the presence of python.pip, installing if not installed ...\e[0m"
pip_check=$(dnf list installed | grep "python3-pip")

if [[ $pip_check != *"python3-pip"* ]]; then
    echo -e "\e[1;32m> Installing python3-pip in the system ...\e[0m"
    sudo dnf install python3-pip -y

fi

echo -e "\e[1;32m> Checking the presence of cmake, installing if not installed ...\e[0m"
cmake_check=$(dnf list installed | grep -i "cmake[^-]$")

if [[ $cmake_check != *"cmake"* ]]; then
    echo -e "\e[1;32m> Installing python3-pip in the system ...\e[0m"
    sudo dnf install cmake -y
fi

echo -e "\e[1;32m> Checking the presence of cmake, installing if not installed ...\e[0m"
dlib_check=$(dnf list installed | grep -i "python.-dlib")

if [[ $dlib_check != *"python3-dlib"* ]]; then
    echo -e "\e[1;32m> Installing python3-pip in the system ...\e[0m"
    sudo dnf install python3-dlib -y
fi

# install required packages: #? likely passing
echo -e "\e[1;31m> Installing required packages ...\e[0m"
pip install -r $HOME/capstone/requirements.txt

# setup a systemd service for repository check : #! FAILED
echo -e "\e[1;32m> Setting up a systemd service ...\e[0m"
sudo touch /etc/systemd/system/repository-check.service
echo -e "[Unit]\nDescription=Check the repository for updates every 24 hours.\nAfter=network.target\nStartLimitIntervalSec=5\n\n[Service]\nType=simple\nRestart=always\nRestartSec=5\nUser='exec $USER'\nExecStart=/usr/bin/env python 'exec $HOME/repository/bin/service.py'\n\n[Install]\nWantedBy=multi-user.target" | sudo tee -a /etc/systemd/system/repository-check.service

#! FAILED

sudo systemctl daemon-reload
sudo systemctl enable repository-check.service

# setup the dirs
mkdir -P $HOME/.att_sys/bak

cp --recursive $HOME/capstone/src -t $HOME/.att_sys
mv -recursive $HOME/capstone -t $HOME/.att_sys/bak

# move the binaries: #? likely passing
# main binaries@$HOME/.att_sys/bin/
# cp $HOME/capstone/src/bin/*.py $HOME/.att_sys/bin/

# algorithm@$HOME/.att_sys/algorithm/
# cp $HOME/capstone/src/*.py $HOME/.att_sys/

# utils@$HOME/.att_sys/system/utils
# cp $HOME/capstone/src/system/utils/*.py $HOME/.att_sys/system/utils
# download the setup script instead of moving it
# pre setup script
# wget https://raw.githubusercontent.com/testno0/capstone/devel/src/system/pre_setup.sh -P $HOME/.att_sys/system/
# user setup script
# wget https://raw.githubusercontent.com/testno0/capstone/devel/src/system/user_setup.sh -P $HOME/.att_sys/system/

# misc@HOME/.att_sys/misc
# cp $HOME/capstone/src/misc/*.py $HOME/.att_sys/misc
# cp $HOME/capstone/requirements.txt $HOME/.att_sys/

# remove the old bashrc
rm $HOME/.bashrc
wget https://raw.githubusercontent.com/testno0/capstone/devel/src/system/.bashrc -P $HOME/
source $HOME/.bashrc

chmod -R +x $HOME/.att_sys/system/*.sh
./$HOME/.att_sys/system/user_setup.sh