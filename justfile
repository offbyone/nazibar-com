set dotenv-load

default: pelican

setup:
  mise install
  terraform init

pelican:
    pelican

serve:
    pelican --listen --autoreload

upload:
  aws s3 sync \
    --delete \
    output \
    s3://nazibar.com

invalidate:
  aws cloudfront create-invalidation \
    --distribution-id E3HG7SIR4ZZAS1 \
    --paths "/*"

node_modules:
  npm install

prepare_fonts: node_modules
  mkdir -p themes/nazibar/static/webfonts

  rsync -pthrvz \
    node_modules/@fortawesome/fontawesome-free/webfonts/ \
    themes/nazibar/static/webfonts/

build settings="pelicanconf.py": prepare_fonts
  pelican --fatal=errors -s {{settings}} -o output content

generate: (build "publishconf.py")

generate-dev: build

publish: generate upload invalidate

compile-deps:
  pdm lock

update-deps:
  pdm update --update-all

install-deps:
  pdm install

deps: compile-deps install-deps

plan:
    terraform plan -out plan.just

apply:
    terraform apply plan.just
