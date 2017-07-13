# Email
Email module for python3


### Start
```bash
git clone https://github.com/Denis-26/Email
```

```python
from Email.Email import Email
from Email.Services import Services

file = open('way_to_file', 'rb')
service = Services.service('gmail')
mail = Email(service)
mail.connect('mymail@lala.la', 'password')
mail.set_destination('from@gmail.com', 'to@gmail.com')
mail.head('Subject Text')
mail.body('Testing my email module, all text you want')
mail.attach(['filename'], [file])                        # filename must be with extension
mail.send()
file.close()
```


# Docs

### Classes
```python 
class Service
class Email
```

### class Service
#### functions
```python
def service(type: 'gmail' | 'yandex') # return dict with info about needed service
```

### class Email
#### functions
```python
Email(service)
def connect(login: str, password: str)
def set_destination(source: str, target: str)
def head(subject: str)
def body(text: str)
def send()
```

