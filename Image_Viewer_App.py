from tkinter import *
from PIL import ImageTk, Image



root = Tk()

root.title("Image Viewer")
root.iconbitmap('D:\SDE\Py\Bookshop_icon_2.ico')
my_img=ImageTk.PhotoImage(Image.open("D:\SDE\Py\Images\img.jpg"))

#my_img1=ImageTk.PhotoImage(Image.open("Saved_Pics/cmp.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("D:\SDE\Py\Images\img1.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("D:\SDE\Py\Images\img2.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("D:\SDE\Py\Images\img3.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("D:\SDE\Py\Images\img4.jpg"))

#packing in to a list
my_images=[my_img,my_img2,my_img3,my_img4,my_img5]

my_label=Label(image=my_img)
my_label.grid(row=0,column=0,columnspan=3)
def back(image_no):
   global my_label
   global button_forward
   global button_back
   my_label.grid_forget()
   my_label=Label(image=my_images[image_no-1])
   my_label.grid(row=0,column=0,columnspan=3)
   if(image_no==1):
      button_back=Button(root, text="<</back",state=DISABLED,command=lambda:back(image_no-1),bg="yellow")
   else:
      button_back=Button(root, text="<</back", command=lambda:back(image_no-1),bg="yellow")
      button_forward=Button(root, text=">>/forward",command=lambda:forward(image_no+1),bg="Green")
      button_back.grid(row=1,column=0)
      button_forward.grid(row=1,column=2)
def forward(image_no):
   global my_label
   global button_forward
   global button_back
   #if we add the label again , then it will be shown over the print_environ_usage
   # so we need to get rid of that 
   my_label.grid_forget()
   my_label=Label(image=my_images[image_no-1])
   my_label.grid(row=0,column=0,columnspan=3)
   if(image_no==1):
      button_back=Button(root, text=">>/forward",state=DISABLED,command=lambda:back(image_no-1),bg="yellow")
   if(image_no==len(my_images)):
      button_forward=Button(root, text=">>/forward",state=DISABLED)#,command=lambda:forward(image_no+1)) or command is not given.
   else:
      button_back=Button(root, text="<</back", command=lambda:back(image_no-1),bg="yellow")
      button_forward=Button(root, text=">>/forward",command=lambda:forward(image_no+1),bg="green")
      button_back.grid(row=1,column=0)
      button_forward.grid(row=1,column=2)
   

button_back=Button(root, text="<</back",command=lambda: back(1), state=DISABLED,bg="yellow") #can write without using lambda for back function which is disbaled
button_forward=Button(root, text=">>/forward",command=lambda:forward(2),bg="green")
button_exit=Button(root, text="EXIT", command=root.quit,bg="Red")
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)


root.mainloop()