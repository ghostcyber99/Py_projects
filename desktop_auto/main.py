import sys
import time
import logging
import shutil
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = "/Users/Eric/Desktop" #path to track


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.txt'], ignore_patterns = None, ignore_directories = False, case_sensitive = True)
      

    def on_created(self, event):
        print("created")

    def on_deleted(self,event):
        print("deleted")

    def on_modified(self, event):
        print("modified")

    def on_moved(self, event):
        print("moved")

if __name__ == "__main__":

    #event_handler = FileSystemEventHandler()


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