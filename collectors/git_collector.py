import subprocess
import os
import requests

def get_git_activity():
    """
    Hybrid Collector: Fetches local logs AND global GitHub activity.
    Ensures your Mentor sees HER work, not yours.
    """
    # 1. Identify the User (Auto-detect or Config)
    username = "Unknown_User"
    if os.path.exists("github_user.txt"):
        with open("github_user.txt", "r") as f:
            username = f.read().strip()
    else:
        try:
            # Tries to get the name from the mentor's system Git settings
            username = subprocess.check_output(
                ["git", "config", "user.name"], 
                stderr=subprocess.STDOUT, shell=True
            ).decode("utf-8").strip()
        except:
            pass

    combined_activity = []

    # 2. Get LOCAL Activity (What they are doing right now)
    try:
        if os.path.exists(".git"):
            local_log = subprocess.check_output(
                ["git", "log", "-n 5", "--pretty=format:%s"],
                shell=True, stderr=subprocess.STDOUT
            ).decode("utf-8").strip()
            if local_log:
                combined_activity.extend(local_log.split("\n"))
    except:
        pass

    # 3. Get GLOBAL Activity (What is on GitHub.com)
    if username and username != "Unknown_User":
        try:
            url = f"https://api.github.com/users/{username}/events/public"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                events = response.json()
                # Extract the last 5 push commit messages
                global_commits = [
                    e['payload']['commits'][0]['message'] 
                    for e in events 
                    if e['type'] == 'PushEvent' and 'commits' in e['payload']
                ]
                combined_activity.extend(global_commits[:5])
        except:
            pass

    # 4. Final Cleanup
    # Remove duplicates and return
    unique_activity = list(set(combined_activity))
    
    if not unique_activity:
        return ["No recent coding activity found. Time to start a new project!"]
    
    return unique_activity