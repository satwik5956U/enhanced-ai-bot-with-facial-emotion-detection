from django.shortcuts import render
from django.http import HttpResponse
import googletrans
import time
from .models import Member
# Create your views here.
#m=Member.objects.all()
#m.delete()
d=googletrans.LANGUAGES
lst=list(d.values())
lst4=['Microsoft David - English (United States)', 'Microsoft Ravi - English (India)', 'Microsoft Heera - English (India)', 'Microsoft Mark - English (United States)', 'Microsoft Zira - English (United States)', 'Microsoft Natasha Online (Natural) - English (Australia)', 'Microsoft William Online (Natural) - English (Australia)', 'Microsoft Clara Online (Natural) - English (Canada)', 'Microsoft Liam Online (Natural) - English (Canada)', 'Microsoft Sam Online (Natural) - English (Hongkong)', 'Microsoft Yan Online (Natural) - English (Hongkong)', 'Microsoft Neerja Online (Natural) - English (India) (Preview)', 'Microsoft Neerja Online (Natural) - English (India)', 'Microsoft Prabhat Online (Natural) - English (India)', 'Microsoft Connor Online (Natural) - English (Ireland)', 'Microsoft Emily Online (Natural) - English (Ireland)', 'Microsoft Asilia Online (Natural) - English (Kenya)', 'Microsoft Chilemba Online (Natural) - English (Kenya)', 'Microsoft Mitchell Online (Natural) - English (New Zealand)', 'Microsoft Molly Online (Natural) - English (New Zealand)', 'Microsoft Abeo Online (Natural) - English (Nigeria)', 'Microsoft Ezinne Online (Natural) - English (Nigeria)', 'Microsoft James Online (Natural) - English (Philippines)', 'Microsoft Rosa Online (Natural) - English (Philippines)', 'Microsoft Luna Online (Natural) - English (Singapore)', 'Microsoft Wayne Online (Natural) - English (Singapore)', 'Microsoft Leah Online (Natural) - English (South Africa)', 'Microsoft Luke Online (Natural) - English (South Africa)', 'Microsoft Elimu Online (Natural) - English (Tanzania)', 'Microsoft Imani Online (Natural) - English (Tanzania)', 'Microsoft Libby Online (Natural) - English (United Kingdom)', 'Microsoft Maisie Online (Natural) - English (United Kingdom)', 'Microsoft Ryan Online (Natural) - English (United Kingdom)', 'Microsoft Sonia Online (Natural) - English (United Kingdom)', 'Microsoft Thomas Online (Natural) - English (United Kingdom)', 'Microsoft Aria Online (Natural) - English (United States)', 'Microsoft Ana Online (Natural) - English (United States)', 'Microsoft Christopher Online (Natural) - English (United States)', 'Microsoft Eric Online (Natural) - English (United States)', 'Microsoft Guy Online (Natural) - English (United States)', 'Microsoft Jenny Online (Natural) - English (United States)', 'Microsoft Michelle Online (Natural) - English (United States)', 'Microsoft Roger Online (Natural) - English (United States)', 'Microsoft Steffan Online (Natural) - English (United States)', 'Microsoft Mohan Online (Natural) - Telugu (India)', 'Microsoft Shruti Online (Natural) - Telugu (India)', 'Microsoft Gagan Online (Natural) - Kannada (India)', 'Microsoft Sapna Online (Natural) - Kannada (India)', 'Microsoft Madhur Online (Natural) - Hindi (India)', 'Microsoft Swara Online (Natural) - Hindi (India)', 'Microsoft Midhun Online (Natural) - Malayalam (India)', 'Microsoft Sobhana Online (Natural) - Malayalam (India)', 'Microsoft Pallavi Online (Natural) - Tamil (India)', 'Microsoft Valluvar Online (Natural) - Tamil (India)', 'Microsoft Kani Online (Natural) - Tamil (Malaysia)', 'Microsoft Surya Online (Natural) - Tamil (Malaysia)', 'Microsoft Anbu Online (Natural) - Tamil (Singapore)', 'Microsoft Venba Online (Natural) - Tamil (Singapore)', 'Microsoft Kumar Online (Natural) - Tamil (Sri Lanka)', 'Microsoft Saranya Online (Natural) - Tamil (Sri Lanka)']
def index1(request):
    uname=""
    logpwd=""
    return render(request,'index1.html')
import random
def signup(request):
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    pwd1=request.GET['pwd1']
    if pwd!=pwd1:
        return render(request,'speak.html')
    m=list(Member.objects.filter(firstname=uname,pwd=pwd).values())
    if m!=[]:
        return HttpResponse("<script>alert('user exists');</script>")
    hello_messages = [
        "Hello, how are you today?",
        "Hey there! What's up?",
        "Hi, nice to see you!",
        "Hey, long time no see! How have you been?",
        "Hello! What's new with you?",
        "Hi there! Ready to conquer the day?",
        "Hey! It's great to see you!",
        "Hello, friend! How's everything going?",
        "Hi! How was your weekend?",
        "Hey! Hope you're having a fantastic day!",
        "Hello! What's on your mind?",
        "Hi there! How's life treating you?",
        "Hello! Ready for another adventure?",
        "Hi! How's everything in your world?",
        "Hello! Let's catch up soon, okay?",
        "Hi! How's the weather over there?",
        "Hello! What's cooking?",
        "Hi! How's the family doing?",
        "Hello! How's work/school treating you?",
        "Hi! Are you ready for some fun?",
        "Hello! Hope you're having a fantastic day!",
        "Hi! Did you have a good sleep?",
        "Hello! What are your plans for today?",
        "Hi there! Let's make today count!",
    ]
    m=Member(firstname=uname,pwd=pwd,by="bot", chat=random.choice(hello_messages))
    m.save()
    #print(uname,pwd)
    return render(request,"signup.html")
def index(request):
    global uname
    global logpwd
    uname=str(request.POST.get('uname'))
    logpwd=str(request.POST.get('logpwd'))
    m=list(Member.objects.filter(firstname=uname, pwd=logpwd).values())
    if m==[]:
        return render(request,"speak.html")
    #print(m)
    return render(request,'index.html',{'lang':lst,'msgs':m,'speech':lst4,'uname':uname,'logpwd':logpwd})
def speechpage(request):
    return render(request,'speechpage.html',{'lang':lst})
from googletrans import Translator
#from gtts import gTTS
def login(request):
    d=Member.objects.filter(firstname=request.GET['fname'],pwd=request.GET['pwd'])
    d=list(d)
    if d==[]:
        return HttpResponse("<h1> invalid details</h1>")
    return render(request,)
def translate(request):
    data=Member.objects.all().values()
    #print(list(data))
    t=Translator()
    lst1=list(d.keys())
    ind=lst.index(str(request.GET['lang']))
    global cod
    cod=lst[ind]
    global out
    #print(cod)
    mod=Member()
    source=t.detect(str(request.GET['inptext'])).lang
    out=t.translate(request.GET['inptext'],dest=cod)
    stri=out.text
    lst55=list(stri.split('\n'))
    stri=""
    for i in lst55:
        stri+=(" "+i.rstrip("\r"))
    global lst3
    lst3=['Microsoft David - English (United States)', 'Microsoft Ravi - English (India)', 'Microsoft Heera - English (India)', 'Microsoft Mark - English (United States)', 'Microsoft Zira - English (United States)', 'Microsoft Natasha Online (Natural) - English (Australia)', 'Microsoft William Online (Natural) - English (Australia)', 'Microsoft Clara Online (Natural) - English (Canada)', 'Microsoft Liam Online (Natural) - English (Canada)', 'Microsoft Sam Online (Natural) - English (Hongkong)', 'Microsoft Yan Online (Natural) - English (Hongkong)', 'Microsoft Neerja Online (Natural) - English (India) (Preview)', 'Microsoft Neerja Online (Natural) - English (India)', 'Microsoft Prabhat Online (Natural) - English (India)', 'Microsoft Connor Online (Natural) - English (Ireland)', 'Microsoft Emily Online (Natural) - English (Ireland)', 'Microsoft Asilia Online (Natural) - English (Kenya)', 'Microsoft Chilemba Online (Natural) - English (Kenya)', 'Microsoft Mitchell Online (Natural) - English (New Zealand)', 'Microsoft Molly Online (Natural) - English (New Zealand)', 'Microsoft Abeo Online (Natural) - English (Nigeria)', 'Microsoft Ezinne Online (Natural) - English (Nigeria)', 'Microsoft James Online (Natural) - English (Philippines)', 'Microsoft Rosa Online (Natural) - English (Philippines)', 'Microsoft Luna Online (Natural) - English (Singapore)', 'Microsoft Wayne Online (Natural) - English (Singapore)', 'Microsoft Leah Online (Natural) - English (South Africa)', 'Microsoft Luke Online (Natural) - English (South Africa)', 'Microsoft Elimu Online (Natural) - English (Tanzania)', 'Microsoft Imani Online (Natural) - English (Tanzania)', 'Microsoft Libby Online (Natural) - English (United Kingdom)', 'Microsoft Maisie Online (Natural) - English (United Kingdom)', 'Microsoft Ryan Online (Natural) - English (United Kingdom)', 'Microsoft Sonia Online (Natural) - English (United Kingdom)', 'Microsoft Thomas Online (Natural) - English (United Kingdom)', 'Microsoft Aria Online (Natural) - English (United States)', 'Microsoft Ana Online (Natural) - English (United States)', 'Microsoft Christopher Online (Natural) - English (United States)', 'Microsoft Eric Online (Natural) - English (United States)', 'Microsoft Guy Online (Natural) - English (United States)', 'Microsoft Jenny Online (Natural) - English (United States)', 'Microsoft Michelle Online (Natural) - English (United States)', 'Microsoft Roger Online (Natural) - English (United States)', 'Microsoft Steffan Online (Natural) - English (United States)', 'Microsoft Mohan Online (Natural) - Telugu (India)', 'Microsoft Shruti Online (Natural) - Telugu (India)', 'Microsoft Gagan Online (Natural) - Kannada (India)', 'Microsoft Sapna Online (Natural) - Kannada (India)', 'Microsoft Madhur Online (Natural) - Hindi (India)', 'Microsoft Swara Online (Natural) - Hindi (India)', 'Microsoft Midhun Online (Natural) - Malayalam (India)', 'Microsoft Sobhana Online (Natural) - Malayalam (India)', 'Microsoft Pallavi Online (Natural) - Tamil (India)', 'Microsoft Valluvar Online (Natural) - Tamil (India)', 'Microsoft Kani Online (Natural) - Tamil (Malaysia)', 'Microsoft Surya Online (Natural) - Tamil (Malaysia)', 'Microsoft Anbu Online (Natural) - Tamil (Singapore)', 'Microsoft Venba Online (Natural) - Tamil (Singapore)', 'Microsoft Kumar Online (Natural) - Tamil (Sri Lanka)', 'Microsoft Saranya Online (Natural) - Tamil (Sri Lanka)']
    global lst4
    lst4=[]
    des=str(request.GET['lang'])
    flag=False
    for i in lst3:
        if des.lower() in i.lower():
            lst4+=[i]
            flag=True
    outtxt=str(stri)
    outtxt=outtxt.replace(" ","_")

    prono=str(out.pronunciation)
    prono=prono.replace(" ","_")
    #time.sleep(10)
    m=Member(firstname=uname,pwd=logpwd,by="user",chat=outtxt)
    m.save()
    if not flag:
        lst4=["this language can't be spelled out as it is but you could try in other formats"]
    global destlangu
    destlangu=str(request.GET['lang'])
    #return render(request,'output.html',{'text':outtxt,'source':d[source],'destlanguage':request.GET['lang'],'destlang':lst4})
    print("translated out text",outtxt)
    return outtxt
def trans(request):
    stri=str(translate(request))
    stri=stri.replace("_"," ")
    d=list(Member.objects.filter(firstname=uname,pwd=logpwd,by="user"))
    for i in d:
        outtxt1=i.chat
    outtxt1=outtxt1.replace("_"," ")
    t=Translator()
    out1=t.translate(outtxt1,dest='english')
    stri=out1.text+' '+stri
    out=t.translate(stri,dest='english')
    stri=str(out.text)
    print("translated text",stri)
    stri=stri.replace(" ","_")
    m=list(Member.objects.filter(firstname=uname, pwd=logpwd).values())
    return render(request,'new_output.html',{'msgs':m,'text':stri,'destlanguage':destlangu,'destlang':lst4})
def respond(request):
    t=Translator()
    lst1=list(d.keys())
    global out
    source=t.detect(str(request.GET['inptext'])).lang
    out=t.translate(request.GET['inptext'],dest=cod)

    stri=out.text
    lst55=list(stri.split('\n'))
    stri=""
    for i in lst55:
        stri+=(" "+i.rstrip("\r"))
    lst4=[]
    des=str(request.GET['lang'])
    flag=False
    for i in lst3:
        if des.lower() in i.lower():
            lst4+=[i]
            flag=True
    outtxt=str(stri)
    outtxt=outtxt.replace(" ","_")
    prono=str(out.pronunciation)
    prono=prono.replace(" ","_")
    #time.sleep(10)
    if not flag:
        lst4=["this language can't be spelled out as it is but you could try in other formats"]
    #print(lst4)
    m=Member(firstname=uname,pwd=logpwd,by="bot",chat=outtxt)
    m.save()
    #print("password",logpwd)
    #return render(request,'output.html',{'text':outtxt,'source':d[source],'destlanguage':request.GET['lang'],'destlang':lst4})
    return render(request,'dis.html',{'text':outtxt,'speech':lst4,'uname':uname,'pwd':logpwd})
