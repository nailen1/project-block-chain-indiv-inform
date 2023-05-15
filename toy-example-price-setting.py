from datetime import datetime


class PersonalData:
    def __init__(self, owner):
        self.owner = owner
        self.history = []

    def add_data_usage(self, company, fee):
        usage_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        usage_record = {"company": company, "fee": fee, "time": usage_time}
        self.history.append(usage_record)
        print(
            f"{company} used {self.owner}'s data with fee of {fee} won at {usage_time}.")


daniel_data = PersonalData("Daniel")

naver_fee = 5000

daniel_data.add_data_usage("Naver", naver_fee)
