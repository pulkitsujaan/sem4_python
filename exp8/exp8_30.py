import threading
import time

class Task:
    def __init__(self, name, duration):
        self.name     = name
        self.duration = duration

    def run(self):
        print(f"[{self.name}] Started")
        time.sleep(self.duration)
        print(f"[{self.name}] Done after {self.duration}s")

tasks = [Task("Download", 2),
         Task("Upload",   1),
         Task("Process",  3)]

threads = [threading.Thread(target=t.run) for t in tasks]

for th in threads: th.start()
for th in threads: th.join()

print("All tasks complete.")