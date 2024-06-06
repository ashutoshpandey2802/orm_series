from django.contrib.auth.models import User
from core.models import Restaurant,Rating
from django.utils import timezone
from django.db import connection
from pprint import pprint


#on way
# def run():
#     restaurant=Restaurant()
#     restaurant.name='my Italian restaurant'
#     restaurant.latitude=60.2
#     restaurant.longitude=81.2
#     restaurant.date_opened=timezone.now()
#     restaurant.restaurant_type=Restaurant.TypeChoice.ITALIAN
    
#     restaurant.save()
    
    
    # rs=Restaurant.objects.all()
    # res=Restaurant.objects.first()
    # print(rs)
    # print(res)
    
    # print(connection.queries)
    
    
#another way

# def run():
#     Restaurant.objects.create(
#     name='my Chinese restaurant',
#     latitude=66.2,
#     longitude=71.2,
#     date_opened=timezone.now(),
#     restaurant_type=Restaurant.TypeChoice.CHINESE
    
    
    
#     )
#     print(connection.queries)
    
    
    
# def run():
    
#     restaurant=Restaurant.objects.first()
#     user=User.objects.first()
    
#     Rating.objects.create(user=user,restaurant=restaurant,rating=3.5)




def run():
    user=User.objects.first()
    restaurant=Restaurant.objects.first()
    
    rating=Rating(user=user,restaurant=restaurant,rating=9)
    
    # print(connection.quaries)
    
    rating.full_clean()
    rating.save()