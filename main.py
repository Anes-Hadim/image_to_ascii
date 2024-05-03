from PIL import Image

user_image = input("Enter the path for the image you want to display: ")

continue_program = True

while continue_program:
    try:
        image = Image.open(user_image)
        continue_program = False
    except IOError:
        print("Error: Could not open the image file make sure of your path and file type.")
        user_image = input("Enter the path for the image you want to display: ")

width, height = image.size

new_width = 300

aspect_ratio = height / width
new_height = int(new_width * aspect_ratio)


image = image.resize((new_width, new_height))



ascii_chars =  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1[]?-_+~<>i!lI;:,^`'."

def map_intensity_to_char(average_intensity):
    
    index = int(average_intensity / 256 * len(ascii_chars))
    index = min(max(index, 0), len(ascii_chars) - 1)
    return ascii_chars[index]

for i in range(new_height) :
  for j in range(new_width) :
    pixel = image.getpixel((j,i))
    if image.mode == 'RGB':
      red = pixel[0]
      green = pixel[1]
      blue = pixel[2]
      average=(red+green+blue)//3
    else:
      average = pixel
    chars=map_intensity_to_char(average)
    print(chars,end="")
  print()



