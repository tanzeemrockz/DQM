import os
from engine import ENGINE_VERSION, list_brains, load_brains, traverse
from nodes import uinput, cls

def select_brain():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    brains_dir = os.path.join(base_dir, "brains")
    available = list_brains(brains_dir)

    if not available:
        print(f"No .tqm brains found in '{brains_dir}'. Add one to start.")
        return None

    if len(available) == 1:
        chosen_brain = available[0]
        print(f"Auto-selected brain: '{chosen_brain}'")
    else:
        print("\n--- Available Brains ---")
        for idx, fname in enumerate(available, 1):
            print(f"[{idx}] {fname}")

        choice = input("\nSelect a brain (number or 'Enter' for default):").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(available):
            chosen_brain = available[int(choice) -1]
        else:
            chosen_brain = "main.tqm" if "main.tqm" in available else available[0]

    filepath = os.path.join(brains_dir, chosen_brain)
    return load_brains(filepath)

def main():
    print(f"--- DQM v{ENGINE_VERSION} ---")

    data = select_brain()
    if not data:
        return

    routes = data.get("routes", {})
    brain_id = data.get("brain_id", "Unknown")
    version = data.get("version", "1.0.0")
    author = data.get("author", "Anonymous")
    info = data.get("info", "No info available")

    print(f"\nLoaded: {brain_id} (v{version}) by {author}")
    print(f"Info: {info}")
    print("Type your query, or 'cls' / 'exit'.\n")

    while True:
        query = uinput("DQM $> ")
        if not query:
            continue

        if query in ["break", "exit", "quit"]:
            break

        if query in ["cls", "clear"]:
            cls()
            continue

        print(f"\n{traverse(routes, query)}\n")

if __name__ == "__main__":
    main()