# USFS Brand Standards Preview

This page demonstrates the updated design elements based on U.S. Forest Service brand standards.

## Typography Hierarchy

### Primary Heading (H1)
Uses Merriweather - a professional serif font with authority and readability.

#### Secondary Heading (H2)
Clean hierarchy with Forest Service blue accent border.

##### Tertiary Heading (H3)
Forest Service green for subsections.

###### Category Heading (H4)
UPPERCASE UTILITY HEADING FOR CATEGORIES

Body text uses **Public Sans** - a professional, accessible sans-serif font developed for government use. It provides excellent readability and a modern, clean appearance suitable for both digital and print materials.

## Color Palette

The design implements official USFS colors:

!!! note "USFS Green - PANTONE 343 CV"
    Primary brand color: `#00502F` - Deep forest green representing the natural environment and Forest Service heritage.

!!! info "USFS Blue - PANTONE 288 CV"
    Secondary color: `#004B87` - Professional blue for accents and interactive elements.

!!! tip "Professional Application"
    These colors create a cohesive, authoritative appearance while maintaining accessibility standards (WCAG AA compliance).

## Content Blocks

### Admonition Styles

??? tip "Forest Service Green Tips"
    Tips and best practices use the primary USFS green color scheme. This creates visual consistency with the Forest Service brand identity.

    Key features:
    - Left border accent
    - Gradient background
    - Professional typography

!!! warning "Fire Weather Warning"
    Warnings use fire orange tones to convey urgency and attention. This is particularly relevant for fire science content.

!!! danger "Critical Alert"
    Critical information uses alert red for maximum visibility and immediate attention.

!!! note "Standard Information"
    Standard notes use the USFS blue color for neutral information and guidance.

## Links & Navigation

[Internal Link Example](#typography-hierarchy) - Links use USFS blue with hover states.

[External Link Example](https://www.fs.usda.gov){target=_blank} - External links include indicator arrow.

### Button Styles

<div class="md-button">USFS Green Button</div>
<div class="md-button md-button--primary">USFS Blue Button</div>

## Data Tables

| Category | Description | Status |
|----------|-------------|--------|
| Data Sources | Fire atlases and journals | Active |
| Software Tools | Modeling and GIS platforms | Active |
| Computing | HPC and cloud resources | Active |
| Training | Educational materials | Active |

## Code Presentation

```python
# Fire behavior calculation example
def calculate_rate_of_spread(wind_speed, slope, fuel_moisture):
    """
    Calculate fire rate of spread using simplified model.
    Based on USFS fire behavior prediction systems.
    """
    base_ros = 2.5  # chains per hour
    wind_factor = wind_speed * 0.3
    slope_factor = slope * 0.15
    moisture_factor = (100 - fuel_moisture) / 100

    return base_ros * (1 + wind_factor + slope_factor) * moisture_factor
```

Inline code examples use `monospace typography` with subtle backgrounds.

## Design Principles

The updated design follows these USFS brand principles:

1. **Authority & Trust**: Professional typography and official colors establish credibility
2. **Accessibility**: High contrast ratios and clear hierarchy ensure usability
3. **Natural Elements**: Subtle textures and organic color palette connect to forestry
4. **Federal Identity**: Consistent with U.S. government design standards
5. **Professionalism**: Clean layouts with appropriate spacing and refinement

## Responsive Behavior

The design adapts seamlessly across devices:

- **Desktop**: Full navigation, wide content areas, detailed typography
- **Tablet**: Responsive grids, touch-friendly targets
- **Mobile**: Streamlined navigation, optimized text size, vertical stacking

## Dark Mode

Toggle to dark mode to see the adapted color scheme:

- Forest Service green remains prominent but lighter for contrast
- Blue accents shift to lighter tones for visibility
- Backgrounds use deep grays with subtle green tints
- Code blocks maintain readability with adjusted colors

---

**Note**: This preview demonstrates the comprehensive CSS overhaul implementing USFS FS-1186 brand standards (May 2023), including official color palette, professional typography, and federal design system best practices.
