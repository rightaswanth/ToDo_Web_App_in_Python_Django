from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import TodoForm,EditTodoForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def task_list(request):
    item_list = Task.objects.order_by("-due_date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        else:
            # Form is not valid, display form errors
            messages.error(request, 'Form submission failed. Please correct the errors.')
    form = TodoForm()
    page = {
        "form": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'tasks/todolist.html', page)

def remove(request, item_id):
    item = Task.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('task')

def edit(request, item_id):
    item_edit = Task.objects.get(pk=item_id)
    if request.method == 'POST':
        form = EditTodoForm(request.POST, instance=item_edit)
        if form.is_valid():
            form.save()
            return redirect('task')  # Redirect to the todo list page after editing
    else:
        form = EditTodoForm(instance=item_edit)

    return render(request, "tasks/todolist.html", {'form':form})

def toggle_status(request, item_id):
    task = Task.objects.get(pk=item_id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect('task')
