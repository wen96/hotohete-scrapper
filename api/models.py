from django.db import models


class Stat(models.Model):
    user_id = models.CharField(max_length=20, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    data = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.user_id, self.timestamp)
