import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtp_server = "smtp.qq.com"
from_addr = "1429316420@qq.com"
password = "nitawctnufyphaje"
name_data = [["Bob", "1527314384@qq.com"], ["Tom", "3274508658@qq.com"]]
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
server.login(from_addr, password)


def send_mail(name, to_addrs):
    text = "Hello, %s:\n我是佩奇，3天后我就要过生日了,我能邀请你来我家玩吗" % name
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addrs)
    msg['Subject'] = Header('python test')
    server.sendmail(from_addr, to_addrs, msg.as_string())


for msg in name_data:
    send_mail(msg[0], msg[1])
server.quit()
print("邀请函发送完成")
