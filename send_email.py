import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header


SMTP_SERVER = "smtp.yeah.net"  
SMTP_PORT = 465
SENDER_EMAIL = "noreply_Yuan@yeah.net"  
RECEIVER_EMAIL = "vincentgalen@163.com"    


SENDER_PASSWORD = os.environ.get("EMAIL_PASSWORD")

def send_email():
    print(f"正在尝试通过 {SENDER_EMAIL} 发送邮件...")
    message = MIMEText("这是一封通过 GitHub Actions 定时发送的自动化邮件。", "plain", "utf-8")
    
    # 标准格式：发件人显示名 <邮箱地址>
    message["From"] = f"Yuan <{SENDER_EMAIL}>"
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = Header("自动提醒：该开会啦！", "utf-8")

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, [RECEIVER_EMAIL], message.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print(f"❌ 发送失败，原因: {e}")

if __name__ == "__main__":
    if not SENDER_PASSWORD:
        print("❌ 未找到环境变量 EMAIL_PASSWORD，请检查 GitHub Secrets 配置！")
    else:
        send_email()
