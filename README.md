# Auto-generated Portfolio

This repository automatically generates a portfolio page from my public GitHub repositories using GitHub Actions and Python.

## How it works

- The workflow runs every Monday (or on manual trigger).
- It uses a Python script to fetch your public repositories.
- It generates a `portfolio.md` with your projects.
- Commit and push changes automatically.

## How to use

1. Fork or clone this repository.
2. Change `"pboric"` to your GitHub username in `.github/workflows/generate-portfolio.yml` if needed.
3. Push to your own GitHub repository.
4. Enable GitHub Pages if you want to publish your portfolio.
