from PIL import Image, ImageDraw

WIDTH = 800
HEIGHT = 1280
PANELS = 3
MARGIN = 90


def main():
    # Create image from zero
    image = Image.new("RGBA", (WIDTH, HEIGHT), (255, 255, 255, 255))

    # Draw a line
    draw = ImageDraw.Draw(image)
    y = MARGIN / 2
    draw.line((0, y) + (WIDTH, y), fill=(0, 0, 0), width=5)
    for _ in range(PANELS):
        y += HEIGHT / PANELS - MARGIN
        draw.line((0, y) + (WIDTH, y), fill=(0, 0, 0), width=5)
        y += MARGIN
        draw.line((0, y) + (WIDTH, y), fill=(0, 0, 0), width=5)

    # Save image
    image.save("template.png")

    pass


if __name__ == "__main__":
    main()
