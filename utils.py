import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def index(email,username,cur_date,order_id,address,phnNo,items):
    print(items)
    try:
        body=f'''
        Subject: Confirmation of Your Hair Products Purchase

        Dear {username},

        I'm excited to inform you that your recent purchase of hair products has been successfully processed and is on its way to you. We appreciate your business and wanted to confirm the details of your purchase:

        Order Confirmation:
        - Order Number: {order_id}
        - Date of Purchase: {cur_date}
        - Address : {address}
        - Contact : {phnNo}

        Purchased Items:

        {items}

        Thank you for choosing tres Beaux for your hair care needs. 
        We value your trust and look forward to serving you in the future.

        Best regards,

        {username}
        '''
        # put your email here
        sender = 'yuvibro1211@gmail.com'
        # get the password in the gmail (manage your google account, click on the avatar on the right)
        # then go to security (right) and app password (center)
        # insert the password and then choose mail and this computer and then generate
        # copy the password generated here
        password = 'tiecqtzjasbhectc'
        # put the email of the receiver here
        receiver = email

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = "Successfully registered"

        message.attach(MIMEText(body, 'plain'))
        # filen = +".pdf"
        # __location__ = os.path.realpath(
        # os.path.join(os.getcwd(), os.path.dirname(__file__)))
        # with open(os.path.join(__location__, filen),'rb') as pdf:
            # print(pdf)
            # pdfname = '/api/rank-test.pdf'

            # pdfname = open(pdf, 'rb')
            
            # payload = MIMEBase('application', 'octate-stream', Name=filen)
            # # payload = MIMEBase('application', 'pdf', Name=pdfname)
            # payload.set_payload((pdf).read())

            # enconding the binary into base64
            # encoders.encode_base64(payload)
            
            # # add header with pdf name
            # payload.add_header('Content-Decomposition', 'attachment', filename=filen)
            # message.attach(payload)

            #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)

            #enable security
        session.starttls()

            #login with mail_id and password
        session.login(sender, password)

        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')

        return True
    except Exception as e:
        print(e)
        return False