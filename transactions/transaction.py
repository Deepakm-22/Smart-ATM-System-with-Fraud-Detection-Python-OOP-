import datetime
class Transaction:
    def __init__(self,t_type,amount):
        self.t_type=t_type
        self.amount=amount
        self.timestamp=datetime.datetime.now()
        
    def __str__(self):
        return f"{self.t_type} | {self.amount} | {self.timestamp}"