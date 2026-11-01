"""Interactive launcher for all AI laboratory experiments."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
EXPERIMENTS = {
    "1": "experiment_01_agents/main.py",
    "2": "experiment_02_environments/main.py",
    "3": "experiment_03_local_search/main.py",
    "4": "experiment_04_uninformed_search/main.py",
    "5": "experiment_05_heuristic_search/main.py",
    "6": "experiment_06_adversarial_search/main.py",
    "7": "experiment_07_csp/main.py",
    "8": "experiment_08_knowledge_base/main.py",
    "9": "experiment_09_uncertainty/main.py",
}


def main() -> None:
    print("AI Laboratory Programs")
    for number, file_name in EXPERIMENTS.items():
        print(f"  {number}. {file_name.split('/')[0]}")
    choice = input("Choose experiment (1-9): ").strip()
    target = EXPERIMENTS.get(choice)
    if not target:
        print("Please choose a number from 1 to 9.")
        return
    subprocess.run([sys.executable, str(ROOT / target)], check=False)


if __name__ == "__main__":
    main()
