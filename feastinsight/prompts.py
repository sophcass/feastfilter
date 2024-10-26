CLAUDE_USER_MESSAGE = (
    """
I am going to provide you with a JSON list of 10 restaurants.
Your task is to generate a richer, more descriptive name for each restaurant based on the data provided.
Follow these guidelines:
<instructions>
2. Inclusions: The name must include the type of cuisine. The name must keep some of the original branding (e.g. A, B).
3. Length: The title must be between 3 and 10 words.
</instructions>
"""
    """
Your output must be only a JSON object. Do not include any additional text, explanations, or introductory phrases.
The JSON object should use the ID as the key and the new title as the value for each restaurant.
Structure the output like this:
<formatting_example>
{
    "<ID>": "<new more descriptive restaurant name>",
}
</formatting_example>
"""
    """
Here is an example:
<example>
Input: [
    {
        "id": "ChIJzXycbusddkgRoBhN4ijnAIc",
        "name": "Cocotte Shoreditch",
        "type": "Brunch Restaurant",
        "rating": 4.3,
        "reviews": [
            "Got take out one evening and the food was amazing! Chicken tenders, mac and cheese, half chicken, and fries all tasted amazing. The chicken was cooked perfect and the gravy was delicious. The restaurant looks like a fun place and hope to try eating in next time.",
            "Thanking Sam & Team for the wonderful food, service and all together good vibes! We were a large group that took up the majority of the restaurant but it didn't seem to phase the team. We got our yummy cocktails as soon as we sat down, along with a timely and most importantly delicious food service! Thank you so much for making our celebration one to remember - we'll be back!",
            "Chicken was soft and filled with brilliance. Chips were on point and extremely crispy. Food came quite early. Service was fantastic and cared about us more than money. Mario is a legend as well.",
        ],
    },
    {
        "id": "ChIJ97tcQbUddkgRrqWJPQzWZQU",
        "name": "Gigi's Hoxton",
        "type": "Bar",
        "reviews": [
            "Great atmosphere and cool interior. We visited on a very quiet Friday before NYE. Cocktails were nice. The kitchen was open but they didn't have much food in stock, including the vegan brownie I really wanted!",
            "Worst bar I've been to in the UK. Owner is hostile to customers and abusive to staff. Bouncers are needlessly aggressive. Cocktails are overpriced, taste terrible & take a rediculously long time to be served. For your own good, avoid this place. It has a low rating for a reason.",
            "i came in to the bar a bit over a week ago to watch england mach, the drinks were ok but shortly realised the aperol sprits we were ordering had an insufficient amount of alcohol in them but we didn't want to complain as i could see the bartenders were under stress, we then ordered food however the cooking was extremely slow for just a mere portion of chips? the atmosphere could also be improved.",
        ],
    },
    {
        "id": "ChIJvZVgN6UcdkgRGkVgG0CMnU0",
        "name": "MEATliquor Bar & Restaurant Shoreditch",
        "type": "Hamburger Restaurant",
        "reviews": [
            "Very good services waiters was on point in seconds and always checking if needed anything asking if everything is all good and very happy and really friendly staff",
            "This place is uniquely decorated with a cool atmosphere, made for a fun meal with friends. Friendly staff members. Menu options were good, with a dedicated vegan/veggie section. The food all came out on a big tray which was then left for us to distribute onto smaller plates - a cool idea in theory but made the already small tables a bit cramped for space. Despite this, food was delicious and have already recommended to friends to visit.",
            "I love this place. Been coming here for years and years, generally try to get here whenever I'm in London. The burgers are very good, not quite top tier, but close. Menu has a decent selection also with a variety of things on offer. The whole vibe and aesthetic of the restaurant is superb also.",
        ],
    },
]
Output:
{"ChIJZSpJ0bocdkgRouqF6clN7WQ": "Cocotte Shoreditch - Brunch and Cocktails with Unmatched Hospitality",
 "ChIJ97tcQbUddkgRrqWJPQzWZQU": "Gigi's Hoxton - Trendy Cocktails, Unpredictable Vibe",
 "ChIJvZVgN6UcdkgRGkVgG0CMnU0": "MEATliquor Shoreditch – Legendary Burgers, Edgy Decor, and a True London Experience"}
</example>
"""
    """
Now, create descriptive names for the following restaurants:
"""
)

# TODO: Get some examples of the types of titles GenAI creates and use this to come up with exclusions, inclusions - document and discuss this approach in the presentation
