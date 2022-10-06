import os

from PIL import Image, ImageDraw, ImageFont
from data_class import Point

FONT_DIR = os.path.abspath("").replace("update_image_code", "fonts" + os.sep + "FontsFree-Net-CodecPro-Regular.ttf")
IMAGE_DIR = os.path.abspath("").replace("update_image_code", "images" + os.sep + "salvador.jpeg")
UPDATED_IMAGE_DIR = os.path.abspath("").replace("update_image_code", "updated_images" + os.sep + "salvador-student-result.png")


class ImageUpdater:

    def __init__(self, image_path: str) -> None:
        self.__source_file_name: str = image_path
        self.source_image: Image = None

    def __enter__(self) -> "ImageUpdater":
        self.source_image = Image.open(self.__source_file_name, 'r').convert("RGBA")
        return self

    def __exit__(self, type, value, tb) -> None:
        self.source_image.close()

    def draw(self, text: str, background_color: str, text_color: str, initial_point: Point, final_point: Point) -> None:
        font = ImageFont.truetype(FONT_DIR, size=20)

        draw = ImageDraw.Draw(self.source_image)

        draw.rectangle(fill=background_color, xy=(initial_point.to_tuple(), final_point.to_tuple()))

        draw.text(text=text, font=font, fill=text_color, xy=(Point(final_point.x-170, final_point.y-95).to_tuple()))

    def save(self) -> None:
        self.source_image.save(UPDATED_IMAGE_DIR)


if __name__ == "__main__":
    with ImageUpdater(IMAGE_DIR) as file_1:
        file_1.draw(text="We are learning\nPython", background_color="black", text_color="white",
                    initial_point=Point(30, 10), final_point=Point(220, 160))

        file_1.draw(text="We are learning\nPython", background_color="yellow", text_color="black",
                    initial_point=Point(320, 10), final_point=Point(510, 160))

        file_1.draw(text="We are learning\nPython", background_color="#3e41f4", text_color="white",
                    initial_point=Point(180, 200), final_point=Point(370, 350))

        file_1.save()
