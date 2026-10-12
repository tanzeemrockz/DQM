import os
from engine import init_brain, traverse
from nodes import uinput, cls

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    brain_path = os.path.join(base_dir, "brains", "main.tqm")

    try:
        data = init_brain(brain_path)
    except FileNotFoundError:
        print(f"Error: Brain not found at '{brain_path}'.")
        return
    except Exception as e:
        print(f"Error loading brain: {e}")
        return

    routes = data.get("routes", {})
    print(f"Loaded brain: {data.get('brain_id', 'unknown')} by {data.get('author', 'CyberDev')}")
    print("Type your query, or 'cls' / 'exit'.\n")

    while True:
        query = uinput("DQM $> ")
        if not query:
            continue
        if query in ["exit", "quit"]:
            break
        if query in ["cls", "clear"]:
            cls()
            continue

        print(f"\n{traverse(routes, query)}\n")

if __name__ == "__main__":
    main()