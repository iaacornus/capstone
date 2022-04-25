if [ ! -d "$HOME/repository/" ]
then
    # system upgrade : #* pass
    echo -e "\e[1;32m> Starting full system upgrade to fix CVE vulnerabilities ...\e[0m\nKindly input the current password : 'root' (no quotations) when prompted, and don't let the system die."
    sudo dnf update -y
    
    # check for system utilities : #? likely passing    
    echo -e "\e[1;32m> Checking system utils, installing if not installed ...\e[0m"
    
    git_check=$(dnf list all | grep "git")
    pip_check=$(dnf list all | grep "python.pip")

    if [[ $git_check != *"git"* ]]
    then
        echo -e "\e[1;32m> Installing git in the system ...\e[0m"
        sudo dnf install git

    fi

    if [[ $pip_check != *"python.pip"* ]]
    then
        echo -e "\e[1;32m> Installing git in the system ...\e[0m"
        sudo dnf install python3-pip

    fi

    # install required packages : #? likely passing
    echo -e "\e[1;31m> Installing required packages ...\e[0m"
    pip install -r $HOME/capstone/requirements.txt

    # setup a systemd service for repository check : #! on test
    echo -e "\e[1;32m> Setting a systemd service ...\e[0m"
    sudo touch /etc/systemd/system/repository-update.service
    echo -e "[Unit]\nDescription=Check the repository for updates every 24 hours.\nAfter=network.target\nStartLimitIntervalSec=5\n\n[Service]\nType=simple\nRestart=always\nRestartSec=5\nUser='exec $USER'\nExecStart=/usr/bin/env python 'exec $HOME/repository/bin/service.py'\n\n[Install]\nWantedBy=multi-user.target" | sudo tee -a /etc/systemd/system/repository-check.service

    sudo systemctl daemon-reload
    sudo systemctl enable system-integrity.service

    echo -e "\e[1;32m> Starting user setup ...\e[0m"
    ret=$(python $HOME/repository/bin/access.py)

    if [[ $ret = "False" ]]
    then
        # false phase, pass : #? passing
        rm -rf $HOME/capstone/*
        sec=3
        while [ $sec -ge 0 ]; do
            echo -e "\e[1;31m> Verification error, shutting the system down" $sec"s ...\e[0m\r"            
            "\e[32m> Setup done! Rebooting after :" 
            let "sec=sec-1"
            sleep 1
        done

        systemctl poweroff
    elif [[ $ret = "True" ]]
    then
        # end phase : #* pass
        echo -e "\e[32m> User system setup passed.\e[0m"
        git clone https://github.com/testno0/repo
        sec=10
        while [ $sec -ge 0 ]; do
            echo -e "\e[32m> Setup done! Rebooting after :" $sec"s ...\e[0m\r" 
            let "sec=sec-1"
            sleep 1
        done

        systemctl poweroff
    
    fi

else
    #* passed
    echo -e "\e[1;31m> System already setup, pulling updates from repository ...\e[0m"

fi
