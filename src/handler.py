import random
import json

fortunes = [
    "You will die a terrible death!",
    "You will live forever.",
    "Cats will remember your name for generations",
    "You will fade into obscurity",
    "Your friends will remember your generosity",
    "You will consume many sandwiches",
    "Baking is your hidden talent",
    "You will become famous for your skill with rational numbers",
    "There is only so much that can be accomplished in one lifetime",
    "It is better to burn out than fade away, man.",
    "Huh?  I'm just here for the free food."
]


def handler(event, _):
    print(event)

    fortune_index = random.randint(0, len(fortunes) - 1)
    fortune = fortunes[fortune_index]
    print(fortune)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'fortune': fortune})
    }
