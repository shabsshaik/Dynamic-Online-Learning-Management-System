from django.shortcuts import render,HttpResponse,redirect
from app1.models import Customer_details,product_details,store_details,course_page,test,score
from django.http import JsonResponse
# Create your views here.
final=[]

def csrf_failure_view(request, reason=""):
    return render(request, 'my_csrf_failure.html', {'reason': reason})

def Website(request):
    return render (request,'Website.html')

def SignUpPage(request):
    if request.method=='POST':
        Uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("<script>alert('Make Sure both passwords are same') ,window.location.href='http://127.0.0.1:8000/signup';</script>")
        else:
            data_store=Customer_details(username=Uname.capitalize(),email=email.capitalize(),password=pass1)
            data_store.save()
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if final!=[]:
        final.pop(-1)
    if request.method=='POST':
        uname=request.POST.get('username').capitalize()
        passw=request.POST.get('password')
        cd=Customer_details.objects.all()
        
        for i in cd:
            if i.username==uname and i.password==passw:
                final.append(uname)
                return redirect('home')
        else:
            return HttpResponse("<script>alert('Please Enter Valid Credentials') ,window.location.href='http://127.0.0.1:8000/login/';</script>")

    return render (request,'login.html')

def HomePage(request):
    if final!= []:
        pd=product_details.objects.all()
        data={
        "pd":pd,
        "username":final[0]
        }
    else:
        return redirect('Website')
    return render (request,'home.html',data)


def payment_free(request,c_name):
    if final !=[]:
        sd=store_details.objects.filter(username=final[0].capitalize(),alt=c_name.capitalize()).values
        pd=product_details.objects.filter(alt=c_name.capitalize()).values()
        data={
        "c_name":c_name,
        "pd":pd,
        "sd":sd
        }
    else:
        return redirect('Website')
    
    return render (request,'payment_free.html',data)

def update(request,alt):
    if final !=[]:
        pd=product_details.objects.filter(alt=alt.capitalize()).values()
        for i in pd:
            data_store=store_details(username=final[0].capitalize(),img=i['img'],alt=i['alt'],small_des=i['small_des'],big_des=i['big_des'],price=i['price'],s_icon=i['s_icon'],c_icon=i['c_icon'],category=i['category'],score=-1)
            data_store.save()
            return redirect('home')
    else:
        return redirect('Website')
    return render (request,'home.html')


def mycourse(request):
    if final!= []:
        pd=store_details.objects.filter(username=final[0].capitalize()).values()
        data={
            "pd":pd,
            "username":final[0]
        }
    else:
        return redirect('Website')
    return render (request,'my_course.html',data)

def course(request):
    if final!= []:
        data={
            "username":final[0]
        }
    else:
        return redirect('Website')
    return render (request,'course.html',data)

def course_view(request,c_name):
    if final !=[]:
        pd=course_page.objects.filter(alt=c_name.capitalize()).values()
        data={
        "c_name":c_name,
        "pd":pd,
        }
    else:
        return redirect('Website')
    
    return render (request,'course_view.html',data)

def recome(request):
    if final!= []:
        k=[]
        c=[]
        sd=store_details.objects.filter(username=final[0].capitalize()).values()
        for i in sd:
            k.append(i['category'])
            c.append(i['alt'])
        pd=product_details.objects.all()
        data={
            "pd":pd,
            "sd":sd,
            "username":final[0],
            "c":c,
            "k":k
            }

    else:
        return redirect('Website')
    return render (request,'recome.html',data)

def assment(request):
    if final!= []:
        pd=store_details.objects.filter(username=final[0].capitalize()).values()
        data={
            "pd":pd,
            "username":final[0]
        }
    else:
        return redirect('Website')
    return render (request,'assment.html',data)

def starttest(request,c_name):
    if final !=[]:
        pd=test.objects.filter(alt=c_name.capitalize()).values()
        data={
        "c_name":c_name,
        "pd":pd,
        }
        # if request.method == "POST":
        #     scores = request.POST.get('score')
        #     sd=score(username=final[0].capitalize(),alt=c_name.capitalize(),score=scores)
        #     sd.save()

    else:
        return redirect('Website')
    return render (request,'starttest.html',data)

def logout(request):
    final.pop(-1)
    return redirect('Website')