from openai import OpenAI
from feastinsight.models import Place, Review

ORGANIZATION_ID = ""
API_KEY = ""

client = OpenAI(
    organization=ORGANIZATION_ID,
    api_key=API_KEY
)

def add_sentiment_of_review(review: Review) -> None:
    """
    Analyzes the sentiment of the given review and updates the review object
    with the detected sentiment.

    This function processes the text content of the review, determines its sentiment
    (e.g., positive, neutral, or negative), and adds this sentiment information
    to the review object. The update is done in place, so the function does not return
    any value.

    Args:
        review (Review): The review object to analyze and update with sentiment information.

    Returns:
        None
    """
    ROLE_CONTENT = "You are a analyst parsing customer reviews about their restaurant experience."

    SENTIMENT = ["Positive", "Negative", "Neutral"]

    OPENAI_USER_MESSAGE_SENTIMENT = f"""
    I am going to provide you with a review from a customer of a restaurant.
    Your job is to tag the review with one of the following sentiment: {SENTIMENT}.
    Please output your answer as the sentiment only. Do not include any additional text,
    explanations, or introductory phrases.
    Here is the review:
    """

    try:
        review_text = review.text

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": ROLE_CONTENT,
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": OPENAI_USER_MESSAGE_SENTIMENT + review_text
                    }
                ]
                },
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={
                "type": "text"
            }
        )

        sentiment = response.choices[0].message.content

        review.sentiment = sentiment
        review.save()

    except Exception as e:
        print(f"Error analyzing sentiment: {e}")

def add_theme_of_review(review: Review) -> None:
    """
    Identifies the main theme(s) of the given review and updates the review
    object with this information.

    This function analyzes the text content of the review to determine
    its primary theme(s) (e.g., service, ambiance, food quality).
    The identified themes are added to the review object. The update is done in place,
    so the function does not return any value.

    Args:
        review (Review): The review object to analyze and update with theme information.

    Returns:
        None
    """
    pass

def add_short_description(place: Place) -> None:
    """
    Generates a short description for the given place based on its attributes and
    adds it to the place object.

    This function creates a concise description of the place, summarizing key attributes
    such as its type, notable features, or specialties. The generated description is
    added to the place object.
    The update is done in place, so the function does not return any value.

    Args:
        place (Place): The place object to generate and update with a short description.

    Returns:
        None
    """
    pass