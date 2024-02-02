from ..Models.models import *


class Users:

    def get_user_by_id(self, user_id):
        user = User.objects.filter(id=user_id)
        return user

    def get_user_by_phone(self, phoneNumber):
        user = User.objects.filter(phoneNumber=phoneNumber)
        return user

    def get_user_by_email(self, email):
        user = User.objects.filter(email=email)
        return user

    def save(self, user):
        user.save()


class Groups:

    def get_group_by_id(self, group_id):
        group = Group.objects.filter(id=group_id)
        return group

    def save(self, group):
        group.save()


class Expenses:

    def get_expense_by_id(self, expense_id):
        expense = Expense.objects.get(id=expense_id)
        return expense

    def get_expenses_by_group(self, group_id):
        expense = Expense.objects.filter(group=group_id)
        return expense

    def get_expense_by_user_id(self, user_id):
        expense = Expense.objects.filter(payer_id=user_id)
        return expense


    def save(self, expense):
        expense.save()



class UserExpenses:

    def get_debt_amout_by_user(self, user_id):
        user_expenses = UserExpense.objects.filter(payee=user_id)
        return user_expenses

    def get_debt_amount_by_user_group(self, group_id):
        group_expense = UserExpense.objects.filter(group=group_id)
        return group_expense

class UserGroups:

    def get_users_in_group(self, group_id):
        group = UserGroup.objects.filter(group=group_id)
        return group

    def get_group_by_user(self, user_id):
        return UserGroup.objects.filter(user=user_id)
