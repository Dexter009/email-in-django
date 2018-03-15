from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render

# Create your views here.
from myapp.forms import QuestionForm


def index(request):
    if request.method == 'POST':
        form=QuestionForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            height=form.cleaned_data['height']
            image=request.FILES['image']

            email=EmailMessage('the subject here','Name:'+name + '\n'+'Age:'+age +'\n'+'Height:'+height,'johnmayor879@gmail.com',['nelsonmarcosdealmeida@gmail.com'])
            email.attach(image.name,image.read(),image.content_type)
            email.send()
            #send_mail('the subject here','Name:'+name,'johnmayor879@gmail.com',['defabc97110@gmail.com'])
            return render(request,'thank.html',{'name':name,'image':image})

    else:
        form=QuestionForm()
    return render(request,'home.html',{'form':form})