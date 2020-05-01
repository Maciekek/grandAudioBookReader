import pygame
import logging
import pygame.display
import os

from src.Logger import log


class Player:
    mixer = pygame.mixer
    logger = logging.getLogger('grand_audio_book_player')
    isPaused = False

    def __init__(self, partEndEvent):
        self.mixer = pygame.mixer
        self.bookPartEndEvent = partEndEvent
        os.environ["SDL_VIDEODRIVER"] = "dummy"

        pygame.display.init()
        pygame.init()
        pygame.mixer.init()
	pygame.mixer.music.set_volume(1)

    def play(self, fileToPlay):
        pygame.mixer.music.set_endevent(self.bookPartEndEvent)
        pygame.mixer.music.load("book/" + fileToPlay)
        pygame.mixer.music.play()

        log("Playing next part: " + fileToPlay)

    def pause(self):
        if self.isPaused:
            pygame.mixer.music.unpause()
            self.isPaused = False
            log("UNPause")
        else:
            pygame.mixer.music.pause()
            self.isPaused = True
            log("Pause")


