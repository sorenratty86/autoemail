import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

# --- 配置信息 ---
SMTP_SERVER = "smtp.qq.com"  # 根据你的实际邮箱修改 (如 smtp.163.com)
SMTP_PORT = 465
SENDER_EMAIL = "your_email@qq.com"  # 你的发送邮箱
RECEIVER_EMAIL = "target@example.com" # 目标接收邮箱

# 从系统环境变量获取授权码，保护密码安全
SENDER_PASSWORD = os.environ.get("EMAIL_PASSWORD")

def send_email():
    print("正在尝试发送邮件...")
    message = MIMEText("这是一封通过 GitHub Actions 定时发送的自动化邮件。", "plain", "utf-8")
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = Header("自动提醒：该开会啦！", "utf-8")

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, [RECEIVER_EMAIL], message.as_string())
        server.quit()
        print("✅ 邮件发送成功！")
    except Exception as e:
        print(f"❌ 发送失败，原因: {e}")

# 单次执行
if __name__ == "__main__":
    if not SENDER_PASSWORD:
        print("❌ 未找到环境变量 EMAIL_PASSWORD，请检查配置！")
    else:
        send_email()