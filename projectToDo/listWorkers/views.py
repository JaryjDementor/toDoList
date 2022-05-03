from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.views import View

from .forms import NewWorkerForm, NewTaskForm
from .models import Workers, Employees_Task_List
from django.http import JsonResponse

def list_workers(request):
    db = Workers.objects.all()
    data = {"db": db}
    return render(request, "listWorkers/list_workers.html", context=data)

def create_new_worker(request):
    if request.method == "POST":
        form = NewWorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_workers")
    form = NewWorkerForm()
    return render(request, "listWorkers/create_new_worker.html", {"form": form})

def detail_worker(request, id_worker: int):
    db = Employees_Task_List.objects.filter(idworker=id_worker)
    form = NewTaskForm(request.POST)
    a='Task completed'
    # if form.is_valid():
    #     Employees_Task_List.objects.delete(id=db.id)
    return render(request, "listWorkers/detail_worker.html", context={'db': db,'idworker': id_worker, 'form': form, 'a':a})

def create_new_task(request, id_worker: int):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            order = form.save(commit=False)
            order.idworker = id_worker
            order.save()
            return redirect("list_workers")
    form = NewTaskForm()
    return render(request, "listWorkers/create_new_task.html", {"form": form})


class TaskList(View):
    def get(self, request):
        form = NewTaskForm()
        tasks = Employees_Task_List.objects.all()
        return render(request, "listWorkers/detail_worker_create_task.html", {'form': form, 'tasks': tasks})
    def post(self, request):
        form = NewTaskForm(request.POST)

        if form.is_valid():
            new_task = form.save()
            return JsonResponse({'task': model_to_dict(new_task)}, status=200)
        else:
            return redirect('task_list_url')



class TaskComplete(View):
    def post(self, request, id):
        task = Employees_Task_List.objects.get(id=id)
        task.completed = True
        task.save()
        return JsonResponse({'task': model_to_dict(task)}, status=200)

class TaskDelete(View):
    def post(self, request, id):
        task = Employees_Task_List.objects.get(id=id)
        task.delete()
        return JsonResponse({'result': 'ok'}, status=200)


