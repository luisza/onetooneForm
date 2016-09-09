from django.contrib import admin
from onetooneForm.forms import RelToParentFrom
from onetooneForm.models import RelToParent

# Register your models here.


class ReltoParentAdmin(admin.ModelAdmin):
    form = RelToParentFrom
    # I want this order
    #fields = ['name', 'attr', 'attr2']

admin.site.register(RelToParent, ReltoParentAdmin)
