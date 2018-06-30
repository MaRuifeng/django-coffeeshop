from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import DrinkType, Drink, Order
from .forms import OrderForm, FilterForm

class OrderListView(generic.ListView, generic.FormView):
    template_name = 'coffeeshop/order_list.html'
    context_object_name = 'order_list'
    form_class = FilterForm

    def get_queryset(self):
        # return Order.objects.all().order_by('id')[:20]
        return Order.objects.all().order_by('id')
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(OrderListView, self).get_context_data(**kwargs)
        # Add in total sales
        context['total_sales'] = Order.total_sales()
        return context

class FilteredOrderListView(generic.ListView):
    template_name = 'coffeeshop/filtered_order_list.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        size_id = self.request.GET.get('size')
        filter_params = {}
        if category_id.isdigit():
            filter_params['drink__drink_type__category_id'] = category_id
        if size_id.isdigit():
            filter_params['drink__size_id'] = size_id
        return Order.objects.filter(**filter_params).order_by('id')

class OrderCreateView(generic.FormView):
    template_name = 'coffeeshop/index.html'
    form_class = OrderForm

def load_drinktypes(request):
    category_id = request.GET.get('category_id')
    if category_id.isdigit():
        drinktypes = DrinkType.objects.filter(category_id=category_id).order_by('name')
        # print(drinktypes)
        return render(request, 'coffeeshop/drinktype_dropdown_list_options.html', {'drinktypes': drinktypes})
    else:
        return HttpResponseBadRequest()

def load_sizes(request):
    drink_type_id = request.GET.get('drink_type_id')
    if drink_type_id.isdigit():
        sizes = set()
        for drink in Drink.objects.filter(drink_type_id=drink_type_id).select_related('size'):
        	sizes.add(drink.size)
        return render(request, 'coffeeshop/size_dropdown_list_options.html', {'sizes': sizes})
    else:
        return HttpResponseBadRequest()

def place_order(request):
    try:
        selected_drink = Drink.objects.filter(drink_type_id=request.POST['drink_type'], size_id=request.POST['size']).first()
        if selected_drink == None: raise Drink.DoesNotExist
    except (KeyError, Drink.DoesNotExist):
        # Redisplay the order form
        return render(request, 'coffeeshop/index.html', {
            'form': OrderForm(),
            'error_message': "Such selection is not available. Please make a new one.",
        })
    else:
        order = Order(quantity=request.POST['quantity'], drink=selected_drink, ordered_at=timezone.now())
        order.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('coffeeshop:order_list'))
