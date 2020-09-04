from django.forms import * #clase para crear los formulario
from core.erp.models import Category #modelo q se va utilizar

#Clase a crear para el formulario
class CategoryForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#for form in self.visible_fields():
		#	form.field.widget.attrs["class"] = "form-control"
		#	form.field.widget.attrs["autocomplete"] = "off"
		#self.fields["name"].widget.attrs["autofocus"] = True

	#aqui lso metas son los datos a utilizar para crear en el formulario
	class Meta:
		model = Category #modelo a utilizar
		fields = '__all__' #datos a utilizar para nuestro formulario basandonos en el modelo aqui con __all__ son todos
		widgets = {
			"name": TextInput(
				attrs = {
					"placeholder" : "Ingrese el nombre",
				}
			),
			"desc": Textarea(
				attrs = {
					"placeholder" : "Ingrese el nombre",
					"rows": 3,
					"cols": 3
				}
			)
		}

	def save(self, commit=True):
		data = {}
		form = super()
		try:
			if form.is_valid():
				form.save()
			else:
				data['error'] = form.errors
		except Exception as e:
			data['error'] = str(e)
	
		return data