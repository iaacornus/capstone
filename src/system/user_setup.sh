if [ ! -d "$HOME/.att_sys/user_info" ]; then
    # user information setup
    echo -e "\e[1;32m> User setup ...\e[0m"

    # take the username and email of the user
    echo -e "\e[1m> This information is to be used in database, kindly use correct punctuation.\e[0m"
    read -p "└─╼ Enter the email for access codes and reports: " email
    read -p "└─╼ Enter the username: " user_name
    read -p "└─╼ Enter the school name: " school_name

    # generate user password
    password_hash=$(python $HOME/.att_sys/system/utils/password_gen.py)
    echo -e "\e[1;32m> Your password is:\e[1;0m $password"

    # append user information and password to a file
    echo -e "\e[1;32m> Appending user info ...\e[0m"
    echo -e "$email\n$user_name\n$password_hash\n$school_name" > $HOME/.att_sys/user_info

    python utils/update.py

    sec=10
    while [ $sec -ge 0 ]; do
        echo -e "\e[32m> Setup done! Rebooting after :" $sec"s ...\e[0m\r"
        let "sec=sec-1"
        sleep 1
    done

    systemctl poweroff
else
    echo -e "\e[1;31m> System already setup ...\e[0m"
fi
