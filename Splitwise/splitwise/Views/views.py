from django.views import View
from django.http import HttpResponse

from ..Services.settle_up_service import *
from ..Exceptions import *

class ExpenseView(View):

    def __init__(self):
        self.settleUpService = SettleUp()


    def settleUpUser(self, user_id):
        try:
            total = self.settleUpService.user_total(user_id)
            #  add transaction and change the status to completed in UserExpense
            pass
        except Exception as e:
            raise e

    def settleUpGroup(self, group_id):
        try:
            total = self.settleUpService.group_total(group_id)
            #  add transaction and change the status to completed in UserExpense
            pass
        except Exception as e:
            raise e



