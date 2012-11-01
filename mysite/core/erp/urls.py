from core.erp.views.category import views #donde estan las vistas
from django.urls import path


urlpatterns = [
	path('category/lists', views.CategoryListView.as_view(), name="category_list"),
	path('category/lists2', views.category_list, name="category_list2"),
	path('category/add', views.CategoryCreateView.as_view(), name="category_create"),

    #path('view1/', myView),
    #path('view2/', myView2),

]