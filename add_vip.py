import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. 在CONFIG中添加VIP密钥（你可以修改这个密码）
old_config = '''const CONFIG = {
  wechatId: 'z6ys8866','''
new_config = '''const CONFIG = {
  wechatId: 'z6ys8866',
  vipKey: 'SBTI2026VIP', // 支付后发给用户的解锁密钥，定期更换'''  

html = html.replace(old_config, new_config)

# 2. 在支付弹窗中添加密码输入区域（在modal-steps后面）
old_steps = '''    <div class="modal-steps">
      <span>①</span> 扫码支付 ¥5.9<br>
      <span>②</span> 添加微信 <span style="color:var(--accent)">z6ys8866</span><br>
      <span>③</span> 发送支付截图 + 你的测试结果<br>
      <span>④</span> 获取你的专属分析报告 ✅
    </div>
  </div>
</div>'''

new_steps = '''    <div class="modal-steps">
      <span>①</span> 扫码支付 ¥5.9<br>
      <span>②</span> 添加微信 <span style="color:var(--accent)">z6ys8866</span><br>
      <span>③</span> 发送支付截图获取<b>解锁密钥</b><br>
      <span>④</span> 输入密钥，自动开通VIP ✅
    </div>
    <div style="margin-top:16px;border-top:1px solid rgba(255,255,255,0.1);padding-top:16px;">
      <div style="font-size:13px;color:var(--gold);margin-bottom:8px;font-weight:600;">🔑 输入解锁密钥</div>
      <input type="text" id="vipKeyInput" placeholder="请输入密钥（如：SBTI2026VIP）" style="width:100%;padding:10px 14px;background:rgba(255,255,255,0.08);border:1px solid rgba(245,166,35,0.3);border-radius:10px;color:#fff;font-size:14px;outline:none;text-align:center;">
      <button onclick="verifyVipKey()" style="width:100%;margin-top:10px;padding:10px;background:linear-gradient(135deg,var(--gold),#ff8c00);color:#fff;border:none;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;">✨ 立即解锁VIP</button>
      <div id="vipError" style="color:var(--accent);font-size:12px;margin-top:8px;display:none;">❌ 密钥错误，请确认后重试</div>
    </div>
  </div>
</div>'''

html = html.replace(old_steps, new_steps)

# 3. 在showPaywall函数后面添加verifyVipKey函数
old_func = '''function closeModal() {
  document.getElementById('modalPaywall').classList.remove('active');
}'''

new_func = '''function closeModal() {
  document.getElementById('modalPaywall').classList.remove('active');
  document.getElementById('vipError').style.display = 'none';
  document.getElementById('vipKeyInput').value = '';
}

function verifyVipKey() {
  const input = document.getElementById('vipKeyInput').value.trim();
  if (input === CONFIG.vipKey) {
    // 密钥正确，解锁VIP
    localStorage.setItem('sbti_vip_' + window._resultTest + '_' + window._resultType, '1');
    closeModal();
    showFullReport();
    showToast('🎉 VIP解锁成功！');
  } else {
    document.getElementById('vipError').style.display = 'block';
  }
}

function showFullReport() {
  // 显示完整报告内容
  const type = TEST_DATA[window._resultTest].types[window._resultType];
  const fullReport = `
    <div style="margin-top:20px;text-align:left;">
      <h3 style="color:var(--gold);font-size:16px;margin-bottom:10px;">📊 完整分析报告</h3>
      <div style="background:rgba(255,255,255,0.05);border-radius:12px;padding:16px;margin-bottom:12px;">
        <h4 style="color:var(--accent);font-size:14px;margin-bottom:8px;">🧬 人格深度解析</h4>
        <p style="font-size:13px;color:var(--text2);line-height:1.8;">
          ${type.name}型人格的你，拥有独特的${type.tags.join('、')}特质。
          在2026年，这种人格特质将帮助你抓住关键机遇。
          你的核心优势在于${type.bars['搞钱力'] > 50 ? '搞钱能力' : type.bars['社交力'] > 50 ? '人际关系' : '执行力'}，
          这是你的核心竞争力。
        </p>
      </div>
      <div style="background:rgba(255,255,255,0.05);border-radius:12px;padding:16px;margin-bottom:12px;">
        <h4 style="color:var(--accent);font-size:14px;margin-bottom:8px;">⚠️ 致命盲区</h4>
        <p style="font-size:13px;color:var(--text2);line-height:1.8;">
          需要注意${type.bars['风险值'] > 60 ? '控制风险，避免冲动决策' : type.bars['消费力'] > 60 ? '控制消费，避免过度支出' : '提升社交能力，拓展人脉'}。
          这个盲区如果不注意，可能会在2026年带来不必要的损失。
        </p>
      </div>
      <div style="background:rgba(255,255,255,0.05);border-radius:12px;padding:16px;margin-bottom:12px;">
        <h4 style="color:var(--accent);font-size:14px;margin-bottom:8px;">🎯 2026年最适合你的方向</h4>
        <p style="font-size:13px;color:var(--text2);line-height:1.8;">
          ${window._resultTest === 'money' ? '适合你的搞钱方向：副业变现、投资理财、技能变现' : window._resultTest === 'work' ? '适合你的职场方向：向上管理、技能深耕、跳槽涨薪' : '适合你的恋爱方向：主动表达、制造惊喜、深度沟通'}
        </p>
      </div>
      <div style="background:rgba(255,255,255,0.05);border-radius:12px;padding:16px;margin-bottom:12px;">
        <h4 style="color:var(--accent);font-size:14px;margin-bottom:8px;">🍀 幸运指南</h4>
        <p style="font-size:13px;color:var(--text2);line-height:1.8;">
          幸运色：${['金色','红色','紫色','蓝色','绿色'][Math.floor(Math.random()*5)]}<br>
          幸运数字：${Math.floor(Math.random()*9)+1}<br>
          幸运星座：${['狮子座','天蝎座','金牛座','双子座','水瓶座'][Math.floor(Math.random()*5)]}<br>
          幸运月份：${['3月','6月','9月','11月'][Math.floor(Math.random()*4)]}
        </p>
      </div>
      <div style="text-align:center;margin-top:16px;">
        <span style="display:inline-block;padding:6px 16px;background:rgba(81,207,102,0.15);border:1px solid rgba(81,207,102,0.3);border-radius:20px;color:#51cf66;font-size:12px;">✅ VIP报告已解锁</span>
      </div>
    </div>
  `;
  document.querySelector('.result-card').insertAdjacentHTML('beforeend', fullReport);
  // 隐藏解锁按钮
  document.querySelector('.btn-unlock').style.display = 'none';
}'''

html = html.replace(old_func, new_func)

# 4. 修改showPaywall函数，检查是否已经解锁
old_show = '''function showPaywall() {
  const modal = document.getElementById('modalPaywall');
  modal.classList.add('active');'''

new_show = '''function showPaywall() {
  // 检查是否已经解锁
  if (localStorage.getItem('sbti_vip_' + window._resultTest + '_' + window._resultType)) {
    showFullReport();
    showToast('🎉 你已解锁VIP，直接查看报告！');
    return;
  }
  const modal = document.getElementById('modalPaywall');
  modal.classList.add('active');'''

html = html.replace(old_show, new_show)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('VIP密码验证功能已添加！')
print('当前密钥：SBTI2026VIP')
print('你可以修改 CONFIG.vipKey 的值来更换密钥')
