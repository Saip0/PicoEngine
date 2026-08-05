sd = None
def init():
    global sd
    from libs import Init
    import os
    sd = Init.sdcard()
    os.mount(sd, "/sd")