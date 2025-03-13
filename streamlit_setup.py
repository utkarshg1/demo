import os

# Create .streamlit directory
os.makedirs(".streamlit", exist_ok=True)

# Create secrets.toml file
with open(".streamlit/secrets.toml", "w") as f:
    f.write("# Add secrets here\n")

# Create blank utility files
open("utils.py", "w").close()
open("app.py", "w").close()

# Update .gitignore
gitignore_path = ".gitignore"
entry = ".streamlit/"

# Check if entry exists in .gitignore
entry_exists = False
if os.path.exists(gitignore_path):
    with open(gitignore_path, "r") as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    entry_exists = entry in lines

# Append entry if it doesn't exist
if not entry_exists:
    with open(gitignore_path, "a") as f:
        if os.path.getsize(gitignore_path) > 0:
            f.write("\n")
        f.write(f"{entry}\n")

print("Streamlit setup completed successfully!")
print("Command to run streamlit app is below :")
print("python -m streamlit run app.py")