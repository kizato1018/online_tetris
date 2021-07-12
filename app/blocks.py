from PIL import ImageTk, Image
import os
import logging

image_path = os.path.dirname(os.path.abspath(__file__)) + '/image'


class Block():
    def __init__(self, type: str):
        self.type = type

        try:
            self.image = ImageTk.PhotoImage(
                image=Image.open(f'{image_path}/{type}.png').resize(size=(20,
                                                                          20)))
        except FileNotFoundError:
            logging.exception(f"{type}block Image Not found", exc_info=True)
            return False
