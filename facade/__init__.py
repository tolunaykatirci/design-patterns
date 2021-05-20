from facade.sub_systems import Light, DVDPlayer, Projector, PopcornPopper
from facade.theater_facade import TheaterFacade

if __name__ == "__main__":

    popper = PopcornPopper()
    light = Light()
    dvd_player = DVDPlayer()
    projector = Projector(dvd_player)

    theater_facade = TheaterFacade(light, dvd_player, projector, popper)
    theater_facade.watch_movie('Star Wars')

    print('\n')

    theater_facade.end_movie()

