import os
import subprocess

# The 'r' before the quote fixes the Unicode error you just saw
PROJECT_PATH = r'C:\Users\91932\Downloads\powerbi'

def run_automation():
    try:
        # 1. Stage the metadata changes
        subprocess.run(["git", "add", "."], cwd=PROJECT_PATH, check=True)
        
        # 2. Commit the changes
        # Using a generic message for your Phase 2 documentation
        commit_result = subprocess.run(
            ["git", "commit", "-m", "Final Phase 2 Sync - Metadata Updated"], 
            cwd=PROJECT_PATH, 
            capture_output=True, 
            text=True
        )
        
        if "nothing to commit" in commit_result.stdout:
            print("ℹ️ No new changes. Your local files already match the last commit.")
        else:
            print("✅ Changes committed successfully.")

        # 3. Push to GitHub
        print("🚀 Pushing to GitHub...")
        subprocess.run(["git", "push", "origin", "main"], cwd=PROJECT_PATH, check=True)
        print("✅ Success! Your changes are now in GitHub.")

    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    run_automation()