from django.contrib import admin
from WebModel.models import Blog, Contact, Tag


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register([Blog, Tag])


