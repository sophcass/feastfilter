from openai import OpenAI

from feastinsight.models import Review
from feastinsight.prompts import CHATGPT_USER_MESSAGE_SENTIMENT
client = OpenAI(
    organization="org-Upl1xBhyX6U3AnAOAxfpQIsj",
    api_key=""
    )

prompt = CHATGPT_USER_MESSAGE_SENTIMENT
role_content = "You are a analyst parsing customer reviews about their restaurant experience."

reviews = Review.objects.all()

for review in reviews.iterator():
    text = review.text

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": role_content,
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt + text
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

    print(response.choices[0].message.content)
