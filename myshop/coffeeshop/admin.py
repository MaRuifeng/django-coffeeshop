from django.contrib import admin

# Register your models here.
from .models import Category, DrinkType, Size, Drink, Order

class DrinkTypeInline(admin.TabularInline):
    model = DrinkType
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [DrinkTypeInline]
    list_display = ('name',)
    search_fields = ['name']
admin.site.register(Category, CategoryAdmin)

class SizeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    list_display = ('name',)
    search_fields = ['name']
admin.site.register(Size, SizeAdmin)

class DrinkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['price']}),
        (None, {'fields': ['drink_type']}),
        (None, {'fields': ['size']}),
    ]
    list_display = ('drink_type', 'size', 'price')
    list_filter = ['price']
    search_fields = ['drink_type__name']
admin.site.register(Drink, DrinkAdmin)

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['drink']}),
        (None, {'fields': ['quantity']}),
        (None, {'fields': ['ordered_at']}),
    ]
    list_display = ('get_drink_cat', 'get_drink_type', 'get_drink_size', 'get_drink_price', 'quantity', 'ordered_at')
    list_filter = ['ordered_at']
    search_fields = ['drink__size__name', 'drink__drink_type__name']

    def get_drink_type(self, obj):
        return obj.drink.drink_type
    get_drink_type.short_description = 'DrinkType'

    def get_drink_cat(self, obj):
        return obj.drink.drink_type.category
    get_drink_cat.short_description = 'Category'

    def get_drink_size(self, obj):
        return obj.drink.size
    get_drink_size.short_description = 'Size'

    def get_drink_price(self, obj):
        return obj.drink.price
    get_drink_price.short_description = 'Price'


admin.site.register(Order, OrderAdmin)
