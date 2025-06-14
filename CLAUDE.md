# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static website for nazibar.com built using Pelican, a Python-based static site generator. The site is deployed to AWS S3 and served via CloudFront.

## Architecture

- **Static Site Generator**: Uses Pelican with Jinja2 templates for content
- **Infrastructure**: AWS resources managed via Terraform
  - S3 buckets for hosting content and logs
  - CloudFront distribution for CDN
  - Route53 for DNS
  - ACM for SSL certificates
  - IAM roles for deployment
- **Dependencies**:
  - Python dependencies managed with uv
  - JavaScript dependencies managed with npm (mainly FontAwesome)
- **Task Runner**: Uses Just for common tasks

## Code 

Use modern Python libraries
Don't use regexes when parsers will work
Prefer modern html and CSS constructs, assuming modern browsers

## Common Commands

### Setup

```bash
# Install all dependencies and initialize Terraform
just setup

# Install Python dependencies
just install-deps

# Install npm dependencies
just node_modules
```

### Development

```bash
# Build the site in development mode
just build

# Serve the site locally with auto-reload
just serve

# Prepare fonts for the theme
just prepare_fonts
```

If port 8000 is in use, assume it's this, and do your checking just using cURL

### Infrastructure Management

```bash
# Plan Terraform changes
just plan

# Apply Terraform changes
just apply
```

### Deployment

```bash
# Generate production-ready site, upload to S3, and invalidate CloudFront cache
just publish

# Individual steps:
# Generate production site
just generate

# Upload to S3
just upload

# Invalidate CloudFront cache
just invalidate
```

### Dependency Management

```bash
# Lock Python dependencies
just compile-deps

# Update all dependencies
just update-deps

# Shorthand for compile and install
just deps
```

## Content Structure

Content is written in Markdown with Jinja2 templates in the `content/` directory. The main index page uses a Jinja2 template to dynamically generate a table of vendors.

