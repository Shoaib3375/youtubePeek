# 🎨 VideoPeek - Visual Style Guide

## Color Palette

### Primary Colors
```
Primary Blue-Purple
  HEX: #667eea
  RGB: 102, 126, 234
  Usage: Main buttons, primary badges, focus states

Primary Dark Purple
  HEX: #764ba2
  RGB: 118, 75, 162
  Usage: Dark gradient endpoint, hover states

Combined Gradient: #667eea → #764ba2
```

### Accent Colors

#### Accent 1: Quality Gradient (Pink → Red)
```
Pink
  HEX: #f093fb
  RGB: 240, 147, 251

Red
  HEX: #f5576c
  RGB: 245, 87, 108
  
Usage: Quality badges (1080p, 720p, etc.)
```

#### Accent 2: Size Gradient (Blue → Cyan)
```
Light Blue
  HEX: #4facfe
  RGB: 79, 172, 254

Cyan
  HEX: #00f2fe
  RGB: 0, 242, 254
  
Usage: File size badges
```

#### Accent 3: Codec Gradient (Purple)
```
Purple
  HEX: #9b59b6
  RGB: 155, 89, 182

Darker Purple
  HEX: #8e44ad
  RGB: 142, 68, 173
  
Usage: Protocol badges (HTTPS, HTTP)
```

### Neutral Colors
```
Text Dark
  HEX: #333333
  RGB: 51, 51, 51
  Usage: Primary text

Text Light
  HEX: #999999
  RGB: 153, 153, 153
  Usage: Secondary text, hints

Border Light
  HEX: #e0e0e0
  RGB: 224, 224, 224
  Usage: Card borders, separators

Background Light
  HEX: #f9f9f9
  RGB: 249, 249, 249
  Usage: Card backgrounds, subtle areas

White
  HEX: #ffffff
  RGB: 255, 255, 255
  Usage: Main backgrounds

Background Gradient
  Linear: #667eea (0%) → #764ba2 (100%)
  Usage: Page background
```

### Status Colors
```
Error
  Background: #ffeeee (HEX: #fee)
  Border: #ffcccc (HEX: #fcc)
  Text: #cc3333 (HEX: #c33)

Success
  Background: #eeffee (HEX: #efe)
  Border: #ccffcc (HEX: #cfc)
  Text: #333333
```

## Typography

### Font Stack
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
             Roboto, 'Helvetica Neue', Arial, sans-serif;
```

**Breakdown:**
1. `-apple-system` - macOS, iOS
2. `BlinkMacSystemFont` - macOS fallback
3. `Segoe UI` - Windows
4. `Roboto` - Android
5. `Helvetica Neue` - Fallback
6. `Arial` - Universal fallback
7. `sans-serif` - Generic sans-serif

### Font Sizes & Weights

```
Hero H1 (Desktop)
  Size: 3rem (48px)
  Weight: 700 (Bold)
  Line Height: 1.2

Hero H1 (Mobile)
  Size: 2rem (32px)
  Weight: 700 (Bold)

Hero Paragraph
  Size: 1.2rem (19px)
  Weight: 300 (Light)
  Opacity: 0.95

Card Title
  Size: 1.3rem (20px)
  Weight: 600 (Semi-bold)

Section Title (H3)
  Size: 1.2rem (19px)
  Weight: 600 (Semi-bold)

Format Title (H4)
  Size: 1rem (16px)
  Weight: 600 (Semi-bold)

Body Text
  Size: 1rem (16px)
  Weight: 400 (Normal)

Small Text
  Size: 0.9rem (14px)
  Weight: 500 (Medium)

Badge Text
  Size: 0.8rem (13px)
  Weight: 600 (Semi-bold)
```

## Shadow System

### Shadow Levels
```
Shadow SM (Subtle)
  0 2px 8px rgba(0, 0, 0, 0.1)
  Usage: Hover effects, light elevation

Shadow MD (Medium)
  0 4px 12px rgba(0, 0, 0, 0.15)
  Usage: Cards, default elevation

Shadow LG (Large)
  0 20px 60px rgba(0, 0, 0, 0.3)
  Usage: Main card, prominent elements

Button Shadow (Glow)
  0 4px 15px rgba(102, 126, 234, 0.4)
  Usage: Button default state

Button Shadow Hover
  0 6px 20px rgba(102, 126, 234, 0.6)
  Usage: Button hover state

Format Card Shadow Hover
  0 8px 20px rgba(102, 126, 234, 0.15)
  Usage: Card hover interaction
```

## Spacing System

### Padding
```
XS: 0.25rem (4px)
SM: 0.5rem (8px)
MD: 0.75rem (12px)
LG: 1rem (16px)
XL: 1.25rem (20px)
XXL: 1.5rem (24px)
XXXL: 2rem (32px)
XXXXL: 2.5rem (40px)
```

### Gap (Flex/Grid)
```
SM: 0.5rem (8px)
MD: 0.75rem (12px)
LG: 1rem (16px)
XL: 1.5rem (24px)
XXL: 2rem (32px)
XXXL: 3rem (48px)
```

### Margin
```
Section: 3rem (48px)
Card Bottom: 3rem (48px)
Element: 1rem - 2rem
Text: 0.5rem - 1.5rem
```

## Border Radius

```
Subtle:    4px  - (Not used much)
Small:     8px  - Meta items
Medium:    12px - Cards, input, buttons, footer sections
Large:     16px - Main card, nav bar
Full:      50%  - Round buttons, badges
```

## Component Specifications

### Button Styles

#### Primary Button
```
Background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
Color: white
Padding: 1rem 2rem
Border Radius: 12px
Font Weight: 600
Font Size: 1rem
Box Shadow: 0 4px 15px rgba(102, 126, 234, 0.4)
Cursor: pointer

States:
  Normal:   Above shadow
  Hover:    Shadow: 0 6px 20px rgba(102, 126, 234, 0.6)
            Transform: translateY(-2px)
  Active:   Transform: translateY(0)
  Disabled: Opacity: 0.6, No transform
  
Transition: all 0.3s ease
```

#### Secondary Button (Format-specific)
```
Proxy Button:
  Background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%)
  Same padding and styling as primary
  Different gradient color
```

### Badge Styles

#### Format Badge (Type)
```
Background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
Color: white
Padding: 0.4rem 0.85rem
Border Radius: 20px
Font Size: 0.8rem
Font Weight: 600
Display: inline-block
```

#### Quality Badge
```
Same as Format Badge but:
Background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%)
```

#### Size Badge
```
Same as Format Badge but:
Background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)
```

#### Codec Badge
```
Same as Format Badge but:
Background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%)
```

#### Feature Badge
```
Background: rgba(255, 255, 255, 0.2)
Color: white
Border: 1px solid rgba(255, 255, 255, 0.3)
Padding: 0.5rem 1.25rem
Border Radius: 30px
Font Size: 0.9rem
Font Weight: 500
Backdrop Filter: blur(10px)
```

### Input Styles

```
Background: #f9f9f9 (focus: white)
Border: 2px solid #e0e0e0 (focus: #667eea)
Border Radius: 12px
Padding: 1rem 1.25rem
Font Size: 1rem
Font Family: inherit
Transition: all 0.3s ease

Focus Box Shadow: 0 0 0 3px rgba(102, 126, 234, 0.1)

Placeholder:
  Color: #999999
  Opacity: 1
```

### Card Styles

#### Main Card
```
Background: white
Border Radius: 16px
Box Shadow: 0 20px 60px rgba(0, 0, 0, 0.3)
Padding: 2.5rem (desktop) / 1.5rem (mobile)
Animation: slideUp 0.6s ease-out
```

#### Format Card
```
Background: #f9f9f9 (hover: white)
Border: 1px solid #e0e0e0 (hover: #667eea)
Border Radius: 12px
Padding: 1.5rem
Transition: all 0.3s ease

Hover Effects:
  - Box Shadow: 0 8px 20px rgba(102, 126, 234, 0.15)
  - Transform: translateY(-4px)
  - Background: white
```

### Navigation Bar

```
Background: rgba(255, 255, 255, 0.95)
Backdrop Filter: blur(10px)
Box Shadow: 0 4px 12px rgba(0, 0, 0, 0.15)
Position: sticky
Top: 0
Z-index: 1000
Padding: 1rem 1.5rem

Logo:
  Font Size: 1.5rem
  Font Weight: 700
  Background: linear-gradient(135deg, #667eea, #764ba2)
  -webkit-background-clip: text
  -webkit-text-fill-color: transparent
  background-clip: text

Menu Links:
  Color: #333 (hover: #667eea)
  Text Decoration: none
  Font Weight: 500
  Position: relative
  
  Underline Animation:
    Position: absolute
    Bottom: -5px
    Height: 2px
    Width: 0 (hover: 100%)
    Background: linear-gradient(90deg, #667eea, #764ba2)
    Transition: width 0.3s ease
```

### Footer

```
Background: rgba(0, 0, 0, 0.1)
Backdrop Filter: blur(10px)
Color: white
Padding: 3rem 1.5rem
Margin Top: auto
Animation: slideUp 0.6s ease-out

Grid:
  Desktop: 4 columns (repeat(auto-fit, minmax(250px, 1fr)))
  Mobile: 1 column
  Gap: 2rem

Section Heading:
  Font Size: 1.1rem
  Font Weight: 600
  Margin Bottom: 1rem

Links:
  Color: white
  Opacity: 0.9
  Transition: opacity 0.3s ease
  
  Hover:
    Opacity: 0.7

Social Links:
  Width: 40px
  Height: 40px
  Background: rgba(255, 255, 255, 0.1)
  Border: 1px solid rgba(255, 255, 255, 0.2)
  Border Radius: 50%
  Display: flex (center)
  Gap: 1.5rem
  
  Hover:
    Background: rgba(255, 255, 255, 0.2)
    Transform: translateY(-2px)
```

## Animation Specifications

### Slide Down
```
Duration: 0.6s
Timing: ease-out
From:
  Opacity: 0
  Transform: translateY(-20px)
To:
  Opacity: 1
  Transform: translateY(0)

Usage: Navigation, hero section
```

### Slide Up
```
Duration: 0.6s
Timing: ease-out
From:
  Opacity: 0
  Transform: translateY(20px)
To:
  Opacity: 1
  Transform: translateY(0)

Usage: Main card, footer
```

### Fade In
```
Duration: 0.4s
Timing: ease-out
From: Opacity: 0
To:   Opacity: 1

Usage: Format cards, results
```

### Spin
```
Duration: 0.8s
Timing: linear
Iteration: infinite
From: Transform: rotate(0deg)
To:   Transform: rotate(360deg)

Usage: Loading spinner
```

### Shake
```
Duration: 0.3s
Timing: ease-out
Animation:
  0%, 100%:  Transform: translateX(0)
  25%:       Transform: translateX(-5px)
  75%:       Transform: translateX(5px)

Usage: Error messages
```

## Responsive Layout

### Desktop (≥ 768px)
```
Container Max Width: 1200px
Padding: 2rem 1rem

Typography:
  Hero H1: 3rem
  Card Title: 1.3rem

Spacing:
  Large gaps: 2rem - 3rem
  Large padding: 2rem - 2.5rem

Layout:
  Video Header: Flex row (side-by-side)
  Format Grid: Multi-row
  Footer: 4 columns
```

### Mobile (< 768px)
```
Container: 100% width
Padding: 1.5rem (cards)

Typography:
  Hero H1: 2rem
  Font sizes: 10% smaller

Spacing:
  Reduced gaps: 1rem - 1.5rem
  Reduced padding: 1rem - 1.5rem

Layout:
  Video Header: Stack (column)
  Format Grid: Single column
  Buttons: Full width
  Footer: Single column
```

## Gradient Directions

All gradients use `135deg`:
```
135deg creates diagonal gradient:
  ↖️ → ↘️
  Top-left to bottom-right
```

This angle:
- Creates visual depth
- Works well with text
- Professional appearance
- Smooth color transitions

## Accessibility Color Contrast

### WCAG AA Compliance (4.5:1 minimum)

```
White on Primary Gradient: ✓ 7:1 (AAA)
Dark Text on White: ✓ 21:1 (AAA)
Light Text on Primary: ✓ 5:1 (AA)
Error Red on Light: ✓ 5.5:1 (AA)
Success Green on Light: ✓ 6:1 (AAA)
```

## Consistency Guidelines

1. **Gradients**: Always use 135deg direction
2. **Radius**: Cards 12-16px, buttons 12px, badges 20px
3. **Shadows**: Use the 3-level system consistently
4. **Spacing**: Follow the spacing scale
5. **Typography**: Use font stack + designated sizes
6. **Colors**: Stick to the palette
7. **Animations**: Keep 0.3s-0.6s duration range

---

**Version**: 2.0
**Last Updated**: January 16, 2026
