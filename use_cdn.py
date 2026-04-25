import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 把base64收款码替换成jsDelivr CDN外链
# jsDelivr格式: https://cdn.jsdelivr.net/gh/用户名/仓库名@分支名/文件路径

wx_cdn = "https://cdn.jsdelivr.net/gh/xiaosheng6688/gaoqian-test@master/wx_pay.jpg"
ali_cdn = "https://cdn.jsdelivr.net/gh/xiaosheng6688/gaoqian-test@master/ali_pay.png"

# 替换微信收款码base64
wx_pattern = r"wechatQrUrl: 'data:image/jpeg;base64,[^']*'"
html = re.sub(wx_pattern, f"wechatQrUrl: '{wx_cdn}'", html)

# 替换支付宝收款码base64  
ali_pattern = r"alipayQrUrl: 'data:image/png;base64,[^']*'"
html = re.sub(ali_pattern, f"alipayQrUrl: '{ali_cdn}'", html)

# 如果上面没匹配到（可能是双引号），再试一次
wx_pattern2 = r'wechatQrUrl: "data:image/jpeg;base64,[^"]*"'
html = re.sub(wx_pattern2, f'wechatQrUrl: "{wx_cdn}"', html)

ali_pattern2 = r'alipayQrUrl: "data:image/png;base64,[^"]*"'
html = re.sub(ali_pattern2, f'alipayQrUrl: "{ali_cdn}"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('已替换为CDN外链！')
print(f'微信: {wx_cdn}')
print(f'支付宝: {ali_cdn}')

# 检查文件大小
import os
size = os.path.getsize('index.html')
print(f'文件大小: {size/1024:.1f} KB')
