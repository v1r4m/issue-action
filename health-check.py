import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# 발신자 이메일 주소와 비밀번호
sender_email = "choyoungisdead@gmail.com"
sender_password = "koup smix cezy dwjj"

# 수신자 이메일 주소
receiver_email = os.environ['TOKEN']

# SMTP 서버 정보 (Gmail 사용 예시)
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Gmail의 경우 SSL을 사용하지 않으므로 587 포트를 사용합니다.

def sendMail(title, b):
    # 이메일 내용 설정
    subject = title
    body = b

    # 이메일 메시지 설정
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # SMTP 서버 연결 및 이메일 전송
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # TLS 암호화 연결을 시작합니다.
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("이메일이 성공적으로 전송되었습니다.")
        #time.sleep(300)
    except Exception as e:
        print("이메일 전송 중 오류가 발생했습니다:", str(e))
response = requests.get('https://diary-two.vercel.app/')
if response.status_code != 200:
    #send alarm
    sendMail("서버가 다운되었습니다.", "서버가 다운되었습니다.")
    