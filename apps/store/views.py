from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# the index function is called when root is visited
def index(request):
    try: 
        request.session['total']
    except:
        request.session['total']={
            'charge':0,
            'num':0
        }
    #return HttpResponse(response)
    return render(request,'store/index.html')
def buy(request):
    if request.method=='POST':
        if request.POST['product_id']=='1':
            price=19.99
        elif request.POST['product_id']=='2':
            price=29.99
        elif request.POST['product_id']=='3':
            price=39.99
        elif request.POST['product_id']=='4':
            price=49.99
        else:
            return redirect('/amadon')

        if request.POST['quantity']<1:
            quantity=0
        else:
            quantity=int(request.POST['quantity'])

        # print quantity
        # print type(quantity)
        charge=float(price)*quantity
        request.session['last_item']={'charge':charge}
        # print "last item cost",request.session['last_item']['charge']
        request.session['total']['charge']+=charge
        request.session['total']['num']+=quantity
        request.session.modified = True
        # print 'total charge is:',request.session['total']['charge']
        # print 'total num is: ',request.session['total']['num']
        return redirect('/amadon/checkout')
    return redirect('/amadon')
def checkout(request):
    try:
        request.session['last_item']
    except:
        return redirect('/amadon')
    try:
        request.session['total']
    except:
        return redirect('/amadon')
    # if not request.session['cart']:
    #     return redirect('/amadon')

    return render(request,'store/checkout.html')
def clear(request):
    for key in request.session.keys():
        del request.session[key]
    print "cart cleared!"
    return redirect('/amadon')