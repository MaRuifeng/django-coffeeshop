# django-coffeeshop

## Description
Below table contains a simple menu of a coffee shop.  

| Type/Size    | Tall   | Grande|Venti  |
| :-----------:|:------:|:-----:|:-----:|
| Espresso     | $1.95  | $2.05 | $2.35 |
| Latte        | $3.4   | $4.45 | $4.65 |
| Cappuccino   | $3.15  | $3.75 | $4.15 |
| Green Tea    | $3.45  | $4.25 | $4.45 |
| Hot Tea      | N.A.   | $1.95 | N.A.  |

Code a simple Django web app that supports
* Adding order
* Keep track of orders
* Group orders by beverage category (coffee or tea) and/or size

## Design
The app is designed via below simple database schema with general OOP principles adhered to. Coding is completed by following the well written [Django Documentation](https://docs.djangoproject.com/en/2.0/) with the MVC design pattern.
* `Category` - data model hosting beverage categories (coffe, tea etc.).
* `DrinkType` - data model hosting beverage type (Espresso, Green Tea etc.), `many-to-one` mapped to the `Category` model.
* `Size` - data model hosting available beverage sizes offered by the shop.
* `Drink` - data model hosting beverage prices based on type and size, `many-to-many` mapped to the `DrinkType` and `Size` model, yet combination of the both yields a unique constraint.
* `Order` - data model hosting beverage orders, `many-to-one` mapped to the `Drink` model, containing a quantity field indicating number of beverages in an order.

## Requirements
* Django ~> 2.0.6
* python ~> 3.4.3

## Build & Deployment
### Local envrionment
* Load the source code from the `development` branch.
* Fixtures are available to load initial DB data.
* Install the required the python packages and start server with command `python3 manage.py runserver`. The application is available at http://127.0.0.1:8000/coffeeshop/ and the Django admin at http://127.0.0.1:8000/admin. Some other useful commands are listed below.
  *  `python3 manage.py shell` - start the interactive python CLI shell
  *  `sqlite3 db.sqlite3` - start the SQLite CLI shell
  *  `python3 manage.py test coffeeshop` - run tests
### Heroku
The app is deployed from the `master` branch on Heroku accessible via https://flyer-shop.herokuapp.com/coffeeshop/.

## App Workflow
An admin person (powered by Django Admin) can open up the admin page  https://flyer-shop.herokuapp.com/admin to add new beverage categories, types and prices.

Once launched, a webpage will be directly presented to a shop cashier to place orders. Beverage types and sizes are loaded via chained Ajax calls for selection, depending on their availability in the database. Quantity can also be set or selected. Once selections are done and the submit button is clicked, an order will be placed via HTML form submission and the user will be directed to a page listing all orders and total sales amount. Filters are provided on the same page to view orders by category and/or size.

## Constraints and Future Improvement
This is a beginner project in Django for practice purpose. Below constraints are documented for further possible improvements.
* CSS styling is missing
* Currently plain Django form is used for order placement (a classed based `ModelForm` can be explored for cleaner implementation)
* Usage by generic class based views (`CreateView`, `ListView` etc.) can be expanded
* `Order` update/delete is not supported
* Ideally an `OrderDetail` model should be separated from the `Order` model such that different beverages can be placed in a single order, which is a very practical use case
* Filtering on order list can be better implemented with built-in Django tables and filters, in an Ajax manner instead of page redirecting
* Unit test coverage needs to be greatly expanded
* Other unspotted silly code snippets that do not fully utilize the power of the Django

## Extension Requirements
* Adding new beverage types or sizes: available via the Django admin console
* Support of adding condiments (grass jelly etc.): if the condiments have fixed price increments, a new model representing them can be added with a reference added to the `Order` model. Condiments are taken as parallel products offered by the shop just like beverages.


## Author
Ruifeng Ma (mrfflyer@gmail.com)
