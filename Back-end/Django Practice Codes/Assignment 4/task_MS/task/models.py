from django.db import models


# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    task_description = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField()


    def __str__(self):
        return f"{'✅' if self.is_completed else ''}{self.title}!"
    
# def delete_task(req,id):


