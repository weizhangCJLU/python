import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtp_server = "smtp.qq.com"
from_addr = "1429316420@qq.com"
password = "nitawctnufyphaje"
to_addrs = "3274508658@qq.com"

text = "我的第一封邮件"
msg = MIMEText(text, 'plain', 'utf-8')
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addrs)
msg['Subject'] = Header('python test')

server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
server.login(from_addr, password)
server.sendmail(from_addr, to_addrs, msg.as_string())
print("登录邮箱成功")
server.quit()
print("退出登录")
