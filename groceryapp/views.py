from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department, Product
import base64
from django.core import serializers
from django.http import HttpResponse
import pyotp
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password
from .serializer import UserSerializer
# Create your views here.
def ListOfSimilarItems(id):
    ls = []
    id = int(id)
    if (id == 4920):
        ls = ['Red Seedless Grapes', 'Red Seedless Grapes Bunch', 'Red Seedless Grapes Imported', 'Organic Red Seedless Grapes', 'Concord Grape', 'Red Grapes', 'Grape Wine, Delicious Red', 'Green Seedless Grapes', 'Red Grape Juice Cocktail', 'Large Lemon', 'Organic Raspberries']

    elif (id == 16797):
        ls = ['YoKids Strawberry Banana/Strawberry Yogurt', 'Whole Strawberries', 'Strawberry Guava', 'Whole Frozen Strawberries', 'Frozen Strawberries', 'Strawberry Spread', 'Strawberry Shampoo', 'Frozen Whole Strawberries', 'Slim Strawberry', 'Strawberries Whole', 'Large Lemon']


    elif (id == 21137):
        ls = ['Organic Whole Strawberries', 'Organic Strawberry Spread', 'Organic Strawberry Thirst Quencher', 'Organic Strawberry Yogurt', 'Premium Organic Spread Strawberry', 'Fruit Spread, Organic, Strawberry', 'Organic Strawberry Preserves', 'Premium Organic Strawberry Spread', 'Organic Strawberry Fruit Spread', 'Large Lemon', 'Organic Raspberries']


    elif (id == 21903):
        ls = ['Organic Spinach & Potatoes 2, 6 Months+', 'Pears, Kale & Spinach Organic Baby Food', '2nd Foods Organic  Pear and Spinach Baby Food', 'Pear, Kiwi, Peas & Spinach Organic Baby Food', 'Organic 2nd Foods Apples, Blueberries & Spinach Baby Food', 'Organic Baby Spinach Salad', 'Organic Stage 4 Spinach Mango & Pear Baby Food', 'Organic Just Peas And Spinach Baby Food Stage 2', 'Organic Spinach', 'Large Lemon', 'Organic Raspberries']


    elif (id == 26209):
        ls = ['Classic Lime Margarita', 'Sweetened Lime Juice', 'Margaritas Strawberry Lime', 'Organic Lime Bag', 'Organic Limes', 'Lime Juice', 'Authentic Margaritas Classic Lime', 'Lime Beer', 'Lime', 'Large Lemon', 'Organic Raspberries']

    
    elif (id == 27845):
        ls = ['Organic  Whole Milk', 'Organic 2% Milk', 'Organic Milk Whole', 'Organic 1% Milk', 'Organic Milk', 'Vitamin D Organic Milk', 'Organic Vanilla Soy Milk', 'Vitamin D Organic Whole Milk', 'Organic Lowafat 1% Milk', 'Large Lemon', 'Organic Raspberries']


    elif (id == 28204):
        ls = ['Organic Fuji Apples', 'Organic Fuji Red Apple Chips', 'Tea House Organic Green Tea With Fuji Apple & Ginger', 'Bag of Organic Fuji Apples', 'Organic Heirloom Apple', 'Organic Honeycrisp Apples', 'Organic Envy Apple', 'Organic Apple Fuji 3 Lb Bag', 'Organic Fuji Red Crunchy Apple Chips', 'Large Lemon', 'Organic Raspberries']


    elif (id == 45066):
        ls = ['Apples Honeycrisp', 'Organic Honeycrisp Apples', 'Honeycrisp Apple Bag', 'Honeycrisp Apples', 'Just Honeycrisp Apples', 'Honeycrisp Apple Wheat Beer', 'Honeycrisp Apples, Bag', 'Honeycrisp Apple Cider', 'Apple Honeycrisp Organic', 'Large Lemon', 'Organic Raspberries']


    elif (id == 47626):
        ls = ['Bag of Large Lemons', 'Lemon Tea', 'Lemon Bag', 'Large Eggs', 'Large Soup', 'Sweet Lemon', 'Large AA Eggs', 'Lemon Tulsi Tea', 'Large Enriched Bread', 'Large Lemon', 'Organic Raspberries']


    elif (id == 47766):
        ls = ['Organic Avocado Oil', 'Organic Avocados', 'Organic Avocados 5 Count', 'Organic Hass Avocado', 'Organic Wild Rumpus Avocado Babyfood', 'Organic Hass Avocado Bag', 'Organic Safflower Avocado & Coconut Oil', 'Apples, Kale & Avocados Organic Baby Food', 'Organic Avocados Hass Variety', 'Large Lemon', 'Organic Raspberries']


    elif (id == 49683):
        ls = ['Cucumber Vodka', 'English Cucumbers', 'Seedless Cucumbers', 'Baby Cucumbers', 'Cucumbers', 'Cucumber', 'Cucumber Salad', 'Cucumber Jalapeno Juice', 'Organic Cucumber', 'Large Lemon', 'Organic Raspberries']

    print(ls)
    ls = ls[:4]
    return ls
def ListOfFreqItems(id):
    ls = []
    id = int(id)
    print(id)
    if (id == 4920):
        ls = ['Banana', 'Large Lemon', 'Organic Raspberries', 'Organic Strawberries', 'Organic Avocado', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Fuji Apple', 'Bag of Organic Bananas', 'Honeycrisp Apple', 'Organic Baby Spinach']
    elif (id == 16797):
        ls = ['Banana', 'Large Lemon', 'Organic Raspberries', 'Organic Strawberries', 'Organic Avocado', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Fuji Apple', 'Bag of Organic Bananas', 'Honeycrisp Apple', 'Organic Baby Spinach']

    elif (id == 21137):
        ls = ['Organic Raspberries', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Whole Milk', 'Bag of Organic Bananas', 'Organic Baby Spinach', 'Organic Avocado', 'Banana', 'Large Lemon', 'Organic Strawberries', 'Organic Fuji Apple']

    elif (id == 21903):
        ls = ['Organic Avocado', 'Organic Hass Avocado', 'Organic Strawberries', 'Bag of Organic Bananas', 'Banana', 'Large Lemon', 'Organic Raspberries', 'Organic Blueberries', 'Organic Fuji Apple', 'Honeycrisp Apple', 'Organic Baby Spinach']

    elif (id == 26209):
        ls = ['Large Lemon', 'Banana', 'Organic Raspberries', 'Organic Strawberries', 'Organic Avocado', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Fuji Apple', 'Bag of Organic Bananas', 'Honeycrisp Apple', 'Organic Baby Spinach']
    
    elif (id == 27845):
        ls = ['Organic Strawberries', 'Bag of Organic Bananas', 'Banana', 'Large Lemon', 'Organic Raspberries', 'Organic Avocado', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Fuji Apple', 'Honeycrisp Apple', 'Organic Baby Spinach']

    elif (id == 28204):
        ls = ['Banana', 'Large Lemon', 'Organic Raspberries', 'Organic Strawberries', 'Organic Avocado', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Fuji Apple', 'Bag of Organic Bananas', 'Honeycrisp Apple', 'Organic Baby Spinach']

    elif (id == 45066):
        ls = ['Banana', 'Large Lemon', 'Organic Raspberries', 'Organic Strawberries', 'Organic Avocado', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Fuji Apple', 'Bag of Organic Bananas', 'Honeycrisp Apple', 'Organic Baby Spinach']

    elif (id == 47626):
        ls = ['Limes', 'Organic Avocado', 'Banana', 'Large Lemon', 'Organic Raspberries', 'Organic Strawberries', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Fuji Apple', 'Bag of Organic Bananas', 'Honeycrisp Apple']

    elif (id == 47766):
        ls = ['Large Lemon', 'Organic Baby Spinach', 'Banana', 'Organic Strawberries', 'Organic Raspberries', 'Organic Avocado', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Fuji Apple', 'Bag of Organic Bananas', 'Honeycrisp Apple']

    elif (id == 49683):
        ls = ['Banana', 'Large Lemon', 'Organic Raspberries', 'Organic Strawberries', 'Organic Avocado', 'Organic Blueberries', 'Organic Hass Avocado', 'Organic Fuji Apple', 'Bag of Organic Bananas', 'Honeycrisp Apple', 'Organic Baby Spinach']
    print(ls)
    ls = ls[:4]
    return ls
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"
class HomeView(APIView):
    def get(self, request):
        return Response(data, status=200)
class ProductsView(APIView):
    def get(self, request):
        name = ['Organic Fuji Apple', 'Honeycrisp Apple', 'Cucumber Kirby', 'Organic Avocado', 'Seedless Red Grapes', 'Strawberries', 'Large Lemon', 'Organic Whole Milk', 'Limes', 'Organic Baby Spinach', 'Organic Strawberries']
        object = Product.objects.filter(product_name__in = name)
        print(object)
        qs_json = serializers.serialize('json', object)
        return HttpResponse(qs_json, content_type='application/json')
class ProductView(APIView):
    def get(self, request):
        qs_json = ""
        if request.GET.get('id'):
            id  = request.GET.get('id')
            object = Product.objects.filter(pk = id)
            print(object)
            qs_json = serializers.serialize('json', object)
        print(qs_json)
        return HttpResponse(qs_json, content_type='application/json')
class SimilarView(APIView):
    def get(self, request):
        if request.GET.get('id'):
            id = request.GET.get('id')
            print("id", id)
            name = ListOfSimilarItems(id)
            object = Product.objects.filter(product_name__in = name)
            print(object)
            qs_json = serializers.serialize('json', object)
            return HttpResponse(qs_json, content_type='application/json')
        return "Null"
class FreqView(APIView):
    def get(self, request):
        if request.GET.get('id'):
            id = request.GET.get('id')
            print("ikd",id )
            name = ListOfFreqItems(id)
            print(name)
            object = Product.objects.filter(product_name__in = name)
            print(object)
            qs_json = serializers.serialize('json', object)
            return HttpResponse(qs_json, content_type='application/json')
        return "Null"
class Department(APIView):
    def get(self, request):
        departments = Department.objects.all()
        print(departments)
        return Response("okk", status = 200)
# Registraion using otp 
class OtpView(APIView):
    def post(self, request):
        if 'get' in request.data:
            email = request.data['email']
            keygen = generateKey()
            key = base64.b32encode(keygen.returnValue(email).encode())
            OTP = pyotp.TOTP(key, interval=300)
            subject = "OTP to Sign Up On Grocery app"
            message = "Your OTP for singing up on Grocery app is " + OTP.now() + ". The code will be valid for 5 minutes only."
            email_from = settings.EMAIL_HOST_USER
            recipient = [email,]
            send_mail(subject, message, email_from, recipient)
            print(OTP.now())
            return Response("Otp Sent Successfully on email "+ email, status = 200 )
        otp = request.data['otp']
        email = request.data['email']
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(email).encode())
        OTP = pyotp.TOTP(key, interval=300)
        if OTP.verify(otp):
            print("veryfied")
            request.data['username'] = email
            serializer = UserSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                serializer.save()
                return Response("User Created Successfully", status = 201)
            return Response(serializer.errors, status=400)
        return Response("worng otp entered", status = 400)






