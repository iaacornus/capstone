SUCCESS="\e[1m[ \e[32mPASS\e[0m\e[1m ]\e[0m"
FAIL="\e[1m[ \e[31m FAIL\e[0m\e[1m ]\e[0m"
INFO="\e[1m[ INFO ]\e[0m"
PROC="\e[1m[ PROC ]\e[0m"
END="... \e[0m"

check_program() {
    if [[ ! -d ./installed.programs ]]; then
        dnf list installed 1> $HOME/capstone/installed
    fi

    echo -e "$PROC Checking for the presence of $program $END"
    check=$(cat ./installed.programs | grep -e $program)
    if [[ $program != *"$program"* ]]; then
        echo -e "$PROC Installing $program in the system $END"
        sudo dnf install $program -y
    fi
}

# system upgradeS
echo -e "$PROC Starting full system upgrade to fix CVE vulnerabilities $END\nKindly input the current password : 'root' (no quotations) when prompted, and don't let the system die."
sudo dnf update -y

# check for system utilities
program="git"
check_program
program="python3-pip"
check_program
program="cmake"
check_program
program="python-dlib"
check_program

# install required packages
echo -e "$PROC Installing required packages $END"
pip install -r $HOME/capstone/requirements.txt

# setup a systemd service for repository check
echo -e "$PROC Setting up a systemd service $END"
mkdir -p $HOME/.config/systemd/user
echo -e "[Unit]\nDescription=Check the repository for updates every 24 hours.\nAfter=network.target\nStartLimitIntervalSec=5\n\n[Service]\nType=simple\nRestart=always\nRestartSec=5\nUser=\"%u\"\nExecStart=/usr/bin/env python \"%h\"/repository/bin/service.py'\n\n[Install]\nWantedBy=multi-user.target" > $HOME/.config/systemd/user/repository-check.service

systemctl --user daemon-reload
systemctl --user start repository-check.service
systemctl --user enable repository-check.service

# setup the dirs
mkdir -p $HOME/.easywiz/bak

cp --recursive $HOME/capstone/src/* -t $HOME/.easywiz
cp --recursive $HOME/capstone -t $HOME/.easywiz/bak

# remove the old bashrc
rm $HOME/.bashrc
wget https://raw.githubusercontent.com/testno0/capstone/devel/src/system/.bashrc -P $HOME/
source $HOME/.bashrc

chmod +x $HOME/.easywiz/sutils/user_setup.sh
chmod +x $HOME/.easywiz/sutils/pre_setup.sh
$HOME/.easywiz/sutils/./user_setup.sh
