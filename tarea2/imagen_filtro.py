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

        self.open_button = Button(root, text="Abrir imagen", command=self.open_image)
        self.open_button.pack()

        self.image_label = Label(root)
        self.image_label.pack()

        self.filter_label = Label(root, text="Filtro:")
        self.filter_label.pack()
        self.filter_var = StringVar(root)
        self.filter_var.set("Ninguno")
        self.filter_option = OptionMenu(root, self.filter_var, "Ninguno", "Emboos", "Gaussian Blur", "Contour", "Detail")
        self.filter_option.pack()

        self.radio_label = Label(root, text="Radio para Gaussian Blur")
        self.radio_label.pack()
        self.radio_entry = Entry(root)
        self.radio_entry.pack()

        self.apply_button = Button(root, text="Aplicar", command=self.apply_button)
        self.apply_button.pack()

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Archivos de imagen", ".jpg .jpeg .png .bmp")])
        if path:
            self.image = Image.open(path) # Preparamos la imagen en python con PIL
            self.image_copy = self.image.copy()
            self.imageTk = ImageTk.PhotoImage(self.image_copy) # La pasamos a Tkinter
            self.image_label.config(image=self.imageTk)
            self.image_label.image = self.imageTk

    def apply_button(self):
        self.image_copy = self.image.copy()
        filter = self.filter_var.get()
        if filter == 'Emboos':
            self.image_copy = self.image_copy.filter(ImageFilter.EMBOSS) # Modifica imagen
        elif filter == 'Contour':
            self.image_copy = self.image_copy.filter(ImageFilter.CONTOUR) # Modifica imagen
        elif filter == 'Gaussian Blur':
            # Esperamos un numero
            try:
                radio = int(self.radio_entry.get())
                self.image_copy = self.image_copy.filter(ImageFilter.GaussianBlur(radius=radio))
            except ValueError:
                print("Error: El radio debe ser un número entero")
        elif filter == 'Detail':
            self.image_copy = self.image_copy.filter(ImageFilter.DETAIL)
        
        # Vuelve a recrearla para pintarla una vez mas
        self.imageTk = ImageTk.PhotoImage(self.image_copy)
        self.image_label.config(image=self.imageTk)
        self.image_label.image = self.imageTk

root = Tk()
app = Application(root)
root.mainloop()
