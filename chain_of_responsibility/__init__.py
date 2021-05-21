from chain_of_responsibility.handlers import MonkeyHandler, SquirrelHandler, DogHandler, Handler


def handle_food(food: str, handler: Handler):
    result = handler.handle(food)
    if result:
        print(f"  {result}", end="")
    else:
        print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":

    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    foods = ['Nut', 'Banana', 'Cup of Coffee']

    for food in foods:
        print(f"\nClient: Who wants a {food}?")
        handle_food(food, monkey)

    print()
    foods.append('MeatBall')
    for food in foods:
        print(f"\nClient: Who wants a {food}?")
        handle_food(food, squirrel)
