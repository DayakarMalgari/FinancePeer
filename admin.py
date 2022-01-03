from django.contrib import admin

# Register your models here.
from .models import loginTab, FinancePeerJsonTab, FinancePeerDetailsTab

# Register your models here.
admin.site.register(loginTab)
admin.site.register(FinancePeerJsonTab)
admin.site.register(FinancePeerDetailsTab)







