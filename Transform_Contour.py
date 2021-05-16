import sys
from PIL import Image, ImageFilter


if __name__ == "__main__":
  print(f'argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argument {i}: {arg}")


original = Image.open(sys.argv[1])

Contour1 = original.filter(ImageFilter.DETAIL)

Contour1.save(sys.argv[2])