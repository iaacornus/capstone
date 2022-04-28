ret=$(python $HOME/repository/bin/access.py)

ret=$(python $HOME/.att_sys/bin/access.py)

if [[ $ret = "False" ]]; then
    if [ ! -d "$HOME/repo" ]; then        
        git clone https://github.com/testno0/repo $HOME/ &> /dev/null

    else
        echo -e "\e[32m> User system setup passed.\e[0m"
        cd $HOME/repo/ && git pull
        
    fi

else
  # false phase, pass : #? passing
    rm -rf $HOME/repo/
    sec=3
    echo -e "\e[1;31m> Verification error, repository was nuked by system for security."            
    systemctl poweroff

fi

