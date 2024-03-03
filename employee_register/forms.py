from django import forms
from .models import Employee,Position

class EmployeeForm(forms.ModelForm):
    position = forms.ModelChoiceField(queryset=Position.objects.all())

    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ['fullname','mobile','emp_code','position']
        labels= {
            'fullname':"full Name",
            'emp_code': "EMP_code"
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="select"
        self.fields['emp_code'].required = False

