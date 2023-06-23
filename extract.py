def extract_values(serial_number):
    # Extract MAC address
    mac_start_index = serial_number.index('M:') + 2
    mac_end_index = serial_number.index('D:')
    mac_address = serial_number[mac_start_index:mac_end_index]
    mac_address = ':'.join(mac_address[i:i + 2] for i in range(0, len(mac_address), 2))

    # Extract expiry date
    date_start_index = serial_number.index('D:') + 2
    date_end_index = serial_number.index('C:')
    expiry_date = serial_number[date_start_index:date_end_index]
    expiry_date = '/'.join(expiry_date[i:i + 2] for i in range(0, len(expiry_date), 2))

    # Extract number of cameras
    cameras_start_index = serial_number.index('C:') + 2
    num_cameras = serial_number[cameras_start_index:]

    return mac_address, expiry_date, num_cameras


def main():
    serial_number = 'M:001122334455D:230623C:4'
    mac_address, expiry_date, num_cameras = extract_values(serial_number)

    print('Mac Address:', mac_address)
    print('Expiry Date:', expiry_date)
    print('Number of Cameras:', num_cameras)


if __name__ == '__main__':
    main()
