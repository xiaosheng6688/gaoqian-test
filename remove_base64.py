import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 找到所有base64数据（长度超过100的）
matches = list(re.finditer(r'data:image/[^;]+;base64,[A-Za-z0-9+/=]{100,}', html))
print(f'找到 {len(matches)} 处base64数据')

# 从后往前删除，避免位置偏移
for m in reversed(matches):
    start = m.start()
    end = m.end()
    html = html[:start] + html[end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import os
size = os.path.getsize('index.html')
print(f'文件大小: {size/1024:.1f} KB')
print('完成！')
