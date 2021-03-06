from tastypie.authorization import Authorization
from tastypie.fields import CharField
from tastypie.resources import ModelResource

from expensonator.models import Expense


class ExpenseResource(ModelResource):
    tags = CharField()

    def dehydrate_tags(self, bundle):
        return bundle.obj.tags_as_string()

    def save(self, bundle, skip_errors=False):
        bundle = super(ExpenseResource, self).save(bundle, skip_errors)
        if "tags" in bundle.data:
            bundle.obj.reset_tags_from_string(bundle.data["tags"])
        return bundle

    class Meta:
        queryset = Expense.objects.all()
        always_return_data = True
        excludes = ["created", "updated"]
        # WARNING: Tastypie docs say that this is VERY INSECURE!
        # For development only!
        authorization = Authorization()
