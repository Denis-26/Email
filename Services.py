class Services:
    def service(type):
        return {'url': 'smtp.gmail.com', 'port': 587} if type == 'gmail' else None
        return {'url': 'smtp.yandex.com', 'port': '465'} if type == 'yandex' else None
