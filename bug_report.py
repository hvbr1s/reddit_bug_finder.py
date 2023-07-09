import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('reddit.csv')  # replace with your file path

# Define a list of keywords that could indicate a bug
bug_keywords = ['bug', 'issue', 'problem', 'error', 'not working', 'crash', 'failure', 'stuck', 'broken']

# Create a new column 'bug_report' that indicates if the post might be reporting a bug
df['bug_report'] = df['Title'].str.contains('|'.join(bug_keywords), case=False) | df['Content'].str.contains('|'.join(bug_keywords), case=False)

# Filter the dataframe to only include potential bug reports
bug_reports = df[df['bug_report']]

# Print the bug reports with URLs
for index, row in bug_reports.iterrows():
    print(f"Title: {row['Title']}")
    print(f"URL: {row['URL']}")
    print()
