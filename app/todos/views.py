from django.views.generic.edit import FormView

from todos.forms import TodoForm
from todos.models import Todo

class HomePageView(FormView):
    template_name = 'home.html'
    form_class = TodoForm
    success_url = '/'

    def form_valid(self, form):
        form.add_todo()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()
        return context
