import json
import sys
import os

STATE_FILE = "nomad_state.json"

def save_state(data_str):
    try:
        data = json.loads(data_str)
        with open(STATE_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Success: Trip state saved to {STATE_FILE}")
    except Exception as e:
        print(f"Error: Could not save state. {str(e)}")

def load_state():
    if not os.path.exists(STATE_FILE):
        print(f"Info: No existing trip state found at {STATE_FILE}")
        return
    try:
        with open(STATE_FILE, 'r') as f:
            data = json.load(f)
            print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error: Could not load state. {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python session_manager.py [save <json> | load]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "save":
        save_state(" ".join(sys.argv[2:]))
    elif cmd == "load":
        load_state()
    else:
        print(f"Error: Unknown command {cmd}")
