from django.db import models

# Create your models here.
class Task(models.Model):
    item = models.CharField(max_length=250)
    is_item_complate = models.BooleanField(default=False)
    create_at = models.TimeField(auto_now_add=True)
    update_at = models.TimeField(auto_now=True)
    def __str__(self):
        return self.item
