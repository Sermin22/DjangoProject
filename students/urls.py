from django.urls import path
from . import views
from students.views import StudentCreateView, StudentUpdateView, StudentDeleteView

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    path('mymodel/', views.MyModelListView.as_view(), name='mymodel_list'),
    path('mymodel/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/<int:pk>/', views.MyModelDetailView.as_view(), name='mymodel_detail'),
    path('mymodel/update/<int:pk>/', views.MyModelUpdateView.as_view(), name='mymodel_update'),
    path('mymodel/delete/<int:pk>/', views.MyModelDeleteView.as_view(), name='mymodel_delete'),
]

# urlpatterns = [
#     path('show_data/', views.show_data, name='show_data'),
#     path('submit_data/', views.submit_data, name='submit_data'),
#     path('item/<int:item_id>/', views.show_item, name='show_item'),
#     path('list/', views.students_list, name='list')
# ]

