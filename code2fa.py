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
code_2fa('OIT5FDF4K5P3GVDJKZQ4MFMPYYBPKLAX')
# Kết quả : 378542

