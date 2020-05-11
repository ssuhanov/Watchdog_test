from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            filename_components = filename.split(".")
            if len(filename_components) <= 1:
                continue

            extension = filename_components[1].lower()
            if extension in ["jpg", "jpeg", "png"]:
                file = folder_track + "/" + filename
                new_path = folder_destination + "/" + filename
                os.rename(file, new_path)


folder_track = 'Test_data'
folder_destination = 'Test_data/Images'

handler = Handler()
observer = Observer()
observer.schedule(handler, folder_track, recursive=True)
observer.start()

try:
    while (True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
