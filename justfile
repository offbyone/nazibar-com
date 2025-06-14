set dotenv-load

default: pelican

setup:
  mise install
  terraform init

pelican:
  uv run pelican

serve:
  uv run pelican --listen --autoreload

upload:
  uv run aws s3 sync \
    --delete \
    output \
    s3://nazibar.com

invalidate:
  uv run aws cloudfront create-invalidation \
    --distribution-id E3HG7SIR4ZZAS1 \
    --paths "/*"

node_modules:
  npm install

prepare_assets: node_modules
  # Create required directories
  mkdir -p themes/nazibar/static/webfonts
  mkdir -p themes/nazibar/static/js
  
  # Copy FontAwesome webfonts
  rsync -pthrvz \
    node_modules/@fortawesome/fontawesome-free/webfonts/ \
    themes/nazibar/static/webfonts/
  
  # Copy sorttable.js - temporary solution until webassets is fully configured
  cp node_modules/sorttable/sorttable.js themes/nazibar/static/js/

build settings="pelicanconf.py": prepare_assets
  uv run pelican --fatal=errors -s {{settings}} -o output content

generate: (build "publishconf.py")

generate-dev: build

pr-preview pr_number:
  #!/usr/bin/env bash
  set -euo pipefail
  
  # Create a PR-specific publishconf
  cat > pr_publishconf.py << EOF
# Import all settings from the main publishconf
import os
import sys
sys.path.append(os.curdir)
from publishconf import *

# Override SITEURL for GitHub Pages PR preview
SITEURL = "https://offbyone.github.io/nazibar-com/pr-{{pr_number}}"
EOF
  
  # Build the site with PR-specific publishconf
  uv run pelican --fatal=errors -s pr_publishconf.py -o output content
  
  # Clean up the temporary file
  rm pr_publishconf.py
  
  echo "PR preview built successfully for PR #{{pr_number}} at https://offbyone.github.io/nazibar-com/pr-{{pr_number}}"

publish: generate upload invalidate

compile-deps:
  uv sync

update-deps:
  uv sync --refresh

install-deps:
  uv sync

deps: compile-deps install-deps

plan:
  terraform plan -out plan.just

apply:
  terraform apply plan.just