from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from expensonator.models import Expense


class ExpenseResource(ModelResource):
    class Meta:
        queryset = Expense.objects.all()
        excludes = ["created", "updated"]
        # WARNING: Tastypie docs say that this is VERY INSECURE!
        # For development only!
        authorization = Authorization()
