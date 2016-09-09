# encoding: utf-8

'''
Free as freedom will be 9/9/2016

@author: luisza
'''

from __future__ import unicode_literals
from django.utils import six
from django import forms
from onetooneForm.models import RelToParent


class OneToOneFormMetaClass(forms.models.ModelFormMetaclass):

    def __new__(cls, name, bases, attrs):
        new_class = super(OneToOneFormMetaClass, cls).__new__(
            cls, name, bases, attrs)

        if 'Meta' not in attrs:
            return new_class
        else:
            meta = attrs['Meta']

        opts = forms.models.ModelFormOptions(getattr(new_class, 'Meta', None))
        fields = None
        if hasattr(meta, "extra_onetoone_fields"):
            fields = meta.extra_onetoone_fields

        rel_field = getattr(opts.model, meta.onetoone_model).field
        model = rel_field.rel.to

        # FIXME: Improve needed, a lot of fields are not contempled
        extra_fields = forms.models.fields_for_model(
            model,
            fields=fields)
        new_class.base_fields.update(extra_fields)

        info = {
            'model_name': meta.onetoone_model,
            'model': model,
            'fields':  [field for field in extra_fields]
        }
        setattr(new_class, 'onetoone_info', info)
        return new_class


class OnetoOneForm(six.with_metaclass(OneToOneFormMetaClass,
                                      forms.models.BaseModelForm)):

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs and kwargs['instance']:
            instance = kwargs['instance']
            initial = {}
            rel_instance = getattr(instance,
                                   self.onetoone_info['model_name'])
            for field in self.onetoone_info['fields']:
                initial[field] = getattr(rel_instance, field)

                if 'initial' in kwargs:
                    kwargs['initial'].update(initial)
                else:
                    kwargs['initial'] = initial
        super(OnetoOneForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):

        if hasattr(self.instance, self.onetoone_info['model_name']):
            for field in self.onetoone_info['fields']:
                rel_instance = getattr(self.instance,
                                       self.onetoone_info['model_name'])
                setattr(rel_instance, field, self.cleaned_data[field])
                rel_instance.save()

        else:
            fields_filled = {}

            for field in self.onetoone_info['fields']:
                fields_filled[field] = self.cleaned_data[field]
            setattr(self.instance, self.onetoone_info['model_name'],
                    self.onetoone_info['model'].objects.create(**fields_filled))

        return super(OnetoOneForm, self).save(commit=commit)


class RelToParentFrom(OnetoOneForm):

    class Meta:
        model = RelToParent
        fields = '__all__'
        onetoone_model = 'parent'
        exclude = ['parent']
