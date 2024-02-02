from ..Models.models import *


class Simplify:
    def __init__(self):
        self.transaction = {}

    def simplify_debts(self, group_id):
        total_group_amount = UserExpense.object.filter(group=group_id, status=PENDING)

        while total_group_amount:
            current_debt = total_group_amount.pop(0)
            payee = current_debt['payee']
            payer = current_debt['payer']
            amount = current_debt['amount']
            matching_debt = next((d for d in total_group_amount if d['payee'] == payer and d['payer'] == payee), None)

            if matching_debt:
                offset_amount = min(amount, matching_debt['amount'])
                self.transaction.append({'from_user': payee, 'to_user': payer, 'amount': offset_amount})
                current_debt['amount'] -= offset_amount
                matching_debt['amount'] -= offset_amount
                if current_debt['amount'] == 0:
                    total_group_amount.remove(current_debt)
                if matching_debt['amount'] == 0:
                    total_group_amount.remove(matching_debt)

        return self.transaction
