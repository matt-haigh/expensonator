from tastypie.resources import ModelResource

from expensonator.models import Expense


class ExpenseResource(ModelResource):
    class Meta:
        queryset = Expense.objects.all()
        excludes = ["created", "updated"]
