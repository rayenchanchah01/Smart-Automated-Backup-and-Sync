# Smart Automated Backup and Sync

A background application in Python for automated file backup and synchronization.

## Features
- Local to Local Sync
- Real-time Directory Watching (Watchdog)
- Local to Cloud Sync (AWS S3 using Boto3)

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Update `config/settings.yaml` with your preferred directories and AWS Bucket name.
3. Run the application: `python src/main.py`
