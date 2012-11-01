from django.forms import ModelForm #clase para crear los formulario
from core.erp.models import Category #modelo q se va utilizar

#Clase a crear para el formulario
class CategoryForm(ModelForm):
	#aqui lso metas son los datos a utilizar para crear en el formulario
    class Meta:
        model = Category
        fields = '__all__'