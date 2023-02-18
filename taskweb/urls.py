from django.urls import path
from taskweb import views
urlpatterns=[
path("signup",views.SignUpView.as_view(),name="register"),
path("",views.LoginView.as_view(),name="signin"),
path("home",views.IndexView.as_view(),name="home"),
path("Task/add/",views.TaskCreateView.as_view(),name="task-add"),
path("Task/all",views.TaskListView.as_view(),name="task-list"),
path("Task/details/<int:id>",views.TaskDetailView.as_view(),name="task-detail"),

path("Task/remove/<int:id>",views.TaskDeleteView.as_view(),name="task-delete"),
path("Task/<int:id>/change",views.TaskEditView.as_view(),name="task-edit"),
path("signout",views.LogoutView.as_view(),name="signout")
]