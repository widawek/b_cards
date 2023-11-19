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


class BusinessContact(BaseContact):
    def __init__(self, job, company, job_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
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


if __name__ == '__main__':
    business_contact = BusinessContact(*base_data(), *business_data())
    business_contact.contact()
