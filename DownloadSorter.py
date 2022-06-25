from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

separ = os.sep
track = input("Введите путь для папки с вашими загрузками:")
folder_track = track
folder_dest_1 = "D:Загрузки/Изображения"
folder_dest_2 = "D:Загрузки/Архивы"
folder_dest_3 = "D:Загрузки/Музыка"
folder_dest_4 = "D:Загрузки/Установщики"
folder_dest_5 = "D:Загрузки/Торренты"

for file in os.listdir(folder_track):
    if os.path.isfile(folder_track + separ + file):
        filename_new, extension = os.path.splitext(file)
        os.rename(folder_track + separ + file,
                  folder_track + separ + filename_new.replace(".", "_").replace("+", "_") + extension)


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename_new in os.listdir(folder_track):
            extension = filename_new.split(".")
            if len(extension) > 1 and (extension[1].lower() == "png" or extension[1].lower() == "jpg" or extension[1].lower() == "jpeg" or extension[1].lower() == "webp"):
                file = folder_track + "/" + filename_new
                new_path = folder_dest_1 + "/" + filename_new
                os.rename(file, new_path)
            if len(extension) > 1 and (extension[1].lower() == "zip"):
                file = folder_track + "/" + filename_new
                new_path = folder_dest_2 + "/" + filename_new
                os.rename(file, new_path)
            if len(extension) > 1 and (
                    extension[1].lower() == "mp3" or extension[1].lower() == "flac" or extension[1].lower() == "wav"):
                file = folder_track + "/" + filename_new
                new_path = folder_dest_3 + "/" + filename_new
                os.rename(file, new_path)
            if len(extension) > 1 and (extension[1].lower() == "exe"):
                file = folder_track + "/" + filename_new
                new_path = folder_dest_4 + "/" + filename_new
                os.rename(file, new_path)
            if len(extension) > 1 and (extension[1].lower() == "torrent"):
                file = folder_track + "/" + filename_new
                new_path = folder_dest_5 + "/" + filename_new
                os.rename(file, new_path)


handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
print("Monitoring started")
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
