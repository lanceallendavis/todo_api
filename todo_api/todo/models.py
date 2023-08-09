from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

