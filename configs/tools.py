import json

def hint_conversation(**kwargs):
    print(f"CALLED: hint_conversation\nPASSED :{kwargs}")
    return f"Can't do that yet"

def hint_error(error_message, **kwargs):
    print(f"CALLED: hint_error\nPASSED :{error_message}")
    return f"ERROR : {error_message}"

def get_weather_data(location:str, unit:str="Celcius", **kwargs):
    print(f"CALLED: get_weather_data\nPASSED : location={location}, unit={unit}")
    weather_data = {
        "temperature-high" : f"30 {unit}",
        "temperature-low"  : f"20 {unit}",
        "sky": "Clear",
        "rains" : "Slight Possibility"
    }
    return json.dumps(weather_data)

def generate_image(prompt:str, **kwargs):
    return prompt

def get_time_data(location, format="12H", **kwargs):
    print("CALLED: get_time_data","\nPASSED :", location)
    return "7:30 AM"


if __name__ == "__main__":
    generate_image("A tree on a moon")
