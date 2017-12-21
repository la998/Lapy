from django.contrib import admin
from WebModel.models import Blog, Contact, Tag


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    fieldsets = (['Main', {
            'fields': ('name', 'email'),
     }],
        ['Advance', {
            'classes': ('collapse', ),  # css
            'fields': ('age', ),
        }
        ]
    )
    # fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Blog, Tag])


