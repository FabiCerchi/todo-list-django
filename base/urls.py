from django.urls import path
from .views import TaskList, TaskDetail, TaskForm, TaskUpdate, TaskDelete, Login, SignUp
from django.contrib.auth.views import LogoutView
urlpatterns = [
               path('signup/', SignUp.as_view(), name='signup'),
               path('login/', Login.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('', TaskList.as_view(), name="tasks"),
               path('task/<int:pk>', TaskDetail.as_view(), name="task-detail"),
               path('create-task/', TaskForm.as_view(), name="task-form" ),
               path('update-task/<int:pk>', TaskUpdate.as_view(), name="task-update" ),
               path('delete-task/<int:pk>', TaskDelete.as_view(), name="task-delete" ),
]