from django.urls import path
from api import views

urlpatterns= [
    path('',views.EmployeeListView.as_view(),name='employeeListView'),
    path('api/employees/<int:pk>',views.EmployeeDetailView.as_view(),name='employeeDetailView'),
    path('on/',views.turn_on,name='turn_on'),
    path('off/',views.turn_off,name='turn_off'),
    # path("ee/<int:id>",views.relay_data_dimmer,)
      
]

