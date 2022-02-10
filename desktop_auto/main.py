import sys
import time
import logging
import shutil
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = "/Users/Eric/Desktop" #path to track
ext = ['*.txt', '*.png', '*.jpeg', '*.jpg', '*.mp4']


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=[ext], ignore_patterns = None, ignore_directories = False, case_sensitive = True)
      

    def on_created(self, event):
        print(f"File was moved to {event.src_path}")
        if event.src_path.endswith(ext[0]):
            shutil.move(event.src_path, r'/Users/Eric/Documents')
        elif event.src_path.endswith(ext[1]):
            shutil.move(event.src_path, r'/Users/Eric/Pictures')
        elif event.src_path.endswith(ext[2]):
            shutil.move(event.src_path, r'/Users/Eric/Pictures')
        elif event.src_path.endswith(ext[3]):
            shutil.move(event.src_path, r'/Users/Eric/Pictures')
        elif event.src_path.endswith(ext[4]):
            shutil.move(event.src_path, r'/Users/Eric/Movies')

    def on_deleted(self,event):
        print("deleted")

    def on_modified(self, event):
        print("modified")

    def on_moved(self, event):
        print("moved")

if __name__ == "__main__":


    event_handler = FileSystemEventHandler()


    #calling the class handler
    event_handler = Handler() 

     
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()