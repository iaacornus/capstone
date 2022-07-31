SUCCESS="\e[1m[ \e[32mPASS$END\e[1m ]\e[0m"
FAIL="\e[1m[ \e[31m FAIL$END\e[1m ]\e[0m"
INFO="$END[ INFO ]\e[0m"
PROC="\e[1m[ PROC ]\e[0m"
INPT="\e[1m[ INPT ]\e[0m"
END="... \e[0m"

if [ ! -d "$HOME/.att_sys/user_info" ]; then
    # user information setup
    echo -e "$PROC User setup $END"

    # take the username and email of the user
    echo -e "\e[1m[=] This information is to be used in database, kindly use correct punctuation.\e[0m"
    read -p "$INPT Enter the email for access codes and reports: " email
    read -p "$INPT Enter the username: " user_name
    read -p "$INPT Enter the school name: " school_name

    # generate user password
    echo -e "$INFO Your password is:$END"
    password_hash=$(python $HOME/.easywiz/sutils/password_gen.py)

    # append user information and password to a file
    echo -e "$PROC Appending user info $END"
    echo -e "$email\n$user_name\n$password_hash\n$school_name" > $HOME/.easywiz/user_info

    python $HOME/.easywiz/sutils/update.py
    sec=10
    while [ $sec -ge 0 ]; do
        echo -e "$SUCCESS Setup done! Rebooting after :" $sec"s $END\r"
        let "sec=sec-1"
        sleep 1
    done

    systemctl poweroff
else
    echo -e "$FAIL System already setup $END"
fi
