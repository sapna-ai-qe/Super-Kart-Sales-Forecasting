"""Helper to check required environment variables and prompt securely if missing.

Run locally to verify configuration before deployment.
"""
import os
import getpass

REQUIRED = [
    ("HF_HUB_TOKEN", "Hugging Face token (HF_HUB_TOKEN or HF_TOKEN)"),
    ("HF_REPO_ID", "Hugging Face repo id (username/space-name)"),
    ("BACKEND_API_URL", "Backend API URL for Streamlit frontend")
]

def mask_token(tok: str) -> str:
    if not tok:
        return "(not set)"
    return tok[:6] + "..." + tok[-4:]

def main():
    env = {}
    env['HF_HUB_TOKEN'] = os.environ.get('HF_HUB_TOKEN') or os.environ.get('HF_TOKEN')
    if not env['HF_HUB_TOKEN']:
        env['HF_HUB_TOKEN'] = getpass.getpass('Enter Hugging Face token (input hidden, or set HF_HUB_TOKEN): ')

    env['HF_REPO_ID'] = os.environ.get('HF_REPO_ID') or ''
    if not env['HF_REPO_ID']:
        val = input('Enter HF_REPO_ID (username/space-name) or leave blank to skip upload: ').strip()
        env['HF_REPO_ID'] = val

    env['BACKEND_API_URL'] = os.environ.get('BACKEND_API_URL') or ''
    if not env['BACKEND_API_URL']:
        val = input('Enter BACKEND_API_URL for frontend (or leave blank): ').strip()
        env['BACKEND_API_URL'] = val

    print('\nConfiguration summary:')
    print(f"HF_HUB_TOKEN: {mask_token(env['HF_HUB_TOKEN'])}")
    print(f"HF_REPO_ID: {env['HF_REPO_ID'] or '(not set)'}")
    print(f"BACKEND_API_URL: {env['BACKEND_API_URL'] or '(not set)'}")

if __name__ == '__main__':
    main()
