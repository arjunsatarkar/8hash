#!/usr/bin/env python3
import ctypes
import random
import sys

# Source: https://en.wikipedia.org/wiki/Magic_8-ball#Possible_answers
committal_responses = [
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
    # Negative
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

non_committal_responses = [
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
]


def djb2_hash(text: str):
    res = ctypes.c_uint32(5381)
    for c in text:
        res = ctypes.c_uint32(res.value * 33 + ord(c))
    return res.value


def get_committal_response(question: str) -> str:
    return committal_responses[djb2_hash(question) % len(committal_responses)]


def get_response(question: str) -> str:
    if random.random() < len(non_committal_responses) / len(committal_responses):
        return random.choice(non_committal_responses)
    else:
        return get_committal_response(question)


if __name__ == "__main__":
    try:
        while True:
            print(get_response(input("> ")))
    except (KeyboardInterrupt, EOFError):
        print()
        sys.exit(0)
