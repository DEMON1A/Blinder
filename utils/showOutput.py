from colorama import init
from termcolor import colored
import sys

def logOutput(url, code, payload):
    if str(code).startswith("20"):
        color = "green"
    elif str(code).startswith("30"):
        color = "yellow"
    elif str(code).startswith("40") or code.startswith("50"):
        color = "red"
    else:
        color = "yellow"

    init()
    messageColored = colored(f"[{code}]: {url}\t||\t{payload}", color, attrs=['bold'])
    sys.stdout.write(f"{messageColored}\n")

def errorOutput(rule, message):
    init()
    messageColored = colored(f"[{rule}]: {message}", 'red', attrs=['bold'])
    sys.stdout.write(f"{messageColored}\n")

# def goodOutput(url, code, payload):
#     init()
#     messageColored = colored(f"[{code}]: {url} | {payload}", 'green', attrs=['bold'])
#     sys.stdout.write(f"{messageColored}\n")