import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

# --- 配置信息 ---
SMTP_SERVER = "smtp.yeah.net"  
SMTP_PORT = 465
SENDER_EMAIL = "noreply_Yuan@yeah.net"  
RECEIVER_EMAIL = "gavinchen@vip.126.com"    

SENDER_PASSWORD = os.environ.get("EMAIL_PASSWORD")

def read_email_content():
    """读取同目录下的 email.txt 文件内容"""
    file_path = "email.txt"
    # 检查文件是否存在，防止程序崩溃
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print("⚠️ 未找到 email.txt，将使用默认内容。")
        return "默认邮件内容：文件 email.txt 不存在。"

def send_email():
    # 提取文件内容
    #body_content = read_email_content()
    
    print(f"正在读取 email.txt 并尝试通过 {SENDER_EMAIL} 发送...")
    
    # 使用从文件读取的 body_content
    message = MIMEText(body_content, "plain", "utf-8")
    
    message["From"] = f"noreply <{SENDER_EMAIL}>"
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = Header("谈心", "utf-8")

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, [RECEIVER_EMAIL], message.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print(f"发送失败，原因: {e}")

if __name__ == "__main__":
    if not SENDER_PASSWORD:
        print("❌ 未找到环境变量 EMAIL_PASSWORD，请检查 GitHub Secrets 配置！")
    else:
        send_email()
