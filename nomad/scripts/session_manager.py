import json
import sys
import os
import glob

# Store sessions in the workspace directory
SESSIONS_DIR = ".nomad_sessions"

def ensure_dir():
    if not os.path.exists(SESSIONS_DIR):
        os.makedirs(SESSIONS_DIR)

def save_state(name, data_str):
    ensure_dir()
    try:
        data = json.loads(data_str)
        filename = os.path.join(SESSIONS_DIR, f"{name}.json")
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Success: Trip state '{name}' saved.")
    except Exception as e:
        print(f"Error: Could not save state. {str(e)}")

def load_state(name):
    filename = os.path.join(SESSIONS_DIR, f"{name}.json")
    if not os.path.exists(filename):
        print(f"Error: Session '{name}' not found.")
        return
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error: Could not load state. {str(e)}")

def list_sessions():
    ensure_dir()
    files = glob.glob(os.path.join(SESSIONS_DIR, "*.json"))
    if not files:
        print("No saved sessions found.")
        return
    print("Available Nomad Sessions:")
    for f in files:
        print(f"- {os.path.basename(f)[:-5]}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python session_manager.py [save <name> <json> | load <name> | list]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "save" and len(sys.argv) >= 4:
        save_state(sys.argv[2], " ".join(sys.argv[3:]))
    elif cmd == "load" and len(sys.argv) >= 3:
        load_state(sys.argv[2])
    elif cmd == "list":
        list_sessions()
    else:
        print(f"Error: Invalid usage or unknown command {cmd}")
