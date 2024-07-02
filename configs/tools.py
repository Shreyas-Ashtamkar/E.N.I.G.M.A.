import json

def hint_conversation(**kwargs):
    print(f"CALLED: hint_conversation\nPASSED :{kwargs}")
    if "message" in kwargs:
        return kwargs['message']
    return f"Okay, let's talk."

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

_IMAGE_GENERATION_URL = "IMAGE : ![{prompt}](https://image.pollinations.ai/prompt/{prompt}?width=1600&height=1200&nologo=poll&nofeed=yes)"

def generate_image(prompt:str, **kwargs):
    image_path = _IMAGE_GENERATION_URL.format(prompt=prompt.replace(" ", "%20"))
    return image_path
    # return _IMAGE_GENERATION_OUTPUT.format(img_path=image_path, img_prompt=prompt)

def get_time_data(location, format="12H", **kwargs):
    print("CALLED: get_time_data","\nPASSED :", location)
    return "7:30 AM"


if __name__ == "__main__":
    op = generate_image("A tree on a moon")
    print(op)
