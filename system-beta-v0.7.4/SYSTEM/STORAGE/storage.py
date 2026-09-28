sd = None
def init():
    global sd
    from libs import init as Init
    import os
    sd = Init.sdcard()
    os.mount(sd, "/sd")