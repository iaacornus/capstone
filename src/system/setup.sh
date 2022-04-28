# test 1: #* passed!

if [ ! -d "$HOME/.att_sys/" ]; then
    # system upgrade: #* pass
    echo -e "\e[1;32m> Starting full system upgrade to fix CVE vulnerabilities ...\e[0m\nKindly input the current password : 'root' (no quotations) when prompted, and don't let the system die."
    #sudo dnf update -y
    
    # check for system utilities: #? likely passing    
    echo -e "\e[1;32m> Checking the presence of git, installing if not installed ...\e[0m"    
    git_check=$(dnf list all | grep "git")
    if [[ $git_check != *"git"* ]]; then
        echo -e "\e[1;32m> Installing git in the system ...\e[0m"
        sudo dnf install git

    fi

    # install pip if not installed: #? likely passing
    echo -e "\e[1;32m> Checking the presence of python.pip, installing if not installed ...\e[0m"
    pip_check=$(dnf list all | grep "python3-pip")
 
    if [[ $pip_check != *"python3-pip"* ]]; then
        echo -e "\e[1;32m> Installing python3-pip in the system ...\e[0m"
        sudo dnf install python3-pip

    fi

    # install required packages: #? likely passing
    echo -e "\e[1;31m> Installing required packages ...\e[0m"
    pip install -r $HOME/capstone/requirements.txt

    # setup a systemd service for repository check : #! on test
    echo -e "\e[1;32m> Setting up a systemd service ...\e[0m"
    sudo touch /etc/systemd/system/repository-check.service
    echo -e "[Unit]\nDescription=Check the repository for updates every 24 hours.\nAfter=network.target\nStartLimitIntervalSec=5\n\n[Service]\nType=simple\nRestart=always\nRestartSec=5\nUser='exec $USER'\nExecStart=/usr/bin/env python 'exec $HOME/repository/bin/service.py'\n\n[Install]\nWantedBy=multi-user.target" | sudo tee -a /etc/systemd/system/repository-check.service

    sudo systemctl daemon-reload
    sudo systemctl enable repository-check.service

    # setup the dirs
    mkdir $HOME/.att_sys $HOME/.att_sys/bin $HOME/.att_sys/system $HOME/.att_sys/system/utils $HOME/.att_sys/misc $HOME/.att_sys/algorithm
    touch $HOME/.att_sys/user_info

    # move the binaries: #? likely passing
    # main binaries@$HOME/.att_sys/bin/
    mv $HOME/capstone/src/bin/* $HOME/.att_sys/bin/

    # algorithm@$HOME/.att_sys/algorithm/
    mv $HOME/capstone/src/algorithm/* $HOME/.att_sys/algorithm

    # utils@$HOME/.att_sys/system/utils
    mv $HOME/capstone/src/system/utils/* $HOME/.att_sys/system/utils
    # download the setup script instead of moving it
    wget https://raw.githubusercontent.com/testno0/capstone/devel/src/system/setup.sh -P $HOME/.att_sys/system/

    # misc@HOME/.att_sys/misc
    mv $HOME/capstone/src/misc/* $HOME/.att_sys/misc
    mv $HOME/capstone/requirements.txt $HOME/.att_sys/

    # remove the old bashrc
    rm $HOME/.bashrc
    wget https://raw.githubusercontent.com/testno0/capstone/devel/src/system/.bashrc -P $HOME/
    source $HOME/.bashrc

    # user information setup : #* pass
    echo -e "\e[1;32m> User setup ...\e[0m"

    # take the username and email of the user
    echo -e "\e[1m> This information is to be used in database, kindly use correct punctuation.\e[0m"
    read -p "└─╼ Enter the email for access codes and reports: " email
    read -p "└─╼ Enter the username: " user_name
    read -p "└─╼ Enter the school name: " school_name
    
    # generate user password
    password=$(python $HOME/.att_sys/system/utils/password_gen.py)
    echo -e "\e[1;32m> Your password is: $password"

    # append user information and password to a file
    echo -e "\e[1;32m> Appending user info ...\e[0m"
    echo -e "$email\n$user_name\n$password\n$school_name" >> $HOME/.att_sys/user_info

    bash $HOME/.att_sys/system/utils/update.sh

    sec=10
    while [ $sec -ge 0 ]; do
        echo -e "\e[32m> Setup done! Rebooting after :" $sec"s ...\e[0m\r" 
        let "sec=sec-1"
        sleep 1
    done

    systemctl poweroff

else
    #* passed
    echo -e "\e[1;31m> System already setup ...\e[0m"

fi
