from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from worker.models import Worker
from worker.forms import WorkerEditForm, WorkerAddForm



class WorkerView(View):
    def get(self, request):
        workers = Worker.objects.all()
        return render(request, 'worker/workers_list.html', {'workers': workers})

def worker_detail(request, pk):
    worker_object = Worker.objects.get(pk=pk)
    return render(
        request,
        'worker/worker_detail.html',
        {'worker_object': worker_object}
    )

def worker_edit(request, pk):
    worker_object = Worker.objects.get(pk=pk)

    if request.method == "GET":
        form = WorkerEditForm(instance=worker_object)
        return render(request, "worker/worker_edit.html", {"form": form})

    elif request.method == "POST":
        form = WorkerEditForm(data=request.POST, instance=worker_object)
        if form.is_valid():
            object = form.save()
            return redirect(worker_detail, pk=object.pk)
        else:
            return HttpResponse("Форма не валидна")


def worker_add_form(request):
    if request.method == "POST":
        form = WorkerAddForm(request.POST)
        if form.is_valid():
            new_worker = form.save()
            return redirect(f'/worker/{new_worker.id}/')
    worker_form = WorkerAddForm()
    return render(
        request,
        'worker/worker_form.html',
        {"worker_form": worker_form}
    )