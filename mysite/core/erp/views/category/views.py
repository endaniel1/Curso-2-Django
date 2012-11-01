from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from core.erp.models import Category

#para manejar vistas basada en clases
from django.views.generic import ListView,CreateView

from django.http import JsonResponse #para q los datos se de tipo json

#para manejo de decoradores
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from core.erp.forms import CategoryForm #Aqui el formulario para utilizar

"""Para la vistas basadas en funciones"""
def category_list(request):
	data = {
		"title":"Listado de Categorias",
		"categories": Category.objects.all()
	}
	return render(request,"category/lists.html", data)

"""Para la vistas basadas en clase"""
class CategoryListView(ListView):
	model = Category #modelo a utilizar
	template_name = "category/lists.html" #vista a crear

	@method_decorator(csrf_exempt)#con el decorador vemos a ver si esta loggueado
	#dispatch se ejecuta antes q todo y es mas q todo para ver si es de post o get envio y mas
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	#Metodo post para el manejo de peticiones de tipo post
	def post(self, request, *args, **kwargs):
		data = {}
		try:
			data = Category.objects.get(id=request.POST["id"]).txtJson()
		except Exception as e:
			data["error"] = str(e)

		return JsonResponse(data)

	#Cambiando aqui y agregando datos a nuestra vista
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context["title"] = "Listado de Categorias"
	    return context

#para el manejo de creaciones de formularios basados en clases
class CategoryCreateView(CreateView):
    model = Category #modelo a utilizar
    form_class = CategoryForm #formaulario a utilizar
    template_name = "category/create.html" #donde se encuentra el formulario
    success_url = reverse_lazy("category_list") #cuando haga el envio para donde va a ir dirigido
    
    #Cambiando aqui y agregando datos a nuestra vista
    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context["title"] = "Creacion una Categoria"
    	return context