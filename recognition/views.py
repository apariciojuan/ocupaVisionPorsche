from django.shortcuts import render
from .forms import Formulario
from .testvision import StartDetec

# Create your views here.
def home_view(request):
    form = Formulario()
    data = ""
    if request.method == 'POST':
        myfile = request.FILES['foto']
        print(myfile)
        face = StartDetec(myfile)
        return render(request, 'index.html', {'form': form, 'data': face})
    else:
        return render(request, 'index.html', {'form': form, 'data': data})
