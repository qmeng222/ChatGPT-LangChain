# ChatGPT-LangChain

## About:

- Description: Production-ready apps focused on real-world AI integration.
- Highlights:
- Tech stack: ChatGPT, LangChain, Python
- Overview:
  - Programming workflow: ![What's going on inside my code?](images/programming-workflow.png)
  - Connecting chains (the output from Chain A serves as the input for Chain B): ![Connecting chains](/images/connecting-chains.png)

## Setup:

1. (For project isolation) create & activate a virtual environment (dependencies are installed within the virtual environment other than system-wide & all subsequent steps will be performed within the virtual environment):
   ```
   python -m venv env
   source env/bin/activate
   ```
2. Upgrade the pip package manager to the latest version within the current Python environment: `python -m pip install --upgrade pip`
3. Install libraries/packages:
   - Install the **_openai_** package with a version that is strictly before 1.0.0 (ensuring compatibility with versions before the major release) and the latest version of the **_langchain_** package:
     ```
     pip install "openai<1.0.0" langchain
     pip show openai langchain # display info about the installed packages
     ```
   - Install the python-dotenv library: `pip install python-dotenv`
4. Create a symbolic link in the current working directory from the .env file under the root directory (now each project depends on the central .env file under root):
   - `ln -s ../.env .env` (using a relative path to create a symbolic link)
   - or `ln -s /.env .env` (using the absolute path)
   - or more generally `ln -s </target-directory/target-file> </symlink-directory/example-symlink>` (The </symlink-directory/> is optional. If not specified, the symlink is created in the current working directory.)
5. Generate a snapshot of the installed packages and their versions to the requirements.txt file (or overwrite the txt file): `pip freeze > requirements.txt`, so others can install all the packages and their respective versions specified in the requirements.txt file with `pip install -r requirements.txt`
6. Run the code: `python main.py`

## Resources:

1. [.gitignore File – How to Ignore Files and Folders in Git](https://www.freecodecamp.org/news/gitignore-file-how-to-ignore-files-and-folders-in-git/)
2. [Create a symbolic link in Unix](https://kb.iu.edu/d/abbe)
