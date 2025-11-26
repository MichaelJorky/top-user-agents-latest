
import random
import os

def load_all_user_agents(base_path="data"):
    ua = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file)) as f:
                    ua.extend([x.strip() for x in f.readlines()])
    return ua

if __name__ == "__main__":
    agents = load_all_user_agents()
    print(random.choice(agents) if agents else "No user agents found")
