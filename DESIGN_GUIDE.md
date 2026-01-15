# 🎬 VideoPeek - UI/UX Design Guide

## Overview

This document outlines the modern, smooth UI/UX design of the VideoPeek application.

## Color Scheme

```
Primary Colors:
  --primary: #667eea (Blue-Purple)
  --primary-dark: #764ba2 (Dark Purple)

Accent Colors:
  --accent-pink: #f093fb (Pink)
  --accent-red: #f5576c (Red)
  --accent-cyan: #00f2fe (Cyan)
  --accent-blue: #4facfe (Light Blue)

Neutral Colors:
  --text-dark: #333
  --text-light: #999
  --border-light: #e0e0e0
  --bg-light: #f9f9f9
```

## Layout Components

### 1. Navigation Bar
- **Style**: Sticky, frosted glass effect with backdrop blur
- **Features**:
  - Gradient logo with brand name
  - Navigation menu with smooth underline hover effect
  - Responsive design collapses on mobile
- **Animation**: Slides down on page load

### 2. Hero Section
- **Design**: Center-aligned with gradient background
- **Elements**:
  - Large heading with text shadow
  - Subheading with description
  - Feature badges with glassmorphism effect
  - All elements animate in with staggered timing

### 3. Main Card (Input Section)
- **Style**: White card with large shadow
- **Features**:
  - Full-width search input with focus states
  - Extract button with gradient background
  - Status indicator with spinner animation
  - Result container below

### 4. Video Information Display
- **Thumbnail**: Rounded with shadow, left-aligned on desktop
- **Metadata**: Organized in styled boxes with icons
  - Uploader name
  - Video duration with formatting
  - Format count

### 5. Format Cards
- **Grid Layout**: Responsive grid that stacks on mobile
- **Card Elements**:
  - Format badges (type, quality, size, codec)
  - Two download buttons (Direct Link, Via Server)
  - Hover effects with lift animation

### 6. Footer
- **Style**: Semi-transparent with backdrop blur
- **Sections**:
  - About section
  - Features links
  - Support links
  - Legal links
  - Social media icons
  - Copyright information

## Animations & Transitions

```css
slideDown:  0.6s - Elements fade and slide down from top
slideUp:    0.6s - Elements fade and slide up from bottom
fadeIn:     0.4s - Elements fade in
spin:       0.8s - Infinite spinner rotation
shake:      0.3s - Error message shake effect
```

## Responsive Breakpoints

### Mobile (< 768px)
- Single column layout
- Full-width buttons
- Stacked flex containers
- Reduced font sizes
- Collapsed footer grid

### Tablet & Desktop (≥ 768px)
- Multi-column layouts
- Flexible button sizing
- Side-by-side arrangements
- Full typography hierarchy

## Interactive Features

### Input Field
- Smooth border color transition on focus
- Background color change (light -> white)
- Shadow highlight on focus

### Buttons
- Gradient background with shadow
- Lift animation on hover (translateY -2px)
- Press animation on click
- Disabled state with reduced opacity

### Format Cards
- Subtle hover lift effect
- Border color change on hover
- Shadow enhancement on hover
- Background transition to white

### Navigation Links
- Underline animation from left to right
- Smooth color transition
- Active state support

## Typography

```
Font Family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif

Sizes:
  Hero Title: 3rem (desktop), 2rem (mobile)
  Card Title: 1.3rem
  Section Title: 1.2rem
  Body: 1rem
  Small: 0.9rem
```

## Spacing System

- Small gap: 0.5rem
- Medium gap: 1rem
- Large gap: 1.5rem
- XL gap: 2rem
- Section gap: 3rem

- Small padding: 0.75rem
- Medium padding: 1rem
- Large padding: 1.25rem
- XL padding: 1.5rem
- Section padding: 2rem - 2.5rem

## Shadow System

```
--shadow-sm:  0 2px 8px rgba(0, 0, 0, 0.1)
--shadow-md:  0 4px 12px rgba(0, 0, 0, 0.15)
--shadow-lg:  0 20px 60px rgba(0, 0, 0, 0.3)
```

## Interaction States

### Hover States
- Navigation links: Color change + underline
- Buttons: Lift effect + shadow enhancement
- Cards: Border highlight + shadow + lift
- Links: Opacity change

### Focus States
- Input field: Border color + glow shadow
- Buttons: Full visual feedback
- Links: Outline for accessibility

### Disabled States
- Reduced opacity (0.6)
- No cursor pointer
- No transform effects

### Loading States
- Spinner animation
- Status text update
- Button disabled state

## Accessibility Features

1. **Color Contrast**: WCAG AA compliant
2. **Focus Indicators**: Clear visual feedback
3. **Semantic HTML**: Proper heading hierarchy
4. **Alt Text**: Provided for images
5. **Keyboard Navigation**: Supported via Enter key
6. **Screen Reader**: Semantic elements used
7. **Motion**: Respects prefers-reduced-motion (can be added)

## Format Display Features

### Format Grouping
- Video formats (🎥)
- Audio formats (🎵)
- Other formats (📦)

### Format Badges
- **Type Badge**: Format extension
- **Quality Badge**: Resolution or bitrate
- **Size Badge**: File size
- **Codec Badge**: Protocol used

### Download Options
- **Direct Link**: Redirects to source
- **Via Server**: Proxy download option

## Error Handling

### Error Display
- Red background (#fee)
- Red border (#fcc)
- Red text (#c33)
- Shake animation
- Clear error icon and message

## Success Indicators

### Success Display
- Green background (#efe)
- Green border (#cfc)
- Professional message
- Smooth slide-up animation

## Performance Considerations

1. **CSS Grid/Flexbox**: Efficient layouts
2. **Transform Animations**: GPU-accelerated
3. **Backdrop Blur**: Modern browser support
4. **No Heavy Shadows on Mobile**: Reduced blur
5. **Lazy Loading**: Images load on demand

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile: iOS Safari, Chrome Mobile

## Future Enhancements

- [ ] Dark mode support
- [ ] Theme customization
- [ ] Accessibility preferences toggle
- [ ] Advanced format filters
- [ ] Batch download support
- [ ] Download history
- [ ] Custom quality settings
- [ ] Playlist support
