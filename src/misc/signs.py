class Signs:
    RPROC: str = "[bold][ PROC ][/bold]"
    RFAIL: str = "[bold][ [red]FAIL[/red] ][/bold]"
    RPASS: str = "[bold][ [green]PASS[/green] ][/bold]"
    RINFO: str = "[bold][ INFO ][/bold]"
    RINPT: str = "[bold][ INPT ][/bold]"

    PROC: str = "\033[1m[ PROC ]\033[0m"
    FAIL: str = "\033[1m[ \033[31mFAIL\033[0m\033[1m ]\033[0m"
    PASS: str = "\033[1m[ \033[32mPASS\033[0m\033[1m ]\033[0m"
    INFO: str = "\033[1m[ INFO ]\033[0m"
    INPT: str = "\033[1m[ INPT ]\033[0m"
