from faker import Faker

fake = Faker(['pl_PL'])


class BaseContact:
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return f'{self.name} {self.surname} {self.phone_number} {self.email}'

    def contact(self):
        print('Wybieram numer {} i dzwonię do {} {}'
              .format(self.phone_number, self.name, self.surname))

    @property
    def label_length(self):
        return len(self.name + self.surname) + 1


class BusinessContact(BaseContact):
    def __init__(self, job, company, job_phone_number, *args):
        super().__init__(*args)
        super().label_length
        self.job = job
        self.company = company
        self.job_phone_number = job_phone_number

    def contact(self):
        print('Wybieram numer {} i dzwonię do {} {}'
              .format(self.job_phone_number, self.name, self.surname))


def base_data():
    fullname = fake.name()
    name = fullname.split()[0] if len(fullname.split()) == 2 \
        else fullname.split()[1]
    surname = fullname.split()[1] if len(fullname.split()) == 2 \
        else fullname.split()[2]
    pho_num = fake.phone_number()
    email = fake.email()
    return (name, surname, pho_num, email)


def business_data():
    job = fake.job()
    company = fake.company()
    job_pho_num = fake.phone_number()
    args = tuple([i for i in locals().values()])
    return args


def create_contacts(type_of: str, how_many: int) -> list:
    """Created list of business contacts

    Args:
        type_of (str): Two possible types: simple, business
        how_many (int): specifies the quantity
    """
    if isinstance(how_many, int):
        pass
    else:
        print('Improper type attribute, try intiger')
        return []

    if type_of in ['simple', 'business']:
        pass
    else:
        print('Improper type attribute, try: simple or business')
        return []

    list_of_cards = []
    for i in range(how_many):
        if type_of == 'simple':
            list_of_cards.append(base_data())
        elif type_of == 'business':
            list_of_cards.append(business_data() + base_data())
    return list_of_cards


if __name__ == '__main__':
    type_of = input("Podaj typ wizytówki - simple lub business: ")
    how_many = int(input("Wprowadź liczbę wizytówek: "))
    contacts = create_contacts(type_of, how_many)

    for contact in contacts:
        if contacts == []:
            break
        if type_of == 'simple':
            b_card = BaseContact(*contact)
            b_card.contact()
        if type_of == 'business':
            b_card = BusinessContact(*contact)
            b_card.contact()
