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