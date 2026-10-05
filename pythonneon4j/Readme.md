````markdown
# Python + Neo4j Development Environment

## Project Description

This project sets up a Python development environment for connecting a Python application with Neo4j AuraDB.

The purpose of this project is to configure and verify:

- Python
- VS Code
- Git
- GitHub
- Python virtual environment
- Neo4j Python Driver
- Python dotenv
- Neo4j AuraDB
- GitHub repository

The project also demonstrates a successful connection between Python and Neo4j AuraDB by creating a test node.

---

## Technologies Used

- Python
- VS Code
- Git
- GitHub
- Neo4j AuraDB
- Neo4j Python Driver
- python-dotenv

---

## Project Structure

```text
pythonneon4j/
│
├── .venv/                 # Python virtual environment (not pushed to GitHub)
├── .env                   # Neo4j credentials (not pushed to GitHub)
├── .gitignore             # Files excluded from Git
├── database.py            # Neo4j connection configuration
├── main.py                # Neo4j connection and test node creation
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
````

---

## Python Virtual Environment

A Python virtual environment was created using:

```powershell
python -m venv .venv
```

The virtual environment is activated using:

```powershell
.venv\Scripts\activate
```

---

## Required Packages

The project uses the following Python packages:

* `neo4j`
* `python-dotenv`

Install all required packages using:

```powershell
pip install -r requirements.txt
```

---

## Neo4j AuraDB Configuration

A Neo4j AuraDB cloud database is used for this project.

The Neo4j connection details are stored in a `.env` file.

Example:

```env
NEO4J_URI=neo4j+s://your-database.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

The actual `.env` file is not committed to GitHub because it contains sensitive credentials.

---

## Neo4j Connection

The Neo4j Python Driver is used to connect to Neo4j AuraDB.

The connection is verified using:

```python
driver.verify_connectivity()
```

Run the connection test using:

```powershell
python database.py
```

Expected output:

```text
Neo4j connection successful!
```

---

## Test Node Creation

The `main.py` file creates a test node in Neo4j.

Run:

```powershell
python main.py
```

Expected output:

```text
Connecting to Neo4j...
Neo4j connection successful!
Created node: Hello Neo4j
```

The created node can be verified in Neo4j Aura using:

```cypher
MATCH (n:TestNode)
RETURN n;
```

The result should display:

```text
TestNode
message: "Hello Neo4j"
```

---

## Git and GitHub

Git is used for version control and GitHub is used to store the project repository.

The project includes a `.gitignore` file to prevent sensitive and unnecessary files from being uploaded.

The following files are excluded:

```text
.venv/
.env
__pycache__/
*.pyc
```

---

## Verification

The following setup components were successfully verified:

* Python installation
* pip installation
* Python virtual environment
* Required Python packages
* Git installation
* Neo4j AuraDB connection
* Python to Neo4j connectivity
* Test node creation in Neo4j
* GitHub repository setup

---

## Conclusion

The Python + Neo4j development environment has been successfully configured.

Python is able to connect to Neo4j AuraDB using the Neo4j Python Driver, and a test node was successfully created and verified in the Neo4j database.

````

---

# 2. Check `.gitignore` BEFORE pushing

Your `.gitignore` should contain:

```gitignore id="6m9w2r"
.venv/
.env
__pycache__/
*.pyc
````

**This is extremely important because `.env` contains your Neo4j password.**

---

# 3. Check your project

In VS Code terminal:

```powershell id="r9v9yq"
dir
```

You should have approximately:

```text
database.py
main.py
README.md
requirements.txt
.gitignore
.venv
.env
```

---

# 4. Check Git

Run:

```powershell id="f3x0f6"
git --version
```

Then:

```powershell id="8f1b1h"
git status
```

You should **NOT** see:

```text
.env
.venv
```

in the files that Git wants to commit.

---

# 5. Initialize Git

If you haven't already done this:

```powershell id="8x3d7p"
git init
```

Then:

```powershell id="7w7e1j"
git status
```

---

# 6. Add your files

Run:

```powershell id="0t6q1m"
git add .
```

Then check:

```powershell id="x6o6d4"
git status
```

You should see files such as:

```text
.gitignore
README.md
database.py
main.py
requirements.txt
```

You should **NOT** see:

```text
.env
.venv
```

If `.env` appears, **STOP** and don't commit yet.

---

# 7. Commit

Run:

```powershell id="6b5d0a"
git commit -m "Initial Python Neo4j project setup"
```

You should get something similar to:

```text
[main ...] Initial Python Neo4j project setup
...
files changed
```

---

# 8. Create GitHub repository

Go to GitHub and create a **new repository**.

For example:

```text
pythonneon4j
```

You can keep it **Public** if your assignment requires the reviewer to access it.

When creating the repository, **don't add**:

* README
* .gitignore
* License

because you already created them locally.

---

# 9. Connect your local project to GitHub

GitHub will show a repository URL similar to:

```text
https://github.com/YOUR_USERNAME/pythonneon4j.git
```

In your VS Code terminal:

```powershell id="9x8d8k"
git remote add origin https://github.com/YOUR_USERNAME/pythonneon4j.git
```

Replace `YOUR_USERNAME` with your actual GitHub username.

Check:

```powershell id="y1bq4q"
git remote -v
```

You should see your GitHub repository URL.

---

# 10. Push to GitHub

Run:

```powershell id="w2g9n6"
git branch -M main
```

Then:

```powershell id="q1f8m5"
git push -u origin main
```

If GitHub asks you to authenticate, complete the GitHub authentication.

---

# 11. Verify GitHub

Refresh your GitHub repository.

You should see:

```text
pythonneon4j
│
├── .gitignore
├── README.md
├── database.py
├── main.py
└── requirements.txt
```

And importantly:

**You should NOT see `.env` or `.venv`.**

---

### Your final assignment proof

You now have all three things the assignment asks for:

**1. Working project**

```text
Python → Neo4j AuraDB
```

**2. GitHub repository**

```text
Python files + requirements.txt + README + .gitignore
```

**3. YouTube demonstration**

Show:

```text
VS Code
  ↓
.venv activated
  ↓
python --version
  ↓
git --version
  ↓
pip --version
  ↓
python database.py
  ↓
Neo4j connection successful!
  ↓
python main.py
  ↓
Created node: Hello Neo4j
  ↓
Neo4j Aura
  ↓
MATCH (n:TestNode) RETURN n;
```


