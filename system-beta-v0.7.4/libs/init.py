def St_init(SCL, SDA, RES, DC):
    from libs import st7789
    from machine import SPI, Pin
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

    from machine import Pin, SPI
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
    from machine import SPI, Pin
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
