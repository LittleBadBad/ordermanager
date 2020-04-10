from django import forms
from accounts.models import User

class orderForm(forms.Form):
    platform = forms.CharField(widget=forms.TextInput(attrs={"class": "vTextField","placeholder":""}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    unit = forms.CharField(widget=forms.TextInput(attrs={"class": "vTextField"}))
    receiver = forms.ChoiceField(widget=forms.Select(attrs={"class": "vTextField"}))
#     recivedate = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class orderitemForm(forms.Form):
        start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local',"placeholder":"开始时间"}))
        end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local',"placeholder":"结束时间"}))
        place = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "vTextField","placeholder":"地点"}))
        cause = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "vTextField","placeholder":"原因"}))
        speed_limit = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={"class": "vTextField","placeholder":"限速"}))
        speed_note = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "vTextField","placeholder":"备注"}))
        pattern = forms.CharField(required=False,widget=forms.Textarea(attrs={"class": "vTextField","placeholder":"行车方式变化",'rows':'3'}))
        device = forms.CharField(required=False,widget=forms.Textarea(attrs={"class": "vTextField","placeholder":"设备变更",'rows':'3'}))
    def __init__(self, *args, **kwargs):
        super(orderForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].choices = User.objects.filter(state=1).values_list('id','name')#valuelist