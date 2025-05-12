from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

class Application:
    def __init__(self, root):
        self.root = root
        self.root = root.title("Editor de imagenes")
        self.image = None
        self.imageTk = None
        self.image_copy = None

        self.open_button = Button(root, text="Abrir Imagen", command=self.open_image)
        self.open_button.pack()

        self.image_label = Label(root)
        self.image_label.pack()

        self.filter_label = Label(root, text="Filtro:")
        self.filter_label.pack()
        self.filter_var = StringVar(root)
        self.filter_var.set("Ninguno")
        self.filter_option = OptionMenu(root, self.filter_var, "Ninguno", "Blur", "Gaussian Blur")
        self.filter_option.pack()

        self.apply_button = Button(root, text="Aplicar", command=self.apply_button)
        self.apply_button.pack()

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Archivos de imagen", ".jpg .jpeg .png .bmp")])
        if path:
            self.image = Image.open(path) # Preparamos la imagen en python con PIL
            self.image_copy = self.image.copy()
            self.imageTk = ImageTk.PhotoImage(self.image) # Pasamos la imagen a Tkinter
            self.image_label.config(image=self.imageTk)
            self.image_label.image = 
    
    def apply_button(self):
        self.image_copy = self.image.copy()
        filter = self.filter_var.get()
        if filter == 'Blur':
            self.image_copy = self.image_copy.filter(ImageFilter.BLUR) # Modifica la imagen
        elif filter =='Sherpen':
            self.image_copy = 
            

