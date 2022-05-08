from PIL import Image, ImageDraw

WIDTH = 800
HEIGHT = 1280
PANELS = 3
MARGIN = 90
PAGES = 2
THICK = 5

BLACK = (0, 0, 0)
RED = (255, 0, 0)


def draw_line(draw, y: float, color: tuple, width=THICK, **kwargs):
    draw.line((0, y, WIDTH, y), fill=color, width=width, **kwargs)


def draw_panels(draw, page_num: int):
    y = page_num * HEIGHT
    y += MARGIN / 2
    draw_line(draw, y, BLACK)
    for _ in range(PANELS):
        y += HEIGHT / PANELS - MARGIN
        draw_line(draw, y, BLACK)
        y += MARGIN
        draw_line(draw, y, BLACK)


def draw_pages(draw):
    for page_num in range(1, PAGES):
        y = page_num * HEIGHT
        draw_line(draw, y, RED)


def main():
    # Create image from zero
    image = Image.new("RGBA", (WIDTH, PAGES * HEIGHT), (255, 255, 255, 255))

    # Draw a line
    draw = ImageDraw.Draw(image)

    if PAGES == 1:
        draw_panels(draw, 0)
    else:
        for i in range(PAGES):
            draw_panels(draw, i)
        draw_pages(draw)

    # Save image
    image.save("template2.png")


if __name__ == "__main__":
    main()
