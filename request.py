import requests

url = "http://localhost:9696/"

device = {
         'battery_power': 981.0,
         'blue': 1.0,
         'clock_speed': 1.9,
         'dual_sim': 1.0,
         'fc': 0.0,
         'four_g': 0.0,
         'int_memory': 2.0,
         'm_dep': 0.1,
         'mobile_wt': 10.0,
         'n_cores': 3.0,
         'pc': 7.0,
         'px_height': 35.0,
         'px_width': 688.0,
         'ram': 400.0,
         'sc_h': 19.0,
         'sc_w': 12.0,
         'talk_time': 19.0,
         'three_g': 0.0,
         'touch_screen': 0.0,
         'wifi': 0.0
}

response = requests.post(url, json=device).json()
predicted_class = response['price_range']

print(f"The price_range for this device is {predicted_class}")