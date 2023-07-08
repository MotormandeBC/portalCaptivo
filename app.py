import pywifi
import tkinter as tk

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_NONE)
    profile.cipher = pywifi.const.CIPHER_TYPE_NONE

    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)

    iface.disconnect()
    iface.remove_network_profile(tmp_profile)
    profile.key = password
    iface.add_network_profile(profile)

    iface.connect(profile)

def on_wifi_connect(ssid):
    if ssid == "motorman":
        window = tk.Tk()

        label_name = tk.Label(window, text="Nombre:")
        label_name.pack()
        entry_name = tk.Entry(window)
        entry_name.pack()

        label_phone = tk.Label(window, text="Teléfono:")
        label_phone.pack()
        entry_phone = tk.Entry(window)
        entry_phone.pack()

        def connect_wifi():
            name = entry_name.get()
            phone = entry_phone.get()

            # Aquí puedes agregar la lógica para validar los datos ingresados

            # Llamar a la función para conectar a la red Wi-Fi
            connect_to_wifi(ssid, "motorman2021")

            window.destroy()

        button = tk.Button(window, text="Conectar", command=connect_wifi)
        button.pack()

        window.mainloop()

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()
scan_results = iface.scan_results()

for wifi_network in scan_results:
    ssid = wifi_network.ssid
    if ssid == "motorman":
        on_wifi_connect(ssid)
        break
