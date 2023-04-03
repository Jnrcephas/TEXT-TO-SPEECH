import pyttsx3
import PySimpleGUI as sg

# Initialize the PySimpleGUI layout
layout = [
    [sg.Text('Enter text to speak:')],
    [sg.Multiline(size=(60, 10), key='-INPUT-')],
    [sg.Text('Select voice:'),
     sg.Combo(values=['male', 'female'], key='-VOICE-'),
     sg.Text('Select speed:'),
     sg.Slider(range=(100, 300), default_value=200, orientation='h', size=(20, 15), key='-SPEED-')],
    [sg.Button('Speak'), sg.Button('Exit')]
]


window = sg.Window('Text to Speech App', layout)


engine = pyttsx3.init()


def speak(text, voice, speed):
    # Set the voice
    if voice == 'male':
        engine.setProperty('voice', 'english+m1')
    else:
        engine.setProperty('voice', 'english+f1')
    # Set the speed
    engine.setProperty('rate', speed)
    # Speak the text
    engine.say(text)
    engine.runAndWait()


while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    elif event == 'Speak':
        text = values['-INPUT-']
        voice = values['-VOICE-']
        speed = values['-SPEED-']
        speak(text, voice, speed)


window.close()
engine.stop()
