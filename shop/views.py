from django.shortcuts import render,redirect
from	cart.forms	import	CartAddProductForm
# Create your views here.
from	django.shortcuts	import	render,	get_object_or_404
from	.models	import	Category,	Product
def	product_list(request,	category_slug=None):
				category	=	None
				categories	=	Category.objects.all()
				products	=	Product.objects.filter(available=True)
				if	category_slug:
								category	=	get_object_or_404(Category,	slug=category_slug)
								products	=	products.filter(category=category)
				return	render(request,'shop/product/list.html',{'category':	category,'categories':	categories,'products':	products})

def	product_detail(request,	id,	slug):
                cart_product_form = CartAddProductForm()
                product	=	get_object_or_404(Product,id=id,slug=slug,available=True)
                return	render(request,'shop/product/detail.html',{'product':	product,'cart_product_form':	cart_product_form})


def clogin(request):
        return render(request,'shop/clogin.html')
def alogin(request):
    if request.method == "GET":
        return render(request,'shop/alogin.html')
    else:
        email = request.POST.get('email')        
        password = request.POST.get('password')        
        if email=="admin@emarket.com" and password=="123":
            return redirect('/master/home')
        else:            
            return redirect('shop/alogin.html')
