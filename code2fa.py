import requests
def code_2fa(code):
    abc = requests.get('http://get2fa.ml/2fa.php?key='+code)
    htmltext = abc.text
    htmltext = htmltext.splitlines()
    htmltext = htmltext[4]
    code = htmltext[56:]
    code = code[:6]
    print(code)
    return code
code_2fa('xxxx') # xxxx là mã code 2fa
