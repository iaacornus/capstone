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
export PATH="$PATH:$HOME/.att_sys/"

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

PS1="\u@\h:\w $ "
export PS1

PROMPT_DIRTRIM=2

if [ ! -d "$HOME/.att_sys/" ]; then
	alias taptap="python $HOME/.att_sys/cli.py"
else
	alias taptap="echo 'taptap not installed.'"
fi

unset rc
