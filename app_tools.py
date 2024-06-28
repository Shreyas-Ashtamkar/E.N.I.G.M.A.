import json

def hint_conversation(**kwargs):
    print("CALLED: hint_conversation","\nPASSED :", kwargs)

def hint_error(error_message, **kwargs):
    print("CALLED: hint_error","\nPASSED :", error_message)
    return f"ERROR : {error_message}"

def get_weather_data(location:str, unit:str="Celcius", **kwargs):
    print("CALLED: get_weather_data","\nPASSED : location=", location, ", unit=", unit)
    
    return f"The current temperature in {location.capitalize()} is 50 {unit.capitalize()}"

def generate_image(prompt:str, **kwargs):
    return prompt

def get_time_data(location, **kwargs):
    print("CALLED: get_time_data","\nPASSED :", location)


if __name__ == "__main__":
    generate_image("A tree on a moon")
