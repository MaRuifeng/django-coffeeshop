##### NOTE #####
##### This is not an executalbe script! #####

# start a django project
django-admin startproject myshop

# start django local server which runs at http://127.0.0.1:8000/
python3 manage.py runserver

# create an app in the project
cd myshop
python3 manage.py startapp coffeeshop



# create migration SQL scripts and check, then run migration
python3 manage.py makemigrations coffeeshop
python3 manage.py sqlmigrate coffeeshop 0001
python3 manage.py migrate

# check project for problems
python3 manage.py check

# open django python shell to play with the model APIs
python3 manage.py shell
from coffeeshop.models import *
Category.objects.all()
c = Category(category_name="Coffee")
c.save()
c = Category(category_name="Tea")
c.save()

Category.objects.all().delete()
Category.objects.filter(id=3)
Category.objects.get(id=4)
Category.objects.filter(name='Coffee')
Category.objects.filter(name__iexact='coffee')
Category.objects.all().values_list('id', flat=True)

c = Category.objects.get(pk=3)
c.drinktype_set.all()
c.drinktype_set.create(name='Espresso')
c.drinktype_set.create(name='Latte')
c.drinktype_set.create(name='Cappuccino')
c = Category.objects.get(pk=4)
c.drinktype_set.all()
c.drinktype_set.create(name='GreenTea')
c.drinktype_set.create(name='HotTea')
c.drinktype_set.create(name='NotTea')

DrinkType.objects.filter(name__iexact='coffee')

d = c.drinktype_set.filter(name__startswith='NotTea')
d.delete()

s = Size(name='Tall')
s.save()
s = Size(name='Grande')
s.save()
s = Size(name='Venti')
s.save()

drink_type = DrinkType.objects.get(name='Espresso')
size = Size.objects.get(name='Tall')
drink = Drink(price = 1.95, drink_type = drink_type, size = size)
drink.save()

drink = Drink.objects.get(pk=1)
order = Order(quantity=2, drink=drink)
order.save
Order.objects.all()

sizes = set()
for drink in Drink.objects.filter(drink_type__name__iexact='Espresso').select_related('size'):
	sizes.add(drink.size)

from django.db.models import Sum, F
sum = Order.objects.aggregate(total=Sum(F('drink__price') * F('quantity'), output_field=DecimalField(decimal_places=2)))['total']


Order.objects.filter(drink__drink_type__category_id=3, drink__size_id=1)
filter_params = {}
filter_params['drink__drink_type__category_id']=3
filter_params['drink__size_id']=1
Order.objects.filter(**filter_params)

# Reload model with changes
from importlib import reload
import coffeeshop.models
reload(coffeeshop.models)
from coffeeshop.models import *

# SQLite client
sqlite3 db.sqlite3
.header on
.mode column
.schema
SELECT * FROM coffeeshop_category;
SELECT * FROM coffeeshop_drinktype;
SELECT * FROM coffeeshop_drink;

# mange test data
python3 manage.py dumpdata coffeeshop.Category > coffeeshop/fixtures/category.json
python3 manage.py dumpdata coffeeshop.DrinkType > coffeeshop/fixtures/drink_type.json
python3 manage.py dumpdata coffeeshop.Size > coffeeshop/fixtures/size.json
python3 manage.py dumpdata coffeeshop.Drink > coffeeshop/fixtures/drink.json

python3 manage.py flush # clear all data
python3 manage.py flush --noinput # clear all data without prompts

Drink.objects.all().delete()
python3 manage.py loaddata coffeeshop/fixtures/category.json
python3 manage.py loaddata coffeeshop/fixtures/drink_type.json
python3 manage.py loaddata coffeeshop/fixtures/size.json
python3 manage.py loaddata coffeeshop/fixtures/drink.json

# django admin
python3 manage.py createsuperuser

# unit test
python3 manage.py test coffeeshop

# Install and use Postgresql
sudo su -
apt-get install postgresql postgresql-contrib
update-rc.d postgresql enable # enable start on boot
service postgresql start
su - postgres
psql # Enter CLI
\q   # Exit

# get project requirement list
sudo apt-get install python3-pip
pip3 install pipreqs
pipreqs /path/to/project

# using Heroku
heroku login
heroku create [app_name]
heroku local web
# so silly... make sure the git repo is initialized within the Django project folder..
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py loaddata coffeeshop/fixtures/category.json
heroku run python manage.py loaddata coffeeshop/fixtures/drink_type.json
heroku run python manage.py loaddata coffeeshop/fixtures/size.json
heroku run python manage.py loaddata coffeeshop/fixtures/drink.json

heroku restart
heroku logs -t
heroku logs --app flyer-shop
