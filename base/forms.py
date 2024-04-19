from django.forms import ModelForm, CharField
from .models import Room, User, Leetcode, Codechef, Codeforces
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm): 
    # create a form that inherits from UserCreationForm
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class RoomForm(ModelForm): 
    class Meta: 
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class CodechefForm(ModelForm):
    class Meta:
        model = Codechef
        fields = ['id']

class CodeforcesForm(ModelForm):
    class Meta:
        model = Codeforces
        fields = ['id']

class LeetcodeForm(ModelForm):
    class Meta:
        model = Leetcode
        fields = ['id']


class UserForm(ModelForm):
    codechef_id = CharField(max_length=255, required=False)
    codeforces_id = CharField(max_length=255, required=False)
    leetcode_id = CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['username', 'bio']

    def save(self, commit=True):
        user = super().save(commit=False)
        codechef_id = self.cleaned_data.get('codechef_id')
        codeforces_id = self.cleaned_data.get('codeforces_id')
        leetcode_id = self.cleaned_data.get('leetcode_id')

        if commit:
            user.save()

            if codechef_id:
                codechef, _ = Codechef.objects.get_or_create(user=user)
                codechef.id = codechef_id
                codechef.save()

            if codeforces_id:
                codeforces, _ = Codeforces.objects.get_or_create(user=user)
                codeforces.id = codeforces_id
                codeforces.save()

            if leetcode_id:
                leetcode, _ = Leetcode.objects.get_or_create(user=user)
                leetcode.id = leetcode_id
                leetcode.save()
            
            user.codechef = codechef
            user.codeforces = codeforces
            user.leetcode = leetcode
            user.save()

        return user