from vncdotool import api
from vnc_eds.driver import epd7in5


class VncEDS:
    def __init__(self):
        self.__display = epd7in5.EPD()
        self.__display.init()

        self.__client = api.connect('192.168.1.1', password='adc-ras')
        self.__last_img = None

    def update(self):
        self.__client.refreshScreen()
        image = self.__client.screen.crop((0, 0, epd7in5.EPD_HEIGHT, epd7in5.EPD_WIDTH))
        image = image.rotate(90, expand=True)

        if self.__last_img:
            if self.__last_img == image:
                print('No changes!')
                return  # abort

        print('Updating...')
        self.__last_img = image
        self.__display.display_frame(self.__display.get_frame_buffer(image))
