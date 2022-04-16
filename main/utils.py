import datetime
from random import randint, uniform
import pytz

from VPN.settings import TIME_ZONE
from .models import User, Transfer


class DataGenerator:

    def __init__(self):
        self.today = datetime.datetime.now()
        self.date_before = self.today - datetime.timedelta(weeks=6*4)
        self.today_stamp = self.today.timestamp()
        self.before_stamp = self.date_before.timestamp()

    def get_date(self):
        date = datetime.datetime.fromtimestamp(uniform(self.today_stamp, self.before_stamp))
        tz = pytz.timezone(zone=TIME_ZONE)
        return tz.localize(date)

    def process(self):
        for user in User.objects.all().values_list('id', flat=True):
            transfers = [Transfer(user_id=user,
                                  date=self.get_date(),
                                  traffic=randint(10, 100)) for _ in range(50, randint(51, 500))]
            Transfer.objects.bulk_create(objs=transfers, batch_size=500, ignore_conflicts=True)
