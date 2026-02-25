"""Fix notebook metadata widgets by removing `metadata['widgets']`
or ensuring it contains a `state` key (empty dict).

Usage: python scripts/fix_notebook_widgets.py path/to/notebook.ipynb
This script overwrites the notebook file in-place.
"""
import json
import sys
from pathlib import Path


def fix_widgets(obj):
    if isinstance(obj, dict):
        # If metadata has widgets, ensure 'state' exists or remove it
        if "metadata" in obj and isinstance(obj["metadata"], dict):
            md = obj["metadata"]
            if "widgets" in md:
                w = md["widgets"]
                if isinstance(w, dict):
                    # Ensure 'state' exists
                    if "state" not in w:
                        w["state"] = {}
                else:
                    # remove non-dict widgets to be safe
                    del md["widgets"]
        # Recurse
        for k, v in list(obj.items()):
            fix_widgets(v)
    elif isinstance(obj, list):
        for item in obj:
            fix_widgets(item)


def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_notebook_widgets.py notebook.ipynb")
        sys.exit(1)
    nb_path = Path(sys.argv[1])
    if not nb_path.exists():
        print(f"File not found: {nb_path}")
        sys.exit(2)

    data = json.loads(nb_path.read_text(encoding="utf-8"))
    fix_widgets(data)
    nb_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Fixed widgets in {nb_path}")


if __name__ == "__main__":
    main()
