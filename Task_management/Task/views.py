from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateForm
from django.views.generic import CreateView
from django.views.generic import ListView
from .models import Create
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Create
from django.db.models import Q


# Create your views here.
class index(CreateView):
    model = Create
    form_class = CreateForm
    template_name = "Task/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context


class update(UpdateView):
    model = Create
    template_name = 'Task/update.html'
    success_url = "/"
    fields = {
        "title",
        "description",
        "due_date",
        "complete"
    }


class delete(DeleteView):
    model = Create
    success_url = "/"
    template_name = 'Task/delete.html'


class TaskSearchView(ListView):
    model = Create
    template_name = "Task/task_search.html"
    ordering = ["-due_date"]
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter based on completion status
        completion_status = self.request.GET.get("status")
        if completion_status:
            queryset = queryset.filter(complete=(completion_status == "completed"))

        # Search based on name or description
        search_query = self.request.GET.get("search")
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

        return queryset


class TaskListView(ListView):
    model = Create
    template_name = 'Task/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Create.objects.all()

        # Get the sorting parameter from the request
        sort_by = self.request.GET.get('sort_by')

        if sort_by == 'due_date':
            # Sort by due date, with recently added tasks first
            queryset = queryset.order_by('-due_date', '-created')
        elif sort_by == 'title':
            # Sort by title alphabetically
            queryset = queryset.order_by('title')

        return queryset
