from enum import Enum
from typing import List


class ExpenseType(Enum):
    EXACT = "EXACT"
    PERCENT = "PERCENT"
    EQUAL = "EQUAL"


class Expense:
    def __init__(self, amount, payer_id, payee):
        self.amount = amount
        self.payer_id = payer_id
        self.payee = payee


class ExactExpense(Expense):
    pass


class PercentSplit:
    def __init__(self, percent):
        self.percent = percent


class PercentExpense(Expense):
    pass


class EqualExpense(Expense):
    pass


class Split:
    def __init__(self):
        self.amount = 0.0


# pushing the event to message queue
def create_expense(expense_type,  amount, payer_id, payee_ids):
    for payee in payee_ids:
        if expense_type == ExpenseType.EXACT:
            return ExactExpense(amount, payer_id, payee)
        elif expense_type == ExpenseType.PERCENT:
            amount = amount * (1/len(payee_ids))
            return PercentExpense(amount, payer_id, payee)
        elif expense_type == ExpenseType.EQUAL:
            amount = amount * (1/len(payee_ids))
            return EqualExpense(amount, payer_id, payee)
        else:
            return None
