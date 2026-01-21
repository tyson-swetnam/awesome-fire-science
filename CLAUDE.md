# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an "Awesome List" style repository for wildland fire science resources, published as a documentation website using Zensical (a modern static site generator by the Material for MkDocs team). The repository organizes curated links to data sources, software tools, computing resources, training materials, and professional networks related to wildland fire research and management.

## Project Structure

```
awesome-fire-science/
├── docs/               # Zensical documentation source files
│   ├── index.md        # Home page
│   ├── data.md         # Data sources and journals
│   ├── software.md     # Licensed and open-source software tools
│   ├── cyberinfrastructure.md  # Computing platforms and resources
│   ├── training.md     # Educational resources
│   ├── networks.md     # Professional networks and communities
│   ├── overrides/      # Theme customizations
│   └── stylesheets/    # Custom CSS
├── mkdocs.yml          # Main Zensical configuration (uses MkDocs-compatible format)
├── mkdocs.insiders.yaml # Extended config (inherits from mkdocs.yml)
└── requirements.txt    # Python dependencies
```

## Development Commands

### Build and Serve Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Serve documentation locally with live reload
mkdocs serve

# Build static site (outputs to site/ directory)
mkdocs build
```

### Deployment

Documentation is automatically deployed to GitHub Pages via `.github/workflows/publish-docs.yml` when changes are pushed to the `main` branch. The workflow:
1. Installs dependencies from `requirements.txt` (including Zensical)
2. Runs `mkdocs gh-deploy --force` to publish to gh-pages branch

Note: Zensical is compatible with existing MkDocs workflows and commands.

## Content Architecture

### Zensical Configuration

- **Main config**: `mkdocs.yml` - Defines site structure, theme, plugins, and markdown extensions (Zensical uses MkDocs-compatible configuration format)
- **Extended config**: `mkdocs.insiders.yaml` - Inherits from main config, adds social card generation and tag plugins
- **Theme**: Zensical with custom color palette (YouTube scheme for light mode, Slate for dark mode). Zensical is built by the Material for MkDocs team and supports both classic (Material-like) and modern theme variants.

### Markdown Extensions

The site uses extensive PyMdown Extensions for enhanced markdown:
- Admonitions (??? Tip, !!! Note, etc.)
- Emoji support via Material/FontAwesome icons (`:material-fire:`, `:octicons-database-24:`)
- Task lists, tables, code highlighting
- Mermaid diagrams support
- Jupyter notebook integration via `mkdocs-jupyter` plugin

### Content Organization

Each markdown file follows a consistent pattern:
- Uses Material Design icons in headings (e.g., `:octicons-gear-24: Software`)
- Organizes resources with collapsible admonition blocks (`??? Tip`)
- Links open in new tabs with `{target=_blank}`
- Emphasizes FAIR and CARE data principles
- Balances commercial/licensed tools with open-source alternatives

## Editing Content

### Adding New Resources

When adding entries to documentation files:
1. Maintain alphabetical or logical grouping within sections
2. Use Material icons for visual consistency (see existing files for icon patterns)
3. Include `{target=_blank}` for external links
4. Provide context with admonition blocks when introducing new categories
5. Include brief descriptions for why resources are valuable

### Icon Usage

Common icon patterns:
- `:material-fire:` - Fire-related content
- `:octicons-database-24:` - Data sources
- `:octicons-gear-24:` - Software/tools
- `:octicons-cloud-24:` - Cloud/computing
- `:material-book-education:` - Educational resources
- `:simple-<brand>:` - Brand logos (github, jupyter, python, etc.)

### Navigation Structure

The site navigation is defined in `mkdocs.yml` under the `nav:` key. To add new pages:
1. Create the markdown file in `docs/`
2. Add the entry to `nav:` in `mkdocs.yml`
3. Follow existing naming conventions (lowercase, hyphenated)

## Technical Notes

- The site uses Google Analytics (property: G-NYETZFD8DN)
- Git revision dates are automatically added to pages via `git-revision-date` plugin
- Jupyter notebooks can be included directly in documentation with `mkdocs-jupyter`
- Social media links and author info are configured in `mkdocs.yml` under `extra:`
- Custom CSS is in `docs/stylesheets/extra.css`
- Zensical is compatible with existing MkDocs Material configurations and maintains the same HTML structure
- Built with Rust and Python for improved performance

## Repository Context

- **Main branch**: `main` (use for PRs and deployment)
- **Published URL**: https://tysonswetnam.com/awesome-fire-science
- **GitHub Repo**: https://github.com/tyson-swetnam/awesome-fire-science
- **License**: See LICENSE file
- **Contributions**: Welcome via GitHub Issues

This is primarily a content curation project rather than a software development project. The focus is on maintaining high-quality, organized lists of wildland fire science resources.
