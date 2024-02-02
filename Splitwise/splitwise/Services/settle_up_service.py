from ..Repository.repo import *
from ..Utils.util import *


class SettleUp:

    def __init__(self):
        self.user_expense = UserExpenses()
        self.expense = Expenses()

    def user_total(self, user_id):
        owed = self.expense.get_expense_by_user_id(user_id) # total - owed from all users
        owes = self.user_expense.get_debt_amout_by_user(user_id) # total - owes to users
        return owed - owes

    def group_total(self, group_id):
        simplified = Group.objects.filter(id=group_id).get("simplified")
        if simplified:
            dict_of_expense = Simplify.simplify_debts(group_id)
            return dict_of_expense
        else:
            owed = self.expense.get_expenses_by_group(group_id)
            owes = self.user_expense.get_debt_amount_by_user_group(group_id)
            return owed-owes
