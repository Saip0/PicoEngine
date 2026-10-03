from machine import SPI, Pin

def St_init(SCL, SDA, RES, DC):
    
    from libs import st7789
    #import st7789
    spi = SPI(
        0,
        baudrate=10000000,
        polarity=1,
        phase=1,
        sck=Pin(SCL),#SCL
        mosi=Pin(SDA))#SDA

    tela = st7789.ST7789(
    spi,
    240,
    240,
    dc=Pin(DC, Pin.OUT),
    reset=Pin(RES, Pin.OUT),
    rotation=0,
    color_order = st7789.RGB
    )
    return tela

def l94_init(SCL, SDA, DC, RES, CS):

    from libs import ili9341

    spi = SPI(
        0,
        baudrate=40000000,
        sck=Pin(SCL),
        mosi=Pin(SDA)
    )

    tela = ili9341.Display(
        spi,
        cs=Pin(CS),
        dc=Pin(DC),
        rst=Pin(RES)
    )
    tela.set_rotation(270)
    tela.clear()
    return tela

def sdcard(SCK=18,MOSI=19,MISO=16,CS=17):
    
    from libs import sdcard
    import os

    spi = SPI(
        0,
        baudrate=1_000_000,
        sck=Pin(SCK),
        mosi=Pin(MOSI),
        miso=Pin(MISO)
    )

    cs = Pin(CS,Pin.OUT)

    sd = sdcard.SDCard(spi,cs)
    return sd


class Comp_SPI0:

    def __init__(
        self,
        SCK=2,
        MOSI=3,
        MISO=4,
        TFT_CS=1,
        TFT_DC=14,
        TFT_RST=15,
        RFID_CS=16,
        RFID_RST=17
    ):
        from machine import SPI, Pin

        self.spi = SPI(
            0,
            baudrate=10_000_000,
            polarity=0,
            phase=0,
            bits=8,
            sck=Pin(SCK),
            mosi=Pin(MOSI),
            miso=Pin(MISO)
        )

        self.TFT_CS = Pin(TFT_CS, Pin.OUT, value=1)
        self.TFT_DC = Pin(TFT_DC, Pin.OUT, value=0)
        self.TFT_RST = Pin(TFT_RST, Pin.OUT, value=1)

        self.RFID_CS = Pin(RFID_CS, Pin.OUT, value=1)
        self.RFID_RST = Pin(RFID_RST, Pin.OUT, value=1)

    def l94_init(self):

        from libs import ili9341

        tela = ili9341.Display(
            self.spi,
            cs=self.TFT_CS,
            dc=self.TFT_DC,
            rst=self.TFT_RST
        )

        tela.set_rotation(270)
        tela.clear()

        return tela

    def mfrc522_init(self):

        from libs.mfrc522 import MFRC522

        rfid = MFRC522(
            self.spi,
            rst=self.RFID_RST,
            cs=self.RFID_CS
        )

        return rfid
    
    def cs_tft(self,CS_Val=0):
        
        self.RFID_CS.value(1)
        self.TFT_CS.value(CS_Val)

    def cs_rfid(self,CS_Val=0):
        
        self.TFT_CS.value(1)
        self.RFID_CS.value(CS_Val)

    def deselect_all(self):
        
        self.TFT_CS.value(1)
        self.RFID_CS.value(1)
