from setuptools import setup
import os
import subprocess

# Define dependencies once
dependencies = [
    "streamlit",
    "requests",
    "numpy",
    "pandas",
    "plotly"
]

def create_project_structure():
    """Create necessary files and directories for the Streamlit project."""
    os.makedirs(".streamlit", exist_ok=True)

    # Create secrets.toml
    with open(".streamlit/secrets.toml", "w") as f:
        f.write("# Add secrets here\n")

    # Create utility and app files
    for filename in ["utils.py", "app.py"]:
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("# Write your code here\n")

    # Update .gitignore
    gitignore_path = ".gitignore"
    entry = ".streamlit/"

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            lines = [line.strip() for line in f.readlines()]
        if entry not in lines:
            with open(gitignore_path, "a") as f:
                f.write(f"\n{entry}\n")
    else:
        with open(gitignore_path, "w") as f:
            f.write(f"{entry}\n")

    print("✅ Streamlit setup completed successfully!")

def upgrade_pip():
    """Upgrade pip to the latest version."""
    print("⬆️ Upgrading pip...")
    subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)

def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    subprocess.run(["pip", "install"] + dependencies, check=True)

def create_requirements_file():
    """Create a requirements.txt file with dependencies."""
    with open("requirements.txt", "w") as f:
        for dep in dependencies:
            f.write(dep + "\n")
    print("✅ requirements.txt created successfully!")

# Run setup tasks
create_project_structure()
upgrade_pip()
install_dependencies()
create_requirements_file()

# Define setup
setup(
    name="StreamlitProjectSetup",
    version="0.1",
    description="A simple setup script for initializing a Streamlit project",
    install_requires=dependencies,
)
