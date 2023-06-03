from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.BookListView.as_view(), name='index2'),
    path('api/', views.BookListAPIView.as_view()),
    path('my_tasks/', views.my_tasks, name='my-tasks'),
    path('add-task/', views.add_task, name='add-task'),
    path('delete-task/<int:pk>', views.delete_task, name='delete-task'),
    path('search-task/', views.search_task, name='search-task'),
    path('colors1/', views.colors1, name='colors1'),
    path('colors2/', views.colors2, name='colors2'),
    path('fade_out_demo/', views.fade_out_demo, name='fade-out-demo'),
    path('shit/', views.shit, name='shit'),

]
