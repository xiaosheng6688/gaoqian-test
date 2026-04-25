import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 提取微信收款码base64
wx_match = re.search(r"wechatQrUrl: '([^']+)'", html)
ali_match = re.search(r"alipayQrUrl: '([^']+)'", html)

wx_b64 = wx_match.group(1) if wx_match else ''
ali_b64 = ali_match.group(1) if ali_match else ''

print(f'WX base64 length: {len(wx_b64)}')
print(f'ALI base64 length: {len(ali_b64)}')

# 保存base64到单独文件，方便上传图床
with open('wx_qr_base64.txt', 'w') as f:
    f.write(wx_b64)
with open('ali_qr_base64.txt', 'w') as f:
    f.write(ali_b64)

print('Base64已保存到 wx_qr_base64.txt 和 ali_qr_base64.txt')
print('请上传到图床后，把外链地址发给我')
