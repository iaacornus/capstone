ret=$(python $HOME/repository/bin/access.py)

if [ ! -d "$HOME/repo" ]; then
    ret=$(python $HOME/.att_sys/bin/access.py)

    if [[ $ret = "False" ]]; then
        # false phase, pass : #? passing
        rm -rf $HOME/repo/
        sec=3
        echo -e "\e[1;31m> Verification error, repository was nuked by system for security."            
        systemctl poweroff
    elif [[ $ret = "True" ]]; then
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