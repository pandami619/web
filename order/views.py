from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import ProductionInBasket, ProductionInOrder, Order
from .forms import CheckoutContactForm


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get('is_delete')
    print(product_id, 'product_id', nmb, 'nmb')

    if is_delete == 'true':
        ProductionInBasket.objects.filter(id=product_id).update(is_active=False)

    else:
        new_product, created = ProductionInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                        is_active=True, order=None, defaults={"nmb": nmb})
        if not created:
            print ("not created")
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    products_in_basket = ProductionInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.title
        product_dict["price_pre_item"] = item.price_pre_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    print(return_dict, 'return_dict')
    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductionInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    print(products_in_basket,' product_in_basket')
    for item in products_in_basket:
        print(item.order, ' order')

    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print('yes')
            data = request.POST
            name = data.get("name", "3423453")
            phone = data['phone']
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)

            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductionInBasket.objects.get(id=product_in_basket_id)
                    print(type(value), 'type value')

                    product_in_basket.nmb = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    ProductionInOrder.objects.create(product=product_in_basket.product, nmb = product_in_basket.nmb,
                                                     price_pre_item=product_in_basket.price_pre_item,
                                                     total_price=product_in_basket.total_price,
                                                     order=order)

                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            print('no')
    return render(request, 'checkout/checkout_html.html', locals())