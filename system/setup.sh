if [ ! -d "$HOME/repository/" ]
then
    # check for system utilities : #? likely passing
    echo -e "\e[1;32m> Pulling data from repository ...\e[0m"

    distro_id=$(cat /etc/os-release | grep "ID")
    
    if [[ $distro = "fedora" ]]
    then
        git_check=$(dnf list all | grep "git\|python.pip")
        package_manager="dnf install"
    elif [[ $distro = "arch" ]]
    then
        git_check=$(pacman -Q | grep "git\|python.pip")
        package_manager="pacman -S"
    elif [[ $distro = "ubuntu "]]
    then   
        git_check=$(apt list all | grep "git\|python3-pip\|python.pip")
        package_manager="apt get-install"
    fi

    if [[ $git_check != *"git"* ]]
    then
        true
    else
        echo -e "\e[1;32m> Installing git in the system ...\e[0m"
        sudo $package_manager git python.pip
    fi

    # install required packages : #? likely passing
    echo -e "\e[1;31m> Installing required packages ...\e[0m"
    
    if [[ $distro = "fedora" ]] || [[ $distro = "arch" ]]
    then
        pip install -r requirements.txt
    elif [[ $distro = "ubuntu" ]]
    then    
        pip3 install -r requirements.txt
    fi

    # setup a systemd service for repository check : #! on test
    echo -e "\e[1;32m> Setting a systemd service ...\e[0m"
    sudo touch /etc/systemd/system/repository-update.service
    echo -e "[Unit]Description=Check the repository for updates every 24 hours.\n\n[Service]\nType=simple\nExecStart=python ~/repository/bin/service.py\n\n[Install]\nWantedBy=multi-user.target" | sudo tee -a /etc/systemd/system/repository-check.service

    sudo systemctl daemon-reload
    sudo systemctl enable system-integrity.service

    echo -e "\e[1;32m> Starting user setup ...\e[0m"
    ret=$(python $HOME/repository/bin/access.py)

    # false phase, pass : #* pass
    if [[ $ret = "False" ]]
    then    
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
        echo -e "\e[32m> User system setup passed.\e[0m"
    fi

    # end phase : #* pass
    sec=10
    while [ $sec -ge 0 ]; do
        echo -e "\e[32m> Setup done! Rebooting after :" $sec"s ...\e[0m\r" 
        let "sec=sec-1"
        sleep 1
    done

    systemctl poweroff
else
    # theoretical : #! on test
    echo -e "\e[1;31m> System already setup, pulling updates from repository ...\e[0m"
    cd $HOME/repository
    git pull
    exit 1
fi
