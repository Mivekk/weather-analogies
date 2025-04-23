def parse_weather_response(response):
    # Adjust the following lines according to the new JSON structure
    try:
        temperature = response['weather']['main']['temp']
        description = response['weather']['description']
        analogy = f"It's as hot as a summer day at noon, and feels like {description}."
        return analogy
    except KeyError as e:
        raise Exception(f"Failed to parse weather response, missing key: {e}")