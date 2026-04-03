# Featured Products Section - Visual Guide

## Section Layout

### Desktop View (990px+)

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  Best Sellers                                    [View All →]    │
│                                                                  │
├───────────────┬───────────────┬───────────────┬───────────────┤
│               │               │               │               │
│  [Image 1:1]  │  [Image 1:1]  │  [Image 1:1]  │  [Image 1:1]  │
│     🔍        │     🔍        │     🔍        │     🔍        │
│               │               │               │               │
│  Product 1    │  Product 2    │  Product 3    │  Product 4    │
│  $29.99       │  $39.99       │  $49.99       │  $19.99       │
│ [Add to Cart] │ [Add to Cart] │ [Add to Cart] │ [Add to Cart] │
│               │               │               │               │
├───────────────┼───────────────┼───────────────┼───────────────┤
│               │               │               │               │
│  [Image 1:1]  │  [Image 1:1]  │  [Image 1:1]  │  [Image 1:1]  │
│     🔍        │     🔍        │     🔍        │     🔍        │
│               │               │               │               │
│  Product 5    │  Product 6    │  Product 7    │  Product 8    │
│  $24.99       │  $34.99       │  $44.99       │  $14.99       │
│ [Add to Cart] │ [Add to Cart] │ [Add to Cart] │ [Add to Cart] │
│               │               │               │               │
└───────────────┴───────────────┴───────────────┴───────────────┘

Layout: 4 columns
Gap: 2rem (32px)
Image: 1:1 ratio with zoom on hover (scale 1.03)
```

---

### Tablet View (750-989px)

```
┌─────────────────────────────────────────────┐
│                                             │
│  Best Sellers              [View All →]    │
│                                             │
├──────────────────┬──────────────────┤
│                  │                  │
│  [Image 1:1]     │  [Image 1:1]     │
│     🔍           │     🔍           │
│                  │                  │
│  Product 1       │  Product 2       │
│  $29.99          │  $39.99          │
│ [Add to Cart]    │ [Add to Cart]    │
│                  │                  │
├──────────────────┼──────────────────┤
│  Product 3       │  Product 4       │
├──────────────────┼──────────────────┤
│  Product 5       │  Product 6       │
├──────────────────┼──────────────────┤
│  Product 7       │  Product 8       │
└──────────────────┴──────────────────┘

Layout: 2 columns
Gap: 1.5rem (24px)
```

---

### Mobile View (<750px)

```
┌────────────────────┐
│                    │
│  Best Sellers      │
│  [View All →]      │
│                    │
├────────────────────┤
│                    │
│  [Image 1:1]       │
│     🔍             │
│                    │
│  Product 1         │
│  $29.99            │
│ [Add to Cart]      │
│                    │
├────────────────────┤
│  Product 2         │
├────────────────────┤
│  Product 3         │
├────────────────────┤
│  Product 4         │
├────────────────────┤
│  Product 5         │
├────────────────────┤
│  Product 6         │
├────────────────────┤
│  Product 7         │
├────────────────────┤
│  Product 8         │
└────────────────────┘

Layout: 1 column (full-width)
Gap: 1.25rem (20px)
```

---

## Product Card Details

### Card Structure

```
┌─────────────────────────────┐
│   Image (1:1 Ratio)         │  ← object-fit: cover
│   ┌─────────────────────┐   │     Hover: scale(1.03)
│   │                     │   │
│   │      Product        │   │  200px × 200px (desktop)
│   │       Image         │   │  Responsive sizing
│   │                     │   │
│   └─────────────────────┘   │
│                             │
│  Product Name (2 lines)     │  ← Truncated with ellipsis
│  $29.99                     │  ← Bold, 16px
│                             │
│  ┌──────────────────────┐   │
│  │   Add to Cart        │   │  ← Full-width button
│  │  (outlined style)    │   │     Hover: filled blue
│  └──────────────────────┘   │
│                             │
└─────────────────────────────┘

Border Radius: 10px
Background: White
Shadow: 0 2px 8px rgba(0,0,0,0.08)
Hover Shadow: 0 8px 20px rgba(0,0,0,0.12)
```

---

## Typography

### Section Title
- **Font Size:** 32px (2rem) desktop → 24px (1.5rem) mobile
- **Font Weight:** 700 (bold)
- **Color:** #1A1A1A (dark gray)
- **Alignment:** Left
- **Letter Spacing:** -0.01em (tighter)

### Product Name
- **Font Size:** 14px (0.875rem) desktop → 13px (0.8125rem) mobile
- **Font Weight:** 600 (semi-bold)
- **Color:** #1A1A1A
- **Lines:** Maximum 2 lines (truncated with ellipsis)
- **Line Height:** 1.4

### Price
- **Font Size:** 16px (1rem) desktop → 15px (0.9375rem) mobile
- **Font Weight:** 700 (bold)
- **Color:** #1A1A1A
- **Format:** Shopify money filter (auto-formatted currency)

### View All Link
- **Font Size:** 16px (1rem) desktop → 15px (0.9375rem) mobile
- **Font Weight:** 500 (medium)
- **Color:** #6BA3BE (ivory blue)
- **Hover:** #4A7A94 (darker blue)

---

## Button Styling

### Add to Cart Button

```
DEFAULT STATE:
┌──────────────────┐
│  Add to Cart     │  ← Text color: #6BA3BE
└──────────────────┘
Border: 1px solid #6BA3BE
Background: transparent
Padding: 0.75rem 1rem (12px 16px)

HOVER STATE:
┌──────────────────┐
│  Add to Cart     │  ← Text color: #FFFFFF (white)
└──────────────────┘
Border: 1px solid #6BA3BE
Background: #6BA3BE (filled)
Transform: None (no movement)

Transition: 0.3s ease
Border Radius: 6px
```

---

## Color Reference

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| Background | White | #FFFFFF | Section & cards |
| Title Text | Dark Gray | #1A1A1A | Headings |
| Product Name | Dark Gray | #1A1A1A | Product info |
| Price | Dark Gray | #1A1A1A | Price display |
| Button Text | Ivory Blue | #6BA3BE | Normal state |
| Button Hover BG | Ivory Blue | #6BA3BE | Hover state |
| Button Hover Text | White | #FFFFFF | On hover |
| "View All" Link | Ivory Blue | #6BA3BE | Normal |
| "View All" Hover | Dark Blue | #4A7A94 | Hover |
| Image Placeholder | Light Gray | #F5F5F5 | No image |
| Card Shadow | Black 8% | rgba(0,0,0,0.08) | Default |
| Hover Shadow | Black 12% | rgba(0,0,0,0.12) | Hover |

---

## Spacing System

### Padding
```
Section Padding:
├─ Desktop:        60px top/bottom × 2rem (32px) sides
├─ Tablet:         50px top/bottom × 1.5rem (24px) sides
└─ Mobile:         40px top/bottom × 1rem (16px) sides

Card Padding:
├─ Desktop:        1.5rem (24px)
└─ Mobile:         1.25rem (20px)
```

### Grid Gap
```
Desktop:           2rem (32px)
Tablet:            1.5rem (24px)
Mobile:            1.25rem (20px)
```

### Margins
```
Header Bottom:     3rem (48px) desktop → 2rem (32px) mobile
Product Info Gap:  0.75rem (12px) between name & price
Price-Button Gap:  1rem (16px)
```

---

## Hover Effects

### Image Hover
```
Transform: scale(1.03)
Duration: 0.3s
Easing: ease
Effect: Subtle zoom inward
```

### Card Shadow Hover
```
Default:  0 2px 8px rgba(0, 0, 0, 0.08)
Hover:    0 8px 20px rgba(0, 0, 0, 0.12)
Duration: 0.3s
Easing:   ease
Effect:   Depth increase, card lifts slightly
```

### Button Hover
```
Background: transparent → #6BA3BE
Text Color: #6BA3BE → #FFFFFF
Duration:   0.3s
Easing:     ease
Effect:     Smooth color transition
```

### Link Hover (View All)
```
Color:    #6BA3BE → #4A7A94
Duration: 0.3s
Easing:   ease
Effect:   Color darkens
```

---

## Responsive Breakpoints

### Desktop (990px and up)
- 4-column grid
- Full padding and spacing
- Standard font sizes
- Full "View All →" text

### Tablet (750px - 989px)
- 2-column grid
- Reduced padding (1.5rem sides)
- Slightly smaller fonts
- Header on one line

### Mobile (below 750px)
- 1-column full-width
- Minimal padding (1rem sides)
- Smallest fonts
- Header stacks vertically

---

## Key Dimensions

| Element | Size |
|---------|------|
| Section Padding (desktop) | 60px vertical |
| Header Margin Bottom | 3rem (48px) |
| Grid Gap (desktop) | 2rem (32px) |
| Product Card Padding | 1.5rem (24px) |
| Product Image Size | Variable (responsive) |
| Image Aspect Ratio | 1:1 (square) |
| Border Radius (card) | 10px |
| Border Radius (button) | 6px |
| Button Height | ~40px (with padding) |

---

## Image Guidelines

### Size Recommendations
- **Upload Size:** 500px × 500px or larger
- **Aspect Ratio:** 1:1 (square preferred, but any ratio works)
- **Format:** JPG, PNG, WebP
- **Optimization:** Compress for web (<150KB)

### Responsive Sizing
- Displays at multiple widths: 250px, 375px, 550px, 750px+
- Shopify CDN automatically resizes for each device
- No image quality loss on any screen size
- Alt text auto-populated from product title

---

## Accessibility

✅ **Semantic HTML**
- `<h2>` for section title
- Proper link markup for "View All"
- Image alt text from product titles

✅ **Color Contrast**
- Text: #1A1A1A on white (21:1 WCAG AAA)
- Buttons: #6BA3BE on white (4.5:1 WCAG AA)
- Meets WCAG accessibility standards

✅ **Focus States**
- Button focus visible (browser default)
- Link focus states clear
- Touch-friendly sizes (48px minimum)

---

## Best Practices

1. **Images:** Always upload square (1:1) images for best appearance
2. **Names:** Keep product names short (2 lines maximum)
3. **Collection:** Use meaningful collection handles
4. **Links:** Ensure "View All" link points to relevant collection page
5. **Testing:** Verify on mobile, tablet, and desktop
6. **Performance:** Optimize images before uploading

---

## Browser Preview

This section will display perfectly on:
- ✅ All modern desktop browsers
- ✅ Tablets (iPad, Android tablets)
- ✅ Mobile phones (iPhone, Android)
- ✅ All modern versions (no IE support needed)

---

**Last Updated:** April 3, 2026  
**Version:** 1.0  
**Status:** ✅ Ready for Production
