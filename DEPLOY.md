# Deployment & Configuration Guide

This file describes required environment variables, common deployment steps, and how to securely provide secrets.

## Required environment variables

- `HF_HUB_TOKEN` or `HF_TOKEN` — Hugging Face access token (secret).
- `HF_REPO_ID` — Hugging Face Space repo id (format: `username/space-name`) used for uploads.
- `BACKEND_API_URL` — Backend API URL that the Streamlit frontend posts to (e.g. `https://<user>-<space>.hf.space`).

Keep secrets out of source control. Use platform secrets (Hugging Face Space secrets / CI secrets) or local environment variables.

## Quick local setup (PowerShell)

```powershell
$env:HF_HUB_TOKEN="hf_..."
$env:HF_REPO_ID="your-username/your-space-name"
$env:BACKEND_API_URL="https://your-backend.hf.space"
pip install -r requirements.txt
streamlit run frontend_files/app.py
```

## Deploying backend and frontend to Hugging Face Spaces

1. Ensure `HF_HUB_TOKEN` and `HF_REPO_ID` are set (or you will be prompted).
2. The repository creation step in the scripts calls `create_repo(...)` — change the repo name if desired.
3. The upload steps use `HfApi.upload_folder(folder_path, repo_id, repo_type="space")`.
4. On Hugging Face Spaces, add `BACKEND_API_URL` as a Space secret (Settings → Secrets) so the Streamlit app can reach the backend.

## Docker

- Build (from project root):
```bash
docker build -t superkart-app -f frontend_files/Dockerfile frontend_files
```
- Run:
```bash
docker run -e BACKEND_API_URL="$BACKEND_API_URL" -p 8501:8501 superkart-app
```

## Notes

- If tokens are missing, the scripts prompt for them using a secure prompt (`getpass`).
- Do not commit tokens or `.env` files with secrets.
