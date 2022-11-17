from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe
# Create your views here.

stripe.api_key = "sk_test_51M3g1wBKRTLDFn2tFd1UkRbfcZ6eU1c6meW1JafHPuO876lSLNKj6JpiZc0jQi25AD2DyWzHKGwhXUMOp8ADJcAj00WpR41VeX"

def index(request):
	return render(request, 'pyament/index.html')


def charge(request):
	
	if request.method == 'POST':
		print('Data:', request.POST)

		amount=int(request.POST['amount'])

		customer=stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['name'],
			id=request.POST['id'],
			source=request.POST['stripeToken']
			)

		charge=stripe.Charge.create(
			customer=customer,
			amount= amount*100,
			currency='usd',
			description="Subscription"
			)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'pyament/success.html', {'amount':amount})
