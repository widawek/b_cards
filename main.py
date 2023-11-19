from faker import Faker

fake = Faker(['pl_PL'])


class BaseContact:
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email


def one_card_data():
    fullname = fake.name()
    name = fullname.split()[0] if len(fullname.split()) == 2 \
        else fullname.split()[1]
    surname = fullname.split()[1] if len(fullname.split()) == 2 \
        else fullname.split()[2]
    pho_num = fake.phone_number()
    email = fake.email()
    return (name, surname, pho_num, email)


if __name__ == '__main__':
    bussiness_card = BaseContact(*one_card_data())
    bussiness_card.print_card()
