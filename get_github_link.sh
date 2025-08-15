#!/bin/bash
# get_github_link.sh
# Usage: ./get_github_link.sh <filepath>

USERNAME="StevenDesigner"
REPO="Python_Training_Files"
BRANCH="main"

if [ -z "$1" ]; then
  echo "Usage: $0 <filepath>"
  exit 1
fi

FILEPATH=$(realpath --relative-to=. "$1" | sed 's/\\/\//g')
echo "https://github.com/$USERNAME/$REPO/blob/$BRANCH/$FILEPATH"