from django.db import models
from django.db.models import Count


class MeetingManager(models.Manager):

    def amount_meetings_job(self):
        outcome = self.values('person__job').annotate(
            amount=Count('id')
        )
        print('**************')
        print(outcome)
        return outcome