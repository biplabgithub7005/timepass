from django.shortcuts import render
from .models import FileUpload
# Create your views here.

def show_pdf(request):
    file =FileUpload.objects.all().order_by('-id')
    context ={
        'pdf':file
    }
    return render(request,'pdf/show-pdf.html',context)