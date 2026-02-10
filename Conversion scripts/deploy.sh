#!/bin/bash
# script for deploying to server via rsync

set -euo pipefail

# Remote target
REMOTE_HOST="login@server"
REMOTE_PATH="/home/login/WWW"

# Rsync options:
#  -a archive (includes -rltpgoD)
#  -v verbose
#  -z compression
#  --delete remove files on remote no longer present locally (optional; remove if undesired)
#  --exclude exclude local-only artifacts
#  --chmod enforce permissions regardless of local umask: dirs 755, files 644
RSYNC_OPTS=(
	-avz
	--delete
	--exclude ".git/"
	--exclude ".venv/"
	--exclude "__pycache__/"
	--chmod=Du=rwx,Dgo=rx,Fu=rw,Fgo=r
)

echo "Deploying to ${REMOTE_HOST}:${REMOTE_PATH} ..."
rsync "${RSYNC_OPTS[@]}" . "${REMOTE_HOST}:${REMOTE_PATH}" 

# Fallback / hard guarantee of permissions (if remote fs or prior perms differ)
echo "Normalizing permissions on remote..."
ssh "${REMOTE_HOST}" "find ${REMOTE_PATH} -type d -exec chmod 755 {} +; find ${REMOTE_PATH} -type f -exec chmod 644 {} +"

echo "Deployment complete."

