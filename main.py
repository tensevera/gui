import PySimpleGUI as sg
import random

# ''.join(random.sample(text,len(text)))

WG_TEXT = "wg_text"
WG_INPUT = "wg_input"
WG_OTOC = "wg_otoc"
WG_ZAMICHEJ = "wg_zamichej"

# vzhled aplikace - vnorene seznamy - seznam radku a kazdy radek je seznam prvku (widgetu)
vzhled = [
  [sg.Text("Napiš text do pole podemnou a stiskni tlačítko Otoč.", key=WG_TEXT)],
  [sg.Input(key=WG_INPUT)],
  [sg.Button("Otoč", key=WG_OTOC)],
   [sg.Button("Zamichej", key=WG_ZAMICHEJ)]
]

window = sg.Window("Otoč", vzhled)

while True:
  event, values = window.read()  # prectu si akci uzivatele
  if event == sg.WINDOW_CLOSED:  # krizek okna nebo tlacitko Ukoncit program
    break
  elif event == WG_OTOC:
    text = values[WG_INPUT]
    otoceny = text[::-1]
    window[WG_TEXT].update(otoceny)
  elif event == WG_ZAMICHEJ:
    text = values[WG_INPUT]
    zamichany = ''.join(random.sample(text,len(text)))
    window[WG_TEXT].update(zamichany)

window.close()