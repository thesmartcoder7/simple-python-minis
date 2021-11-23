import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode

myNumber = input("Enter the phone number: ")
key = '4160f979eb954cadb0993d6bf72f967a'

_geocoder = OpenCageGeocode(key)

country = phonenumbers.parse(myNumber, "CH")
service = phonenumbers.parse(myNumber,"RO")
time_zone = phonenumbers.parse(myNumber, "GB")

query = str(geocoder.description_for_number(country, "en"))
results = _geocoder.geocode(query)

latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']

my_map = folium.Map(location=[latitude, longitude], zoom_start =9)
folium.Marker([latitude, longitude], popup=geocoder.description_for_number(country, "en")).add_to((my_map))
my_map.save("location.html")

print("- Country of origin: " + geocoder.description_for_number(country, "en"))
print("- Network carrier: " + carrier.name_for_number(service, "en"))
print("- Timezone: ", timezone.time_zones_for_number(time_zone))
# print(results)
print("- Latitude: " , latitude)
print("- Longitude: " , longitude)





