OneToOneField in the same form
================================

**What this do?**

Allows to update OneToOneField relation in the same form.

Issues
''''''''

A lot of issues unkown, is not tested, is just and idea with code.

* If I use RelToParentFrom in onetooneForm/forms.py works ok, but I wanted something like in onetooneForm/forms_wanted.py
* No way to sort fields



How is work
''''''''''''

See onetooneForm/models.py.

Basically in models I have model RelToParent with one OneToOne relation call parent to Parent.

** Admin View **

.. code: python

	from django.contrib import admin
	from onetooneForm.forms import RelToParentFrom
	from onetooneForm.models import RelToParent

	class ReltoParentAdmin(admin.ModelAdmin):
		form = RelToParentFrom
		# I want this order, so the issue is here
		#fields = ['name', 'attr', 'attr2']
        

	admin.site.register(RelToParent, ReltoParentAdmin)

** RelToParentFrom **

See onetooneForm/forms.py, but my experected way is like

.. code: python

	
	class RelToParentFrom(OnetoOneForm):
		class Meta:
		    model = RelToParent
		    fields = '__all__'
		    onetoone_model = 'parent'
		    exclude = ['parent']




