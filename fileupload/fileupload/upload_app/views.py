from django.shortcuts import render
from django.http import HttpResponse
from .forms import FileUploadForm
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                return HttpResponse("Unsupported file format")

            data = df.to_html()  # Convert DataFrame to HTML table
            return render(request, 'upload_app/display.html', {'data': data})
    else:
        form = FileUploadForm()
    return render(request, 'upload_app/test.html', {'form': form})
