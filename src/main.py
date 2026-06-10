import os
import time
import yaml
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, settings):
        self.settings = settings

    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}. Triggering sync...")
            # trigger sync here

def load_settings():
    with open('config/settings.yaml', 'r') as f:
        return yaml.safe_load(f)

def main():
    settings = load_settings()
    print(f"Starting {settings['project_name']}...")
    
    if settings.get('backup', {}).get('real_time'):
        observer = Observer()
        handler = ChangeHandler(settings)
        source_dir = settings['backup']['source_dir']
        
        # Ensure dir exists
        os.makedirs(source_dir, exist_ok=True)
        
        observer.schedule(handler, source_dir, recursive=True)
        observer.start()
        print(f"Watching {source_dir} for changes...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        print("Real-time watching is disabled. Running one-time sync...")

if __name__ == "__main__":
    main()
