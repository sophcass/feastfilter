CLAUDE_USER_MESSAGE = (
    """
I am going to provide you with a JSON list of 10 restaurants.
Your task is to generate a richer, more descriptive name for each restaurant based on the data provided.
Follow these guidelines:
<instructions>
1. Exclusions: X, Y, Z
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
Input: [{"name": "Restaurant A", "type": ["Hamburger Joint", "Fast food"], "reviews": [{},{},{}]},
{"name": "Restaurant A", "type": ["Hamburger Joint", "Fast food"], "reviews": [{},{},{}]},
{"name": "Restaurant A", "type": ["Hamburger Joint", "Fast food"], "reviews": [{},{},{}]}
]
Output:
{"ID A": "Hamburger Late Night Takeaway",
 "ID A": "Mario's Italian Fine Dining",
 "ID A": "Cozy Pub Grub"}
</example>
"""
    """
Now, create descriptive names for the following restaurants:
"""
)

# TODO: Get some real examples to input into the <example></example>
# TODO: Get some examples of the types of titles GenAI creates and use this to come up with exclusions, inclusions - document and discuss this approach in the presentation
#  
