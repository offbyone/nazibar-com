import os
import sys
from pathlib import Path

# Ensure the root is in the Python path
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from publishconf import *  # noqa: E402

pr_number = os.getenv("PR_NUMBER", "unknown")

# Override SITEURL for GitHub Pages PR preview
SITEURL = f"https://offbyone.github.io/nazibar-com/pr-{pr_number}"
