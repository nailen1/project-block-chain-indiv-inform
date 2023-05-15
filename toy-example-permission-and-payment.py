from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        # hash function
        return ...


class Blockchain:
    def __init__(self):
        self.chain = [Block(datetime.now(), "Genesis Block", "0")]

    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        new_block = Block(datetime.now(), data, previous_hash)
        self.chain.append(new_block)

    def get_chain(self):
        return self.chain


class PersonalData:
    def __init__(self, owner):
        self.owner = owner
        self.permission_list = []
        self.blockchain = Blockchain()

    def grant_permission(self, requester, fee):
        self.permission_list.append(requester)
        data = "Permission granted to " + \
            requester + " with fee of " + str(fee)
        self.blockchain.add_block(data)

    def check_permission(self, requester):
        return requester in self.permission_list

    def get_chain(self):
        return self.blockchain.get_chain()


class Company:
    def __init__(self, name):
        self.name = name

    def request_permission(self, data_owner, fee):
        if data_owner.check_permission(self.name):
            data_owner.blockchain.add_block("Data accessed by " + self.name)
            return True, "Permission granted and fee paid"
        else:
            return False, "Permission not granted"


daniel = PersonalData("Daniel")
naver = Company("Naver")

daniel.grant_permission(naver.name, 1000)

result, message = naver.request_permission(daniel, 1000)
if result:
    print("Permission granted and fee paid")
else:
    print("Permission not granted")
