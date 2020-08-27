import csv
import random
from faker import Faker

faker = Faker('pl_PL')


def generuj_CSV(n):
    x = set(random.sample(range(10000, 100000), k=1000))
    with open("Fake data.csv", "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(['id', 'imie i nazwisko', 'data urodzenia', 'adres', 'praca', 'nr. telefonu', 'email'])
        for id in range(n):
            imie = faker.name()
            if "pani " in imie:
                imie = imie.replace("pani ", '')
            elif "pan " in imie:
                imie = imie.replace("pan ", '')
            else:
                pass
            adres = faker.address()
            adres = adres.replace('\n', ' ')
            praca = faker.job()
            telefon = faker.phone_number()
            email = faker.email()
            data_urodzenia = faker.date_of_birth()
            id = x.pop()
            csv_writer.writerow([id, imie, data_urodzenia, adres, praca, telefon, email])

if __name__=='__main__':
    generuj_CSV(50)
