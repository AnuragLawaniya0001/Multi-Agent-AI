# view_memory.py

import sys
from Memory.shared_memory import list_all

def display(thread_id: str = None):
    memory = list_all()

    if not memory:
        print("No memory stored.")
        return

    if thread_id:
        entry = memory.get(thread_id)
        if not entry:
            print(f"No memory found for thread ID: {thread_id}")
        else:
            print(f"\n🧵 Thread ID: {thread_id}")
            for key, val in entry.items():
                print(f"  {key}: {val}")
    else:
        # Display all
        for tid, entry in memory.items():
            print(f"\n🧵 Thread ID: {tid}")
            for key, val in entry.items():
                print(f"  {key}: {val}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        thread_id_arg = sys.argv[1]
        display(thread_id_arg)
    else:
        display()
