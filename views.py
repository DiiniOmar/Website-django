from django.shortcuts import get_object_or_404, render, redirect
from django.http import FileResponse
from django.urls import reverse
from webapp.models import contact, ResumeModel
from .forms import DocumentForm
from django.contrib import messages
def home(request):
    resumes= ResumeModel.objects.all()
    return render(request, 'webapp/index.html',{'resumes':resumes})


#=======================================#
# This section is form submition
#=======================================#

def contactView(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Thanks, the form is been submitted successfully!")
        return redirect('contact')
        
    return render(request, 'webapp/contact.html')

#=======================================#
# This section is uploading the PDF file
#=======================================#

def Upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_save():
            form.save()
            return redirect('contact')
    else:
        form =DocumentForm()
    return render(request, 'webapp/upload_document.html',{'form':form})

#=======================================#
# Downloading the PDF file
#=======================================#

def download_pdf(request, resume_id):
    resume = get_object_or_404(ResumeModel, id=resume_id)
    return FileResponse(resume.pdf.open('rb'),as_attachment=True,filename=resume.pdf.name)

def download_redirect(request):
    return render('download_redirects.html')
    
    
    

    