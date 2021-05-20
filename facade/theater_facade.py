from facade.sub_systems import Light, DVDPlayer, Projector, PopcornPopper


class TheaterFacade:

    def __init__(self, light: Light, dvd_player: DVDPlayer, projector: Projector,
                 popcorn_popper: PopcornPopper) -> None:
        self.light = light
        self.dvd_player = dvd_player
        self.projector = projector
        self.popcorn_popper = popcorn_popper

    def watch_movie(self, movie):
        print('Get ready to watch movie: {}'.format(movie))
        self.light.on()
        self.light.theater_mode()

        self.popcorn_popper.on()
        self.popcorn_popper.pop()

        self.projector.on()
        self.projector.wide_screen_mode()

        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print('Shutting theater movie down...')
        self.popcorn_popper.off()

        self.light.daily_mode()

        self.projector.off()

        self.dvd_player.stop()
        self.dvd_player.off()
