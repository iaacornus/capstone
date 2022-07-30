check_program() {
    if [[ ! -d ./installed.programs ]]; then
        dnf list installed 1> $HOME/capstone/installed
    fi

    echo -e "\e[1m> Checking for the presence of $program ...\e[0m"
    check=$(cat ./installed.programs | grep -e $program)
    if [[ $program != *"$program"* ]]; then
        echo -e "\e[1m> Installing $program in the system ...\e[0m"
        sudo dnf install $program -y
    fi
}

# system upgrade: #* pass
echo -e "\e[1;32m> Starting full system upgrade to fix CVE vulnerabilities ...\e[0m\nKindly input the current password : 'root' (no quotations) when prompted, and don't let the system die."
sudo dnf update -y

# check for system utilities: #? likely passing
echo -e "\e[1;32m> Checking the presence of git, installing if not installed ...\e[0m"
program="git"
check_program
program="python3-pip"
check_program
program="cmake"
check_program
program="python-dlib"
check_program

# install required packages: #? likely passing
echo -e "\e[1;32m> Installing required packages ...\e[0m"
pip install -r $HOME/capstone/requirements.txt

# setup a systemd service for repository check : #! FAILED
echo -e "\e[1;32m> Setting up a systemd service ...\e[0m"
mkdir -p $HOME/.config/systemd/user
echo -e "[Unit]\nDescription=Check the repository for updates every 24 hours.\nAfter=network.target\nStartLimitIntervalSec=5\n\n[Service]\nType=simple\nRestart=always\nRestartSec=5\nUser=\"%u\"\nExecStart=/usr/bin/env python \"%h\"/repository/bin/service.py'\n\n[Install]\nWantedBy=multi-user.target" > $HOME/.config/systemd/user/repository-check.service

# replaced with "specifiers" as described from systemd documentation, refer to: https://www.freedesktop.org/software/systemd/man/systemd.unit.html#Specifiers

#! FAILED

systemctl --user daemon-reload
systemctl --user start repository-check.service
systemctl --user enable repository-check.service

# setup the dirs
mkdir -p $HOME/.att_sys/bak

cp --recursive $HOME/capstone/src/* -t $HOME/.att_sys
cp --recursive $HOME/capstone -t $HOME/.att_sys/bak

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

chmod -R +x $HOME/.att_sys/system/user_setup.sh
chmod -R +x $HOME/.att_sys/system/pre_setup.sh
bash $HOME/.att_sys/system/user_setup.sh
