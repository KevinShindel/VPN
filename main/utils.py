from datetime import datetime
from random import randint, uniform

from dateutil import relativedelta

from .models import User, Transfer


class DataGenerator:

    def __init__(self):
        self.today = datetime.now()
        self.date_before = self.today - relativedelta.relativedelta(months=6)

        self.today_stamp = self.today.timestamp()
        self.before_stamp = self.date_before.timestamp()

    def process(self):
        for user in User.objects.all():
            transfers = []
            for i in range(50, randint(51, 500)):
                transfers.append(Transfer(user=user,
                                          date=datetime.fromtimestamp(uniform(self.today_stamp, self.before_stamp)),
                                          traffic=randint(10, 100)))
            Transfer.objects.bulk_create(transfers)

