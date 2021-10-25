import random


class Response:
    """Responses for the magic 8-ball"""
    messages = [
        # Affirmative
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        # Non-committal
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        # Negative
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    @staticmethod
    def get(question: str):
        """Gets a response for a question

        :param question: Question asked of the magic 8-ball
        :return: Magic 8-ball's response
        """
        # Get the number of messages
        count = len(Response.messages)
        # Generate a bit of randomness
        adjustment = random.randrange(count)
        # Get the response by hashing, adding the random adjustment, and using the
        # modulus operator to choose an index within the responses list
        index = (hash(question) + adjustment) % count

        return Response.messages[index]
