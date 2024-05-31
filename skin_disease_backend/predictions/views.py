import os
import urllib
import uuid
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .predict import predict, allowed_file
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            if allowed_file(file.name):
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                file_url = fs.url(filename)
                class_result, prob_result = predict(fs.path(filename))
                predictions = {
                    "class1": class_result[0],
                    "class2": class_result[1],
                    "class3": class_result[2],
                    "prob1": prob_result[0],
                    "prob2": prob_result[1],
                    "prob3": prob_result[2],
                }
                return render(request, 'templates/result.html', {'predictions': predictions, 'file_url': file_url})
            else:
                error = "Please upload images of jpg, jpeg, and png extension only"
        elif 'link' in request.POST:
            link = request.POST['link']
            try:
                resource = urllib.request.urlopen(link)
                unique_filename = str(uuid.uuid4()) + ".jpg"
                file_path = os.path.join('media/images', unique_filename)
                with open(file_path, 'wb') as output:
                    output.write(resource.read())
                class_result, prob_result = predict(file_path)
                predictions = {
                    "class1": class_result[0],
                    "class2": class_result[1],
                    "class3": class_result[2],
                    "prob1": prob_result[0],
                    "prob2": prob_result[1],
                    "prob3": prob_result[2],
                }
                return render(request, 'templates/result.html', {'predictions': predictions, 'file_url': file_path})
            except Exception as e:
                error = 'This image from this site is not accessible or inappropriate input'
        else:
            error = 'No file or link provided'
        return render(request, 'templates/upload.html', {'error': error})
    return render(request, '/templates/upload.html')
