import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MarkdownHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.md'):
            self.update_json(event.src_path)

    def update_json(self, md_file):
        # Read the content of the MD file
        with open(md_file, 'r') as file:
            content = file.read()

        # Prepare the data to be written to JSON
        data = {
            'filename': os.path.basename(md_file),
            'content': content
        }

        # Write to JSON file
        with open('output.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    path = '.'  # Directory to watch
    event_handler = MarkdownHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
