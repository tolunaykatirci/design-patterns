class PopcornPopper:

    def __init__(self) -> None:
        super().__init__()

    def on(self):
        print('PopcornPopper is on!')

    def off(self):
        print('PopcornPopper is off!')

    def pop(self):
        print('PopcornPopper is popping!')


class Light:

    def __init__(self) -> None:
        super().__init__()

    def on(self):
        print('Light is on!')

    def off(self):
        print('Light is off!')

    def daily_mode(self):
        print('Light is set to daily mode!')

    def theater_mode(self):
        print('Light is set to theater mode!')


class DVDPlayer:

    def __init__(self) -> None:
        super().__init__()

    def on(self):
        print('DVDPlayer is on!')

    def off(self):
        print('DVDPlayer is off!')

    def play(self, movie):
        print('DVDPlayer play movie: {}'.format(movie))

    def pause(self):
        print('DVDPlayer pause!')

    def stop(self):
        print('DVDPlayer stop!')


class Projector:

    def __init__(self, dvd_player: DVDPlayer) -> None:
        super().__init__()
        self.dvd_player = dvd_player

    def on(self):
        self.dvd_player.on()
        print('Projector is on!')

    def off(self):
        self.dvd_player.off()
        print('Projector is off!')

    def tv_mode(self):
        print('Projector is set to tv mode!')

    def wide_screen_mode(self):
        print('Projector is set to widescreen mode!')
