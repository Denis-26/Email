import smtplib
import email
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(self, service=None):
        if service is None:
            raise ValueError("You must send Service object to constructor")
        self._service_address = service['url']
        self._service_port = service['port']
        self._source_address = None
        self._target_address = None
        self._smtpObj = 0
        self._message = email.mime.multipart.MIMEMultipart()

    def __del__(self):
        self._smtpObj.quit()

    def set_destination(self, source=None, target=None):
        if not isinstance(source, str) or not isinstance(target, str):
            raise TypeError('source and target must be string type')
        self._source_address = source
        self._target_address = target

    def send(self):
        return self._smtpObj.sendmail(self._source_address, self._target_address, self._message.as_string())

    def attach(self, filenames, files):
        for file, f_name in zip(files, filenames):
            att = email.mime.application.MIMEApplication(file.read(), _subtype=f_name.split('.')[1])
            att.add_header('Content-Disposition', 'attachment', filename=f_name)
            self._message.attach(att)

    def head(self, subject):
        if not isinstance(subject, str):
            raise TypeError('subject must be string type')
        self._message['Subject'] = subject
        self._message['From'] = self._source_address
        self._message['To'] = self._target_address

    def body(self, text):
        body = email.mime.text.MIMEText(text)
        self._message.attach(body)

    def connect(self, login, password):
        try:
            self._smtpObj = smtplib.SMTP(self._service_address, self._service_port)
            self._smtpObj.starttls()
            self._smtpObj.login(login, password)
        except Exception as ex:
            Logger.error("Connection error\n"+str(ex))
            return 1
