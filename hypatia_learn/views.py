
from django.views import generic as views


class dashboard(views.base.TemplateView):
    template_name = 'hypatia_learn/dashboard.html'
