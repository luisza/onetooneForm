from django.db import models

# Create your models here.


class Parent(models.Model):
    name = models.CharField(max_length=50)


class RelToParent(models.Model):
    attr1 = models.SmallIntegerField(default=10)
    attr2 = models.SmallIntegerField(default=20)
    parent = models.OneToOneField(Parent)

    def __str__(self):
        return self.parent.name