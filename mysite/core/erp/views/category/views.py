from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from core.erp.models import Category

#para manejar vistas basada en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.http import JsonResponse, HttpResponseRedirect #para q los datos se de tipo json

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
		#para captar los errores 
		try:
			data = Category.objects.get(id=request.POST["id"]).txtJson()#Buscamos la categoria y llamamos los datos de metodo q creamos
		except Exception as e:
			data["error"] = str(e) #Aqui tranformamos los errores en formato string

		return JsonResponse(data) #Retornamos los tados tipo json porque estamos utilizando Ajax

	#Cambiando aqui y agregando datos a nuestra vista
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context["title"] = "Listado de Categorias"
	    context["create_url"] = reverse_lazy("category_create")
	    context["list_url"] = reverse_lazy("category_list")
	    context["entity"] = "Categorias"
	    return context

#para el manejo de creaciones de formularios basados en clases
class CategoryCreateView(CreateView):
    model = Category #modelo a utilizar
    form_class = CategoryForm #formaulario a utilizar
    template_name = "category/create.html" #donde se encuentra el formulario
    success_url = reverse_lazy("category_list") #cuando haga el envio para donde va a ir dirigido

    #Metodo post para el manejo de peticiones de tipo post mediant ajax
    def post(self, request, *args, **kwargs):
    	data = {}
    	#para captar los errores 
    	try:
    		action = request.POST["action"]
    		if action == 'add':
    			#form = CategoryForm(request.POST)
    			form = self.get_form()
    			data = form.save()
    		else:
    			data["error"] = "No aingresado a ninguna opcion"

    	except Exception as e:
    		data["error"] = str(e) #Aqui tranformamos los errores en formato string


    	return JsonResponse(data) #Retornamos los tados tipo json porque estamos utilizando Ajax


    #Metodo post para el manejo de peticiones de tipo post
    #def post(self, request, *args, **kwargs):
    #	print(request.POST)
    #	form = CategoryForm(request.POST)
    #	if form.is_valid():
    #		form.save()
    #		return HttpResponseRedirect(self.success_url)

    #	self.object = None
    #	context = self.get_context_data(**kwargs)
    #	context["form"] = form

    #	return render(request,self.template_name,context)

    #Cambiando aqui y agregando datos a nuestra vista
    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context["title"] = "Creacion una Categoria"
    	context["entity"] = "Categorias"
    	context["list_url"] = reverse_lazy("category_list")
    	context["action"] = "add"
    	return context

class CategoryUpdateView(UpdateView):
    model = Category #modelo a utilizar
    form_class = CategoryForm #formaulario a utilizar
    template_name = "category/create.html" #donde se encuentra el formulario
    success_url = reverse_lazy("category_list") #cuando haga el envio para donde va a ir dirigido

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    #Metodo post para el manejo de peticiones de tipo post mediant ajax
    def post(self, request, *args, **kwargs):
        data = {}
        #para captar los errores 
        try:
            action = request.POST["action"]
            if action == 'edit':
                #form = CategoryForm(request.POST)
                form = self.get_form()
                data = form.save()
            else:
                data["error"] = "No aingresado a ninguna opcion"

        except Exception as e:
            data["error"] = str(e) #Aqui tranformamos los errores en formato string


        return JsonResponse(data) #Retornamos los tados tipo json porque estamos utilizando Ajax

    #Cambiando aqui y agregando datos a nuestra vista
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edicion una Categoria"
        context["entity"] = "Categorias"
        context["list_url"] = reverse_lazy("category_list")
        context["action"] = "edit"
        return context

"""docstring for DeleteView"""
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/delete.html"
    success_url = reverse_lazy("category_list")

    #Cambiando aqui y agregando datos a nuestra vista
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminacion de una Categoria"
        context["entity"] = "Categorias"
        context["list_url"] = reverse_lazy("category_list")
        return context
