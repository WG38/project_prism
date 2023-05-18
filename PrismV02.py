from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None
inp_img = Image.open("grayscale.png")
inp_img = inp_img.convert("RGB")

width,height = inp_img.size

height_list = [] 
for y in range(0,width):
 for z in range(0,height):
  print(y,z)
  currVal = inp_img.getpixel((y,z))[0]
  height_list.append(currVal)

print(height_list[2])


max_val = max(height_list)

min_val = min(height_list)

def lerp(x1,y1,x2,y2,x3):
 slope = (y2-y1)/(x2-x1)
 y3 = y1 + slope*(x3-x1)
 return y3

#boundary points for color changes#
val0 = lerp(0,min_val,1,max_val,0)
val1 = lerp(0,min_val,1,max_val,0.33333)
val2 = lerp(0,min_val,1,max_val,0.66666)
val3 = lerp(0,min_val,1,max_val,1)

#colour generation#
color_list = []
for i in range(0,len(height_list)):
 print(i)
 currVal = height_list[i]
 if currVal < val1:
  colorVariable = lerp(val0,255,val1,0,currVal)
  pxVal = (0,255,int(colorVariable))
  
 if currVal < val2 and currVal >= val1:
  colorVariable = lerp(val1,0,val2,255,currVal)
  pxVal = (int(colorVariable),255,0)
  
 if currVal < val3 and currVal >= val2:
  colorVariable = lerp(val2,255,val3,0,currVal)
  pxVal = (255,int(colorVariable),0)
 color_list.append(pxVal)

ms = 512 # image size 
img = Image.new("RGB",(width,height))
print(len(color_list))
cnt = 0
for j in range(0,width):
 for k in range(0,height):
  print(j,k)
  img.putpixel((j,k),color_list[cnt])
  cnt += 1 

img.save("colorfull.png")


  

input()




