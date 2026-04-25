import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 找到CONFIG部分，替换收款码为CDN链接
wx_cdn = "https://cdn.jsdelivr.net/gh/xiaosheng6688/gaoqian-test@master/wx_pay.jpg"
ali_cdn = "https://cdn.jsdelivr.net/gh/xiaosheng6688/gaoqian-test@master/ali_pay.png"

# 方法：直接找到CONFIG块，替换整个wechatQrUrl和alipayQrUrl行
config_start = html.find('const CONFIG = {')
config_end = html.find('};', config_start) + 2

old_config = html[config_start:config_end]

# 提取其他配置项
wechat_id = re.search(r"wechatId: '([^']+)'", old_config)
wechat_id = wechat_id.group(1) if wechat_id else 'z6ys8866'

vip_key = re.search(r"vipKey: '([^']+)'", old_config)
vip_key = vip_key.group(1) if vip_key else 'SBTI2026VIP'

price = re.search(r"price: ([0-9.]+)", old_config)
price = price.group(1) if price else '5.9'

new_config = f"""const CONFIG = {{
  wechatId: '{wechat_id}',
  wechatQrUrl: '{wx_cdn}',
  alipayQrUrl: '{ali_cdn}',
  price: {price},
  vipKey: '{vip_key}'
}};"""

html = html[:config_start] + new_config + html[config_end:]

# 删除所有base64数据（data:image后面的长字符串）
# 但保留CONFIG中的（已经替换掉了）
# 检查是否还有残留的base64
base64_count = len(re.findall(r'data:image/[^;]+;base64,', html))
print(f'剩余base64引用数: {base64_count}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import os
size = os.path.getsize('index.html')
print(f'文件大小: {size/1024:.1f} KB')
print('完成！')
