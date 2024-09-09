import os
import platform
import datetime

def display_runner_info():
    print("Runner Information:")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.release()}")
    print(f"Machine Type: {platform.machine()}")
    
    # Get environment variables from GitHub Actions
    event_name = os.getenv('GITHUB_EVENT_NAME')
    workflow = os.getenv('GITHUB_WORKFLOW')
    runner_name = os.getenv('RUNNER_NAME')
    job_name = os.getenv('GITHUB_JOB')
    trigger = os.getenv('GITHUB_EVENT_PATH')
    
    print("\nGitHub Action Environment:")
    print(f"Event: {event_name}")
    print(f"Workflow: {workflow}")
    print(f"Runner: {runner_name}")
    print(f"Job: {job_name}")
    print(f"Trigger file path: {trigger}")
    
    print(f"\nCurrent Time: {datetime.datetime.now()}")

if __name__ == "__main__":
    display_runner_info()
