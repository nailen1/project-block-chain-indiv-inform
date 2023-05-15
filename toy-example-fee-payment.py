class PersonalData:
    def __init__(self, owner, data):
        self.owner = owner
        self.data = data
        self.history = []

    def authorize(self, company_name, contract_amount):
        self.history.append(
            {"company": company_name, "amount": contract_amount})
        self.owner.receive_payment(contract_amount)


class Person:
    def __init__(self, name):
        self.name = name
        self.data = {}

    def add_personal_data(self, data_name, data):
        self.data[data_name] = PersonalData(self, data)

    def receive_payment(self, amount):
        pass


class Company:
    def __init__(self, name, contract_amount):
        self.name = name
        self.contract_amount = contract_amount

    def request_data_authorization(self, person, data_name):
        person_data = person.data.get(data_name)
        if person_data:
            person_data.authorize(self.name, self.contract_amount)
