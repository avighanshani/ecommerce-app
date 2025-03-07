from django.shortcuts import render, redirect
from django.http import JsonResponse
from .data import consultation_bookings
from .models import Booking
import datetime
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from products.models import Product, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib import messages
import datetime

# Create your views here.


def index(request):
    query = Product.objects.all()
    categories = Category.objects.all()
    selected_sort = request.GET.get('sort')
    selected_category = request.GET.get('category')

    if selected_category:
        query = query.filter(category__category_name=selected_category)

    if selected_sort:
        if selected_sort == 'newest':
            query = query.filter(newest_product=True).order_by('category_id')
        elif selected_sort == 'priceAsc':
            query = query.order_by('price')
        elif selected_sort == 'priceDesc':
            query = query.order_by('-price')

    page = request.GET.get('page', 1)
    paginator = Paginator(query, 20)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except Exception as e:
        print(e)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'selected_sort': selected_sort,
    }
    return render(request, 'home/index.html', context)



# Show booking form
def book_consultation(request):
    # return render(request, 'base.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        service_type = request.POST.get('service_type')
        try:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            booking = Booking(name, email, date_obj, service_type)
            consultation_bookings.append(booking.__dict__)
            
            messages.success(request, "Booking successful!")  # Success message
            return redirect('book_consultation')  # Redirect to the same page

        except ValueError:
            messages.error(request, "Invalid date format!")
            return redirect('book_consultation')

    return render(request, 'booking_form.html')


# Show all bookings
def booking_list(request):
    return render(request, 'booking_list.html', {'bookings': consultation_bookings})
