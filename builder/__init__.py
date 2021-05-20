from builder.director import Director

if __name__ == "__main__":

    director = Director()

    house_1 = director.build_minimal_house()
    print(house_1.specifications())

    house_2 = director.build_lux_house()
    print(house_2.specifications())
