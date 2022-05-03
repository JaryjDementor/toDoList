from django.urls import path

from .views import list_workers, create_new_worker, detail_worker, create_new_task, TaskList, TaskComplete,TaskDelete

urlpatterns = [
    path("list-workers", list_workers, name="list_workers"),
    path("create-new-worker", create_new_worker, name="create_new_worker"),
    path("<int:id_worker>/detail-worker", detail_worker, name="detail_worker"),
    path("<int:id_worker>/create-new-task", create_new_task, name="create_new_task"),
    path('', TaskList.as_view(), name='task_list_url'),
    path('<str:id>/completed/', TaskComplete.as_view(), name='task_complete_url'),
    path('<str:id>/delete/', TaskDelete.as_view(), name='task_delete_url'),
]