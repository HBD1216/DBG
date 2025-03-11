# ngrok_setup.py
from pyngrok import ngrok, conf
import getpass

choose_port = 3423

# 输入你的ngrok token
print("从 https://dashboard.ngrok.com/get-started/your-authtoken 获取你的 auth_token：")
conf.get_default().auth_token = getpass.getpass()

# 启动ngrok隧道
public_url = ngrok.connect(choose_port).public_url
print(f"ngrok tunnel available at: {public_url} -> http://localhost:{choose_port}")

# 保持进程运行，防止脚本退出
input("按回车键（Enter）结束隧道...")
ngrok.disconnect(public_url)
