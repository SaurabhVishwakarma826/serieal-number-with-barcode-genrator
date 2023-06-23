import tkinter as tk
import barcode
from barcode.writer import ImageWriter
from PIL import ImageTk, Image


def generate_barcode():
    mac_address = mac_entry.get()
    expiry_date = expiry_entry.get()
    num_camera = num_camera_entry.get()

    serial_number = f"M:{mac_address.replace(':', '')} D:{expiry_date.replace('/', '')} C:{num_camera}"

    barcode_class = barcode.get_barcode_class('code128')
    barcode_image = barcode_class(serial_number, writer=ImageWriter())

    # Generate barcode image
    filename = "barcode"
    barcode_image.save(filename)
    readFile = 'barcode.png'
    # Display barcode image in the GUI
    img = ImageTk.PhotoImage(Image.open(readFile))
    barcode_label.config(image=img)
    barcode_label.image = img


# Create the main window
window = tk.Tk()
window.title("Barcode Generator")

# Create labels and entry fields
mac_label = tk.Label(window, text="MAC Address:")
mac_label.pack()
mac_entry = tk.Entry(window)
mac_entry.pack()

expiry_label = tk.Label(window, text="Expiry Date:")
expiry_label.pack()
expiry_entry = tk.Entry(window)
expiry_entry.pack()

num_camera_label = tk.Label(window, text="Number of Cameras:")
num_camera_label.pack()
num_camera_entry = tk.Entry(window)
num_camera_entry.pack()

# Create buttons
generate_button = tk.Button(window, text="Generate Barcode", command=generate_barcode)
generate_button.pack()

# read_button = tk.Button(window, text="Read Barcode", command=read_barcode)
# read_button.pack()

# Create a label to display the generated barcode
barcode_label = tk.Label(window)
barcode_label.pack()

# Start the main loop
window.mainloop()
