import threading
import requests
import re
import urllib3
import time
from urllib.parse import urlparse, parse_qs, urljoin
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TurboApp(App):
    def build(self):
        # UI Layout အပြင်အဆင်
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Background ကို Transparent ဆန်ဆန် အရောင်ဖျော့ ထည့်ခြင်း
        with self.root.canvas.before:
            Color(0.1, 0.1, 0.1, 0.7) # 0.7 သည် Transparency (ကြည်လင်မှု) ဖြစ်သည်
            self.rect = Rectangle(size=(2000, 2000), pos=self.root.pos)

        # Labels များ
        self.title_label = Label(text="[b]Ruijie Router Turbo Script[/b]", markup=True, font_size='20sp', color=(0, 1, 1, 1))
        self.status_label = Label(text="Status: Ready", font_size='16sp')
        self.dev_label = Label(text="Developed by htlwin using AI", font_size='12sp', color=(0.7, 0.7, 0.7, 1))

        # Start Button
        self.start_btn = Button(text="START", size_hint=(1, 0.2), background_color=(0, 0.8, 0, 1))
        self.start_btn.bind(on_press=self.start_process_thread)

        # Stop Button (အစမှာ ဝှက်ထားမည်)
        self.stop_btn = Button(text="STOP", size_hint=(1, 0.2), background_color=(0.8, 0, 0, 1))
        self.stop_btn.bind(on_press=self.stop_process)
        
        # Widgets များ ထည့်ခြင်း
        self.root.add_widget(self.title_label)
        self.root.add_widget(self.status_label)
        self.root.add_widget(self.start_btn)
        self.root.add_widget(self.dev_label)

        self.running = False
        return self.root

    def update_status(self, text):
        self.status_label.text = f"Status: {text}"

    def start_process_thread(self, instance):
        if not self.running:
            self.running = True
            self.update_status("Running (Ruijie Target Only)")
            
            # Start ခလုတ်ကိုဖယ်ပြီး Stop ခလုတ်ထည့်ခြင်း
            self.root.remove_widget(self.start_btn)
            self.root.add_widget(self.stop_btn, index=1)
            
            # နောက်ကွယ်မှာ အလုပ်လုပ်ဖို့ Thread အသစ်ဖွင့်ခြင်း
            threading.Thread(target=self.main_logic, daemon=True).start()

    def stop_process(self, instance):
        self.running = False
        self.update_status("Stopped")
        self.root.remove_widget(self.stop_btn)
        self.root.add_widget(self.start_btn, index=1)

    def main_logic(self):
        # သင်ပေးထားသော logic များကို ဤနေရာတွင် ထည့်သွင်းထားသည်
        while self.running:
            session = requests.Session()
            try:
                # Connectivity Check
                r = requests.get("http://connectivitycheck.gstatic.com/generate_204", timeout=5)
                if r.status_code == 204:
                    Clock.schedule_once(lambda dt: self.update_status("Internet OK"), 0)
                    time.sleep(5)
                    continue

                portal_url = r.url
                # ... (သင့် code ထဲမှ logic များ ဤနေရာတွင် ဆက်လက်ပတ်မည်) ...
                # SID ရှာဖွေခြင်း နှင့် Voucher API ပို့ခြင်းများ ပြုလုပ်ရန်
                
            except Exception as e:
                Clock.schedule_once(lambda dt: self.update_status(f"Error: Connection Lost"), 0)
                time.sleep(5)
