from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail')
]

# urlpatterns = [
#     path('show_data/', views.show_data, name='show_data'),
#     path('submit_data/', views.submit_data, name='submit_data'),
#     path('item/<int:item_id>/', views.show_item, name='show_item'),
#     path('list/', views.students_list, name='list')
# ]

