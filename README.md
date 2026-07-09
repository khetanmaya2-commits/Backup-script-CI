# 🚀 Automated Backup System with GitHub Actions CI

A Python automation project that creates compressed `.tar.gz` backups of a directory and validates the backup process automatically using GitHub Actions CI.

## ✨ Features

- 📂 Automated directory backup
- 🗜️ Creates compressed `.tar.gz` archives
- ⚙️ GitHub Actions CI pipeline
- 📦 Uploads backup as a GitHub Actions Artifact
- 🐍 Built using Python

## 🛠️ Tech Stack

- Python
- Git & GitHub
- GitHub Actions
- YAML

## 📂 Project Structure

```text
backup-project/
│
├── backups.py
├── sample_data/
├── backup/
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

## 🏗️ Architecture

```text
        Developer
            │
            ▼
      Push Code to GitHub
            │
            ▼
     GitHub Actions CI
            │
    ┌───────┼────────┐
    ▼       ▼        ▼
 Checkout  Setup   Run Backup
   Code    Python    Script
                     │
                     ▼
           Create .tar.gz Backup
                     │
                     ▼
          Upload Backup Artifact
                     │
                     ▼
              Pipeline Success ✅
```

## ▶️ Running Locally

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd backup-project
```

Run the backup script

```bash
python backups.py
```

The backup archive will be created inside the **backup/** directory.

---

## 🚀 Future Enhancements

- Upload backups to AWS S3
- Delete old backups automatically
- Add logging
- Schedule daily backups using GitHub Actions
