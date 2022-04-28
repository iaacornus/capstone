# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
	for rc in ~/.bashrc.d/*; do
		if [ -f "$rc" ]; then
			. "$rc"
		fi
	done
fi

PS1="\u@\h ❯ "
export PS1

PROMPT_DIRTRIM=2

alias update="bash $HOME/.att_sys/system/utils/update.sh"
alias setup="bash $HOME/.att_sys/system/setup.sh"
alias documentation-help="cat $HOME/.att_sys/help.txt"

unset rc
