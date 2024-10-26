
from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_my,name='all_my'),
    path('<int:my_id>/',views.my_detail,name='my_detail'),
    path('my_stores/',views.my_store_view,name='chai_stores'),
   
]