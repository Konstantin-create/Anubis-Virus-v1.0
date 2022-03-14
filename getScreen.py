from PIL import Image, ImageGrab
def screenshoot():
    img = ImageGrab.grab()
    img.save("screen.png", "PNG")