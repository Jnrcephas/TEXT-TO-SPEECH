import qrcode
import PySimpleGUI as sg


layout = [
    [sg.Text('Enter the text or link to encode:')],
    [sg.InputText(key='-INPUT-')],
    [sg.Button('Generate QR Code'), sg.Button('Exit')]
]

window = sg.Window('CN QR Code Generator', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Generate QR Code':
        # Create the QR code image using qrcode library
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(values['-INPUT-'])
        qr.make(fit=True)
        img = qr.make_image(fill_color='red', back_color='white')
        
        
        filename = 'qrcode.png'
        img.save(filename)
        
        sg.popup(f'QR Code image saved as {filename} in the current directory.')

window.close()
