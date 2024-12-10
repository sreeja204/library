from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import book, CartItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Test View
def show(request):
    return HttpResponse("hiii")

# Example View
def example(request):
    return render(request, 'eg.html')

# Home Page
def front(request):
    return render(request, 'front.html')

# Display Featured, Popular, and Offer Books
def msg(request):
    featuredbooks = book.objects.filter(is_featured=True)
    popularbooks = book.objects.filter(is_popular=True)
    offerbooks = book.objects.filter(is_offer=True)
    return render(request, 'index.html', {
        'featuredbooks': featuredbooks,
        'popularbooks': popularbooks,
        'offerbooks': offerbooks
    })

# User Signup
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Create and login user
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('page')  # Redirect to home page after signup

    return render(request, 'signup.html')

# User Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('page')  # Redirect to home page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# User Logout
def logout_views(request):
    logout(request)
    return redirect('page')  # Redirect to home page after logout

  
@login_required   
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(book, id=product_id)
        
        # Check if the product is already in the cart
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': 1}  # Default quantity for a new item
        )
        if not created:
            # If the item already exists, increment the quantity
            cart_item.quantity += 1
            cart_item.save()
        
        return redirect('view_cart')  # Redirect to cart view after adding an item



@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)  # Use `total_price` property in `CartItem`
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'view_cart.html', context)


# Update Cart
def update_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart_item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
        if cart_item:
            cart_item.quantity = quantity
            cart_item.save()
        return redirect('view_cart')

# Remove from Cart
def remove_from_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        cart_item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
        if cart_item:
            cart_item.delete()
        return redirect('view_cart')

@login_required
def checkout_view(request):
    # Logic to display the checkout page (e.g., order summary, user info, etc.)
    return render(request, 'checkout.html')




