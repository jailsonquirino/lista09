import sys
from PIL import Image, ImageFilter


if __name__ == "__main__":
  print(f'argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    if i == 1:
      imagen1 = arg
    imagen2 = arg
    print(f"argument {i}: {arg}")


original = Image.open(sys.argv[1])

Blur1 = original.filter(ImageFilter.DETAIL)

Blur1.save(sys.argv[2])