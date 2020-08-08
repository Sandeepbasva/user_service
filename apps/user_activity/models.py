from django.db import models

# Create your models here.


class User(models.Model):
    """ User Model"""
    id = models.CharField(primary_key=True, editable=False, max_length=10)
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=32, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        if not self.id:
            count = User.objects.count()
            max_id = count + 1 if count else 1
            self.id = "{}{:08d}".format('WA', max_id)
        super().save(*kwargs)

    def __str__(self):
        return self.id


class ActivityPeriod(models.Model):
    """User activity Model"""
    user = models.ForeignKey(User, null=True)
    start_time = models.DateTimeField(null=True, default=None)
    end_time = models.DateTimeField(null=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
