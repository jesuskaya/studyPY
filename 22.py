def greeting(greet):
    return lambda name: f"{greet}, {name}"


morning_greeting = greeting("Good morning")

print(morning_greeting("Temchik"))

evening_greeting = greeting("Good evening")

print(evening_greeting("Artem"))
