from faker import Faker
class wizytowka:
    def __init__(self, name, surname, company, position, mail, private_phone_number, official_phone_number):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.mail = mail
        self.private_phone_number = private_phone_number
        self.official_phone_number = official_phone_number
    def contact(self):
        print(f"Kontaktuje się z {self.name} {self.surname}, {self.company}, {self.position}, {self.mail}")
    def contact_base(self):
        print(f"Wybieram prywatny {self.private_phone_number} i dzwonię do {self.name} {self.surname}")
    def label_length_base(self):
        print("Długość imienia i nazwiska:", len(self.name) + len(self.surname))
    def contact_business(self):
        print(f"Wybieram służbowy {self.official_phone_number} i dzwonię do {self.name} {self.surname}")
    def label_length_business(self):
        print("Długość imienia i nazwiska:", len(self.name) + len(self.surname))
        


lista = []

lista.append(wizytowka(name="Regina",surname= "Stevenson", private_phone_number = "612 751 731", official_phone_number = "214 657 166", company = "firma: PriceRite Warehouse Club", position= "stanowisko: Dyeing machine operator", mail= "mail: ReginaSStevenson@jourrapide.com"))
lista.append(wizytowka(name="Jan",surname= "Dzban", private_phone_number = "712 681 632", official_phone_number = "912 562 125", company = "firma: Żabka", position= "stanowisko: kasjer", mail= "mail: jan.dzban@gmail.com"))
lista.append(wizytowka(name="Kacper",surname= "Nowak", private_phone_number = "511 761 222", official_phone_number = "701 512 218", company = "firma: Lidl", position= "stanowisko: szef", mail= "mail: kacper.nowak@gmail.com"))
lista.append(wizytowka(name="Michał",surname= "Supel", private_phone_number = "999 888 777", official_phone_number = "111 222 555", company = "firma: Fc Barcelona", position= "stanowisko: operator kosiarki", mail= "mail: michalsupel@gmail.com"))
lista.append(wizytowka(name="Halina",surname= "Mostowiak", private_phone_number = "777 111 222", official_phone_number = "997 998 999", company = "firma: Sheraton", position= "stanowisko: sprzątaczka", mail= "mail: halinka@gmail.com"))


name = input("Kontaktuje się z:")
for i in lista:
    if i.name == name:
        i.contact()

class BaseContact(wizytowka):
    def __init__(self, private_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.private_phone_number = private_phone_number
    

    private_phone_number = input("Wybieram ")
    for i in lista:
        if i.private_phone_number == private_phone_number:
            i.contact_base()
            i.label_length_base()
            

class BusinessContact(wizytowka):
    def __init__(self, official_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.official_phone_number = official_phone_number

    official_phone_number = input("Wybieram ")
    for i in lista:
         if i.official_phone_number == official_phone_number:
            i.contact_business()
            i.label_length_business()

amount = int(input("Ilość wizytówek:"))
type = input("Typ numeru:")
def create_contacts(type, amount):
    fake = Faker()
    lista = []
    for i in range(amount):
        lista.append(wizytowka(name = fake.first_name(), surname = fake.last_name(), private_phone_number = fake.phone_number(), official_phone_number = fake.phone_number(), company = fake.company(), position = fake.job(), mail = fake.email()))  
    for i in lista:
        if type == "private":
            i.contact_base()
        if type == "official":
            i.contact_business()
    return(lista)
function = create_contacts(type,amount)
for a in function:
    a.contact()





