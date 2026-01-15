import os
import subprocess

# The folder where your AdventureWorks files are
PROJECT_PATH = r'C:\Users\91932\Downloads\powerbi'

def run_automation():
    try:
        # Stage the changes you made in model.tmdl
        subprocess.run(["git", "add", "."], cwd=PROJECT_PATH, check=True)
        # Commit the changes
        subprocess.run(["git", "commit", "-m", "Manual edit in TMDL - pushed via Python"], cwd=PROJECT_PATH, check=True)
        # Push to GitHub
        subprocess.run(["git", "push", "origin", "main"], cwd=PROJECT_PATH, check=True)
        
        print("✅ Success: Metadata changes pushed to GitHub.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_automation()