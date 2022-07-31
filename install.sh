SUCCESS="\e[1m[ \e[32mPASS\e[0m\e[1m ]\e[0m"
FAIL="\e[1m[ \e[31mFAIL\e[0m\e[1m ]\e[0m"
INFO="\e[1m[ INFO ]\e[0m"
INPT="\e[1m[ INPT ]\e[0m"
PROC="\e[1m[ PROC ]\e[0m"
END="... \e[0m"


echo -e "$INPT Read license file? [y/N] "
read license
if [[ "$license" != "n" || "$license" != "N" ]]; then
    less LICENSE 2> /dev/null
fi

echo -e "$INFO This repository of project contains refactored code in which some parts are experimental and not tested. Proceed in your discretion.\n$INFO Executing setup script, press any key to continue ..."
read
./pre_setup.sh
