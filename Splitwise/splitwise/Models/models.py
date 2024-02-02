
from django.db.models import *
from django.db import models


PENDING = "PENDING"
COMPLETED = "COMPLETED"

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=255)
    phoneNumber = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=255)


class Group(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    simplified = models.BooleanField(default=False)


class Expense(BaseModel):
    description = models.CharField(max_length=255)
    payer_id = models.ForeignKey(User, on_delete=models.Protect)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    amount = models.FloatField()


class UserExpense(BaseModel):

    expense = models.ForeignKey(Expense, on_delete=models.Protect)
    payer = models.ForeignKey(User, on_delete=models.Protect)
    amount = models.IntegerField()
    payee = models.ForeignKey(User, on_delete=models.Protect)
    group = models.ForeignKey(Group, on_delete=models.Protect)
    status = models.CharField()

class UserGroup(BaseModel):
    user = models.ForeignKey(User, on_delete=models.Protect)
    group = models.ForeignKey(Group, on_delete=models.Protect)

