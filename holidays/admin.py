from django.contrib import admin

from .models import  Continent, AsiaCountries, AfricaCountries, NorthAmericaCountries, EuropeCountries, AntarcticaCountries, AustraliaCountries, TypeHoliday, HolidayRef
# admin.site.register(Holiday)
admin.site.register(Continent)
admin.site.register(AfricaCountries)
admin.site.register(AsiaCountries)
admin.site.register(NorthAmericaCountries)
admin.site.register(EuropeCountries)
admin.site.register(AntarcticaCountries)
admin.site.register(AustraliaCountries)
admin.site.register(TypeHoliday)
admin.site.register(HolidayRef)

# admin.site.register(Result)
# admin.site.register(
# admin.site.register(
# admin.site.register(


