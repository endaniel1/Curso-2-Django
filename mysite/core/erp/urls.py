from core.erp.views import myView,myView2
from django.urls import path


urlpatterns = [

    path('view1/', myView),
    path('view2/', myView2),

]