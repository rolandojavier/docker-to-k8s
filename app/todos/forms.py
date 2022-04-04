from django.forms import ModelForm

from todos.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['description']

    def add_todo(self):
        t = Todo(description=self.cleaned_data['description'])
        t.save()
