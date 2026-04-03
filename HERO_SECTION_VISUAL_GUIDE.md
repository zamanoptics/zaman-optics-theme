# Premium Hero Section - Visual Implementation Guide

## 🎨 Hero Section Layout Visualization

### Desktop Layout (990px+)
```
┌─────────────────────────────────────────────────────────────────────┐
│  ANNOUNCEMENT BAR (Orange #FF8C00)                                  │
│  Free Shipping on orders above Rs 3,000 | Cash on Delivery Available│
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                          HEADER + NAVIGATION                         │
├────────────────────────────────┬────────────────────────────────────┤
│                                │                                    │
│                                │                                    │
│  PREMIUM VISION CARE (label)   │                                    │
│  ═════════════════════════════ │      LIGHT BLUE BACKGROUND        │
│  Discover Your Perfect Frame   │      #E8F4F8                       │
│  (Large 52px heading)          │                                    │
│                                │      Featured Product              │
│  Experience premium eyewear    │      Image or Placeholder          │
│  crafted for style and comfort │                                    │
│  (Subheading 18px)             │                                    │
│                                │                                    │
│  [SHOP NOW BUTTON] [LEARN MORE]│                                    │
│  (Primary Blue)    (Secondary) │                                    │
│                                │                                    │
│  ✓ Free shipping on orders     │                                    │
│  ✓ 100% Original Products      │                                    │
│  ✓ Expert Customer Support     │                                    │
│                                │                                    │
│  (50% width)                   │  (50% width)                       │
└────────────────────────────────┴────────────────────────────────────┘
```

### Mobile Layout (<750px)
```
┌─────────────────────────────────┐
│  ANNOUNCEMENT BAR (Orange)      │
│  Free Shipping message (compact)│
│  [X]                            │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│      HEADER + NAVIGATION        │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│                                 │
│   LIGHT BLUE BACKGROUND         │
│   #E8F4F8                       │
│                                 │
│   Featured Product Image        │
│   or Placeholder Text           │
│   (250px min-height)            │
│                                 │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  PREMIUM VISION CARE (label)    │
│  ═══════════════════════════════│
│  Discover Your Perfect Frame    │
│  (32px heading on mobile)       │
│                                 │
│  Experience premium eyewear     │
│  crafted for style and comfort  │
│  (16px subheading)              │
│                                 │
│  ┌─────────────────────────────┐│
│  │  SHOP NOW (Full Width)      ││ Primary Button
│  └─────────────────────────────┘│
│                                 │
│  ┌─────────────────────────────┐│
│  │  LEARN MORE (Full Width)    ││ Secondary Button
│  └─────────────────────────────┘│
│                                 │
│  ✓ Free shipping on orders      │
│  ✓ 100% Original Products       │
│  ✓ Expert Customer Support      │
│                                 │
└─────────────────────────────────┘
```

---

## 🎯 Typography Specifications

### Label
- **Font Size:** 13px (0.8125rem)
- **Font Weight:** 500
- **Color:** #6BA3BE (Ivory Blue)
- **Transform:** UPPERCASE
- **Letter Spacing:** 0.12em
- **Margin Bottom:** 1.5rem

### Heading
| Breakpoint | Font Size | Font Weight | Line Height |
|-----------|-----------|-------------|-------------|
| Desktop (990px+) | 52px (3.25rem) | 700 | 1.1 |
| Tablet (750-989px) | 40px (2.5rem) | 700 | 1.1 |
| Mobile (<750px) | 32px (2rem) | 700 | 1.1 |

- **Color:** #1A1A1A (Dark Gray)
- **Letter Spacing:** -0.02em

### Subheading
| Breakpoint | Font Size | Font Weight | Line Height |
|-----------|-----------|-------------|-------------|
| Desktop (990px+) | 18px (1.125rem) | 400 | 1.6 |
| Tablet (750-989px) | 16px (1rem) | 400 | 1.6 |
| Mobile (<750px) | 16px (1rem) | 400 | 1.6 |

- **Color:** #666666 (Medium Gray)
- **Margin Bottom:** 2.5rem (2.5rem desktop, 1.5rem mobile)

---

## 🔘 Button Specifications

### Primary Button
```
┌─────────────────────────────┐
│  SHOP NOW                   │  ← Text (white, 1rem, 500 weight)
│                             │
│  Background: #6BA3BE        │  ← Ivory Blue
│  Padding: 14px 32px         │  ← 0.875rem 2rem
│  Border Radius: 10px        │
│  Box Shadow: 0 4px 12px     │  ← rgba(107, 163, 190, 0.15)
│  Transition: 0.3s ease      │
│                             │
│  On Hover:                  │
│  - Background: #4A7A94      │  ← Darker Blue
│  - Box Shadow: 0 8px 20px   │  ← rgba(107, 163, 190, 0.25)
│  - Transform: translateY(-2px) │ ← Slight lift effect
└─────────────────────────────┘
```

### Secondary Button
```
┌─────────────────────────────┐
│  LEARN MORE                 │  ← Text (blue #6BA3BE, 1rem, 500 weight)
│                             │
│  Background: Transparent    │
│  Border: 1px solid #6BA3BE  │  ← Ivory Blue outline
│  Padding: 14px 32px         │
│  Border Radius: 10px        │
│  Transition: 0.3s ease      │
│                             │
│  On Hover:                  │
│  - Background: #E8F4F8      │  ← Light Blue fill
│  - Border Color: #4A7A94    │  ← Darker Blue
│  - Text Color: #4A7A94      │  ← Darker Blue
└─────────────────────────────┘
```

---

## ✅ Trust Badges

```
════════════════════════════════════
┌────────────────────────────────────┐
│                                    │
│  ✓ Free shipping on orders above   │  ← Checkmark (#6BA3BE)
│    Rs 3,000                        │
│                                    │
│  ✓ 100% Original Products          │  ← Font: 12px (0.75rem)
│    Guaranteed                      │
│                                    │
│  ✓ Expert Customer Support         │  ← Color: #666666
│    Available                       │  ← Gap between mark & text: 8px
│                                    │
└────────────────────────────────────┘
════════════════════════════════════
```

- **Separator:** 1px solid #E8E8E8 (top border)
- **Padding Top:** 2rem (1.5rem mobile)
- **Gap Between Badges:** 12px (0.75rem)
- **Checkmark Font Weight:** 700

---

## 🎨 Color Reference Card

```
┌──────────────────────────────────────────────────────────────┐
│ PRIMARY BLUE (Ivory Blue)     │ HEX: #6BA3BE                 │
│ RGB: 107, 163, 190           │ HSL: 202, 39%, 56%           │
│ USAGE: Buttons, labels, text, borders                      │
├──────────────────────────────────────────────────────────────┤
│ DARK BLUE (Hover State)       │ HEX: #4A7A94                 │
│ RGB: 74, 122, 148            │ HSL: 202, 33%, 43%           │
│ USAGE: Button hover, active states                         │
├──────────────────────────────────────────────────────────────┤
│ LIGHT BLUE (Background)       │ HEX: #E8F4F8                 │
│ RGB: 232, 244, 248           │ HSL: 202, 50%, 94%           │
│ USAGE: Background fills, secondary hover                   │
├──────────────────────────────────────────────────────────────┤
│ DARK GRAY (Text Primary)      │ HEX: #1A1A1A                 │
│ RGB: 26, 26, 26              │ HSL: 0, 0%, 10%              │
│ USAGE: Headings, primary text                              │
├──────────────────────────────────────────────────────────────┤
│ MEDIUM GRAY (Text Secondary)  │ HEX: #666666                 │
│ RGB: 102, 102, 102           │ HSL: 0, 0%, 40%              │
│ USAGE: Subheadings, secondary text, badges                 │
├──────────────────────────────────────────────────────────────┤
│ LIGHT GRAY (Borders)          │ HEX: #E8E8E8                 │
│ RGB: 232, 232, 232           │ HSL: 0, 0%, 91%              │
│ USAGE: Dividers, separator lines                           │
├──────────────────────────────────────────────────────────────┤
│ ANNOUNCEMENT ORANGE           │ HEX: #FF8C00                 │
│ RGB: 255, 140, 0             │ HSL: 33, 100%, 50%           │
│ USAGE: Announcement bar only                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 📐 Spacing & Layout Grid

### Padding (Hero Section)
```
Desktop:  4rem (64px) horizontal | 4rem vertical
Tablet:   3rem (48px) horizontal | 3rem vertical
Mobile:   1.5rem (24px) horizontal | 2.5rem vertical
```

### Gap Specifications
```
Buttons:        1.5rem (24px) gap (desktop)
                1rem (16px) gap (mobile, stacked)
Badges:         0.75rem (12px) between rows
Badge Content:  0.5rem (8px) between checkmark and text
Label/Heading:  1.5rem (24px) below label
Heading/Sub:    1.5rem (24px) between heading and subheading
Sub/Buttons:    2.5rem (40px) between subheading and buttons
Buttons/Badges: 2.5rem (40px) between buttons and badges
```

---

## 🖼️ Image Placeholder Details

### When No Image Uploaded
```
┌─────────────────────────────────┐
│                                 │
│        Light Blue (#E8F4F8)     │
│                                 │
│        Featured Product         │
│        Image Placeholder        │
│                                 │
│   (Text centered, 0.9375rem)    │
│                                 │
└─────────────────────────────────┘
```

### Image Display
- **Background Color:** #E8F4F8 (Light Blue)
- **Object Fit:** cover (maintains aspect ratio, fills container)
- **Responsive Sizes:** `(min-width: 750px) 50vw, 100vw`
- **Fetch Priority:** high (first image on page)
- **Placeholder Text:** "Featured Product\nImage Placeholder"
- **Text Color:** #6BA3BE (Ivory Blue)

---

## 📱 Responsive Behavior Summary

| Feature | Desktop (990px+) | Tablet (750-989px) | Mobile (<750px) |
|---------|-----------------|------------------|-----------------|
| Layout | Split 50/50 (flex row) | Split 50/50 (flex row) | Vertical stack (flex column) |
| Height | 500px min | 500px min | 350px min |
| Heading Size | 52px | 40px | 32px |
| Subheading Size | 18px | 16px | 16px |
| Padding | 4rem 3rem | 3rem 2rem | 2.5rem 1.5rem |
| Buttons | Horizontal flex | Horizontal flex | Full-width stacked |
| Image | Right side | Right side | Top (image on top) |

---

## 🚀 Quick Implementation Checklist

- [x] HTML structure created with proper semantic elements
- [x] CSS styling implemented for all breakpoints
- [x] Block-based customization enabled
- [x] Image handling with fallback placeholder
- [x] Button links configurable via theme editor
- [x] Trust badges implemented with checkmarks
- [x] Responsive design tested across breakpoints
- [x] Color system applied throughout
- [x] Animation transitions smooth (0.3s ease)
- [x] Accessibility considerations included

---

**Last Updated:** April 3, 2026  
**Version:** 1.0 Complete  
**Ready for Production:** ✅ Yes
