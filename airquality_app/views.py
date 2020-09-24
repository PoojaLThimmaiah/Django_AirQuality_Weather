from django.shortcuts import render


# Create your views here.

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['ZipCode']
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60610&distance=5&API_KEY=CC6EE5FC-6FBD-402A-94A0-97CC44DBBD95")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."

        if api[0]['AQI'] <= 50:
            Category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
            Category_Color = "good"
        elif api[0]['AQI'] >= 51 and api[0]['AQI'] <= 100:
            Category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            Category_Color = "moderate"
        elif api[0]['AQI'] >= 101 and api[0]['AQI'] <= 150:
            Category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            Category_Color = "USG"
        elif api[0]['AQI'] >= 151 and api[0]['AQI'] <= 200:
            Category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            Category_Color = "Unhealthy"
        elif api[0]['AQI'] >= 201 and api[0]['AQI'] <= 300:
            Category_description = "Health alert: The risk of health effects is increased for everyone."
            Category_Color = "Very_Unhealthy"
        else:
            Category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            Category_Color = "Hazardous"

        return render(request,"home.html",{"api":api, "Category_description" : Category_description, "Category_Color":Category_Color})
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60610&distance=5&API_KEY=CC6EE5FC-6FBD-402A-94A0-97CC44DBBD95")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."

        if api[0]['AQI'] <= 50:
            Category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
            Category_Color = "good"
        elif api[0]['AQI'] >= 51 and api[0]['AQI'] <= 100:
            Category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            Category_Color = "moderate"
        elif api[0]['AQI'] >= 101 and api[0]['AQI'] <= 150:
            Category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            Category_Color = "USG"
        elif api[0]['AQI'] >= 151 and api[0]['AQI'] <= 200:
            Category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            Category_Color = "Unhealthy"
        elif api[0]['AQI'] >= 201 and api[0]['AQI'] <= 300:
            Category_description = "Health alert: The risk of health effects is increased for everyone."
            Category_Color = "Very_Unhealthy"
        else:
            Category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            Category_Color = "Hazardous"

        return render(request,"home.html",{"api":api, "Category_description" : Category_description, "Category_Color":Category_Color})
