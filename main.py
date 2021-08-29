from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
import pytube


Builder.load_file("main.kv")
Window.size = (360,500)

class MainScreen(Widget):
    image_loaded = False

    def set_assets(self, thumbnail, title):
        self.ids.thumbnail.source = thumbnail
        self.ids.title.text = title
        
    def get_video(self, stream):
        if self.image_loaded == True:
            stream.download()

    def download_video(self, url):
        yt = pytube.YouTube(url)
        self.set_assets(yt.thumbnail_url, yt.title)
        self.image_loaded = True
        Clock.schedule_once(lambda x: self.get_video(yt.streams.first()), 4)


class YoutubeDownloadApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    YoutubeDownloadApp().run()