from django.shortcuts import render, redirect
from .models import Profile,Addresses,Products,Coming_Products,Cart
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import date
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    products=Products.objects.all()[:20]
    coming_products=Coming_Products.objects.all()
    return render(request,'index.html',{'products':products,'coming_products':coming_products})

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials') 
            return redirect('login')
    else:
        return render(request,'login.html')    

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')    
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')       

def profile(request,id):
    
    user=User.objects.get(id=id)
    print('aaaaaaaa',user.first_name)
    if Profile.objects.filter(user_id=id):

        profile=Profile.objects.get(user_id=user.id)
        print("bbbbbbbbbb",profile.__dict__)
        address=Addresses.objects.get(id=profile.id)
        return render(request,'profile.html',{'profile':profile,'address':address})
    else:
        u='/checkout/'+str(user.id)
        return redirect(u) 
	
def edit(request,id):
    profile=Profile.objects.get(id=id)
    address=Addresses.objects.get(id=profile.id)
    return render(request,'edit.html',{'profile':profile,'address':address})

def contact(request):
    return render(request,'contact.html')

def update(request,id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    User.objects.filter(id =id).update(first_name=first_name,last_name=last_name)
    return redirect('home')

def details(request,id):
    details=Products.objects.get(id=id)
    products=Products.objects.all()[:20]
    coming_products=Coming_Products.objects.all()
    return render(request,'product_details.html',{'details':details,'products':products,'coming_products':coming_products})       
   
def d_details(request):
    details=Products.objects.get(id=1)
    products=Products.objects.all()[:20]
    coming_products=Coming_Products.objects.all()
    return render(request,'product_details.html',{'details':details,'products':products,'coming_products':coming_products})       

def category(request):
    products=Products.objects.all()[:8]
    product=Products.objects.all()
    Adidas,Nike,Puma,Fila=0,0,0,0


    for product in product:
        # product.qty=10
        # product.save()
        print('project_id',product.id,'qtu',product.qty)
        if product.desc =='Adidas':
            Adidas+=1
        elif product.desc =='Nike':
            Nike+=1
        elif product.desc =='Puma':
            Puma+=1
        else:
            Fila+=1
    return render(request,'category.html',{'products':products,'Adidas':Adidas,'Nike':Nike,'Puma':Puma,'Fila':Fila})

def adidas(request):
    products=Products.objects.all()
    Adidas,Nike,Puma,Fila=0,0,0,0
    p=[]
    for product in products:
        if product.desc =='Adidas':
            p.append(product)
            Adidas+=1
        elif product.desc =='Nike':
            Nike+=1
        elif product.desc =='Puma':
            Puma+=1
        else:
            Fila+=1
    return  render(request,'category.html',{'products':p,'Adidas':Adidas,'Nike':Nike,'Puma':Puma,'Fila':Fila})

def nike(request):
    products=Products.objects.all()
    Adidas,Nike,Puma,Fila=0,0,0,0

    p=[]
    for product in products:
        if product.desc =='Adidas':
            Adidas+=1
        elif product.desc =='Nike':
            p.append(product)
            Nike+=1
        elif product.desc =='Puma':
            Puma+=1
        else:
            Fila+=1
    return  render(request,'category.html',{'products':p,'Adidas':Adidas,'Nike':Nike,'Puma':Puma,'Fila':Fila})

def puma(request):
    products=Products.objects.all()
    Adidas,Nike,Puma,Fila=0,0,0,0

    p=[]
    for product in products:
        if product.desc =='Adidas':
            Adidas+=1
        elif product.desc =='Nike':
            Nike+=1
        elif product.desc =='Puma':
            p.append(product)
            Puma+=1
        else:
            Fila+=1
            
    return  render(request,'category.html',{'products':p,'Adidas':Adidas,'Nike':Nike,'Puma':Puma,'Fila':Fila})

def fila(request):
    products=Products.objects.all()
    Adidas,Nike,Puma,Fila=0,0,0,0

    p=[]
    for product in products:
        if product.desc =='Adidas':
            Adidas+=1
        elif product.desc =='Nike':
            Nike+=1
        elif product.desc =='Puma':
            Puma+=1
        else:
            Fila+=1
            p.append(product)
    return  render(request,'category.html',{'products':p,'Adidas':Adidas,'Nike':Nike,'Puma':Puma,'Fila':Fila})

def cart(request,id,pk):
    qty = request.POST['qty']
    product=Products.objects.get(id=id)
    a = int(product.qty)
    b = int(product.price)
    c=int(qty)
    d=a-c
    subtotal= b*c
    cart = Cart(img=product.img,desc=product.desc,price=product.price,user_id=pk,qty=qty,subtotal=subtotal,stock=d,Productid=product.id)
    cart.save();
    if d>=0:
        product.qty=d
        product.save();
    return redirect('category')

def showcart(request,id):
    carts=Cart.objects.all()

    user=User.objects.get(id=id)
    p=[]
    total=0
    for cart in carts:
        if cart.user_id==user.id:
            total=total+cart.subtotal
            p.append(cart)   
    gst=total*(0.18)
    finaltotal=gst+total
    return  render(request,'cart.html',{'products':p,'total':total,'finaltotal':finaltotal})

def checkout(request,id):
    carts=Cart.objects.all()
    user=User.objects.get(id=id)
    p=[]
    total=0
    for cart in carts:
        if cart.user_id==user.id:
            total=total+cart.subtotal
            p.append(cart)
    gst=total*(0.18)
    finaltotal=gst+total
    return render(request,'checkout.html',{'products':p,'total':total,'finaltotal':finaltotal})

def shipping_address(request,pk):
    print(pk)
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile_no = request.POST['mobile_no']
    alternate_mobile_number = request.POST['alternate_mobile_number']
    country = request.POST['country']
    state = request.POST['state']
    city = request.POST['city']
    address = request.POST['address']
    zipcode = request.POST['zipcode']

    user=User.objects.get(id=pk)
    user.first_name=first_name
    user.last_name=last_name
    user.save()

    addresses=Addresses(country=country,state=state,city=city,address=address,zipcode=zipcode) 
    addresses.save()
    p=Profile(mobile_no=mobile_no,alternate_mobile_number=alternate_mobile_number,user=user)
    p.save();

    profile=Profile.objects.get(user_id=user.id)
    profile.addresses.add(addresses)
    return render(request,'checkout.html')

def gmail(request):
    subject = 'swan'
    message = ' Thank you. Your order has been received... '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['darjinihar111@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'confirmation.html')  

def gmail1(request):
    subject = 'swan'
    message = ' Sorry,Your order has not received Because the selected item is not in stock.. '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['darjinihar111@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'out_of_stock.html')

def confirmation(request,id):
    carts=Cart.objects.all()
    user=User.objects.get(id=id)
    p=[]
    total=0
    for cart in carts:
        if cart.user_id==user.id:
            total=total+cart.subtotal
            p.append(cart)
    a=True
    for i in p:
        if i.stock<0:
            a=False
    if a:
        return redirect('/gmail') 
    else:
        return redirect('/gmail1') 

def clearcart(request,id):
    carts=Cart.objects.all()
    user=User.objects.get(id=id)
    p=[]
    total=0
    for cart in carts:
        if cart.user_id==user.id:
            total=total+cart.subtotal
            p.append(cart)
    for i in p:
        i.delete()
    u='/showcart/'+str(user.id)
    return redirect(u) 


