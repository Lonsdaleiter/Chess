'''
A module for the purpose
of drawing images to the
window associated therewith.

- Lonsdaleiter
'''


window = None


def draw(image, x, y):
    global window

    window.blit(image, (x, y))
