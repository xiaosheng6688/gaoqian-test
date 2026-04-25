import base64

with open(r'D:\微信收款码.jpg', 'rb') as f:
    wx_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()

with open(r'D:\支付宝收款码.jpg', 'rb') as f:
    ali_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

with open(r'index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("'WX_QR_PLACEHOLDER'", repr(wx_b64))
html = html.replace("'ALI_QR_PLACEHOLDER'", repr(ali_b64))

with open(r'index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('OK! WX:', len(wx_b64), 'ALI:', len(ali_b64))
