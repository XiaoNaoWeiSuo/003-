import requests

while True:
    word = input("003:")
    rnieq = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + word)
    req.encoding = 'utf-8'
    #print('返回结果: %s' % req.json())
    print('AI: %s' % req.json()['content'])