import smtplib

user = "pytonbootcam"
passward = ""

sent_from = ""
to = ["robinufo@tlen.pl"]
subject = 'To jest treść'

email_txt = f'''
From: {sent_from}

TO wiadomość testowa

[body]
'''

try:
    server = smtplib.SMTP_SSL('smtp.wp.pl', 456)
    server.echo()
    server.login(user)
    server.sendmail(sent_from,to,email_txt)
    server.close()

except:


# NIEDOKONCZONA