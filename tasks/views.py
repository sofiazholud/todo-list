from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, Tag
from .forms import TaskForm, TagForm
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')


class TagListView(ListView):
    model = Tag
    template_name = 'tasks/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/tag_form.html'
    success_url = reverse_lazy('tag_list')

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/tag_form.html'
    success_url = reverse_lazy('tag_list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'tasks/task_confirm_delete.html'


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    template_name = 'tasks/tag_confirm_delete.html'
