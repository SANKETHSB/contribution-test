import os
import random
from datetime import datetime, timedelta
import argparse

def create_commits(repo_url):
    # Create a file to modify
    with open('contribution.txt', 'w') as f:
        f.write('Initial content')
    
    # Add and commit the file
    os.system('git add .')
    os.system('git commit -m "Initial commit"')
    
    # Generate commits for the past year
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    current_date = start_date
    
    while current_date <= end_date:
        # Random number of commits per day (0-5)
        num_commits = random.randint(0, 5)
        
        for _ in range(num_commits):
            # Modify the file
            with open('contribution.txt', 'a') as f:
                f.write(f'\nCommit on {current_date.strftime("%Y-%m-%d")}')
            
            # Create commit with specific date
            commit_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
            os.system('git add .')
            os.system(f'git commit -m "Contribution for {commit_date}"')
        
        current_date += timedelta(days=1)
    
    # Add remote and push
    os.system(f'git remote add origin {repo_url}')
    os.system('git branch -M main')
    os.system('git push -u origin main -f')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--repository', required=True, help='GitHub repository URL')
    args = parser.parse_args()
    
    create_commits(args.repository)