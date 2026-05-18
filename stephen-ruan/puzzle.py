import os

files = []
directory = "/workspaces/weekly-meetings/stephen-ruan/"

# os.walk automatically loops through the directory, subdirectories, and files
for root, dirs, filenames in os.walk(directory):
    for filename in filenames:
        full_path = os.path.join(root, filename)
        files.append(full_path)

for file in files:
    # This still correctly protects puzzle.py in the main directory
    if file == f"{directory}/puzzle.py":
        continue
    else:
        # os.walk only returns files in 'filenames', so os.remove is safe to use here
        os.remove(file)
