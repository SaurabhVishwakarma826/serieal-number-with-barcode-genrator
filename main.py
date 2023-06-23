
import os
import datetime
from pystrich.code128 import Code128Encoder
import PySimpleGUI as sg
import uuid


def convert_mac_to_hex(mac):
    mac_hex = mac.replace(':', '').upper()
    return mac_hex


def generate_serial_number(mac_address, expiry_date, num_cameras):
    # Convert MAC address to hexadecimal form
    mac_hex = convert_mac_to_hex(mac_address)

    # Convert expiry date to the required format (MM/DD/YYYY)
    expiry_date_obj = datetime.datetime.strptime(expiry_date, '%m/%d/%Y')
    expiry_date_str = expiry_date_obj.strftime('%y%m%d')

    # Combine MAC address, expiry date, and number of cameras to generate the serial number
    serial_number = f"M:{mac_hex}D:{expiry_date_str}C:{num_cameras}"

    # Create the directory structure for saving the barcode
    modified_mac_address = mac_address.replace(':', '_')
    save_path = os.path.join(modified_mac_address, num_cameras)
    os.makedirs(save_path, exist_ok=True)

    # Generate the barcode image using pystrich
    barcode = Code128Encoder(serial_number)
    barcode_filename = os.path.join(save_path, f"{serial_number.replace(':', '-')}.png")
    barcode.save(barcode_filename)

    sg.popup(f'Serial Number Generated: {serial_number}', f'Barcode saved at: {barcode_filename}')


# Fetch the MAC address of the PC
mac_address_pc = ':'.join(format(c, '02x') for c in uuid.getnode().to_bytes(6, 'big'))

layout = [
    [sg.Text('MAC Address:'), sg.Input(key='mac_address', default_text=mac_address_pc)],
    [sg.Text('Expiry Date:'), sg.Input(key='expiry_date'),
     sg.CalendarButton('Choose', target='expiry_date', format='%m/%d/%Y')],
    [sg.Text('Number of Cameras:'), sg.DropDown(['1', '4', '16', '32'], default_value='1', key='num_cameras')],
    [sg.Button('Generate Serial Number')]
]

window = sg.Window('Serial Number Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Generate Serial Number':
        mac_address = values['mac_address']
        expiry_date = values['expiry_date']
        num_cameras = values['num_cameras']
        generate_serial_number(mac_address, expiry_date, num_cameras)

window.close()
