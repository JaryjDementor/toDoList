from django.forms import ModelForm, TextInput, Textarea, IntegerField, CharField, Select
from . import models
from django import forms
# from bootstrap_datepicker_plus import DatePickerInput


status_task= [
    ('task not complet', 'Task not complet'),
    ('task completed', 'Task completed'),
    ]

class DateInput(forms.DateInput):
    input_type = 'date'

class NewWorkerForm(ModelForm):
    class Meta:
        model = models.Workers
        fields = ["name", "surname"]

        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "name"}),
            "surname": TextInput(
                attrs={"class": "form-control", "placeholder": "surname"}
            ),
        }

class NewTaskForm(ModelForm):
    class Meta:
        model = models.Employees_Task_List
        fields = ["description", "categories", "date_of_completion"]

        widgets = {
            "description": Textarea(attrs={"class": "form-control", "placeholder": "description"}),
            "categories": TextInput(attrs={"class": "form-control", "placeholder": "categories"}),
            'date_of_completion': DateInput(),
        }
