import requests

from feastinsight.models import Place, Review


def get_places_data():
    url = "https://places.googleapis.com/v1/places:searchNearby"

    data = {
        "maxResultCount": 20,
        "rankPreference": "DISTANCE",
        "includedTypes": ["restaurant"],
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": 51.52789,
                    "longitude": -0.08173
                },
                "radius": 1000
            }
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": "",  # TODO: What is the best way to share this
        "X-Goog-FieldMask": "places.displayName.text,places.id,places.types,places.reviews,places.rating,places.primaryTypeDisplayName.text,places.reviews,places.location,places.formattedAddress"
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        restaurants = response.json()["places"]
        for restaurant in restaurants:
            # Restaurant information
            name = restaurant["displayName"]["text"]
            formatted_address = restaurant["formattedAddress"]
            location_latitude = restaurant["location"]["latitude"]
            location_longitude = restaurant["location"]["longitude"]
            type_displayname = restaurant["primaryTypeDisplayName"]["text"]
            if "rating" in restaurant.keys():
                rating = restaurant["rating"]
            else:
                rating = None

            place = Place(
                name=name,
                formatted_address=formatted_address,
                location_latitude=location_latitude,
                location_longitude=location_longitude,
                type_displayname=type_displayname,
                rating=rating
                )
            place.save()
            
            # Review information
            if "reviews" in  restaurant.keys():
                reviews = restaurant["reviews"]
                for review in reviews:
                    if "originalText" not in review.keys():
                        continue
                    review_text = review["originalText"]["text"]
                    review_publish_time = review["publishTime"]

                    review = Review(place=place, text=review_text, publish_time=review_publish_time)
                    review.save()        
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
