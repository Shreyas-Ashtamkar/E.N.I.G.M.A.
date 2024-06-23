import instructor

from pydantic import BaseModel, Field

from openai import OpenAI

from datetime import datetime
# import weather

def get_time():
    return datetime.now().strftime('%H:%M')

def get_temperature(city="Pune", country="India", time=None):
    # time_now = get_time() if time==None else time
    # return weather \
    #         .forecast(cityname=city, countryname=country) \
    #         .today[time_now] \
    #         .temp
    print(f"Calling the temp function for ({city}, {country})")
    return 17.4

print(get_temperature())

class WeatherInfo(BaseModel):
    city: str = Field(..., description="Name of the City")
    country: str = Field(..., description="Name of the Country")

client = instructor.patch(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",
    ),
    mode=instructor.Mode.JSON,
)

city = "Pune",
country = "India"

resp:WeatherInfo = client.chat.completions.create(
    model="phi3",
    messages=[
        {
            'role' : "user",
            'content' : f"Return the name of the {city} and the name of the {country}."
        }
    ],
    response_model=WeatherInfo
)

print(resp.json())
