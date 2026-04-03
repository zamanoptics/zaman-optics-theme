# Why Choose Us / Trust Features Section - Implementation Guide

## Overview

The **Why Choose Us** section is a static informational component that showcases trust features and key benefits of Zaman Optics. It displays 4 feature cards in a responsive grid layout with emojis, titles, and descriptions.

## File Created
- `sections/trust-features.liquid` - Main section file
- `assets/section-trust-features.css` - Styling (optional, included inline in section)
- **Modified:** `templates/index.json` - Added section to homepage

## Features

### Layout
- **Desktop:** 4-column grid (1 row of 4 cards)
- **Tablet:** 2-column grid (2 rows of 2 cards)
- **Mobile:** 1-column grid (4 rows of 1 card)

### Background & Spacing
- **Background Color:** Light gray (#F5F5F5)
- **Top Padding:** 60px (50px tablet, 40px mobile)
- **Bottom Padding:** 60px (50px tablet, 40px mobile)
- **Horizontal Padding:** 2rem (1.5rem tablet, 1rem mobile)

### Card Components
Each trust feature card includes:

1. **Icon (Emoji)**
   - Size: 32px (28px mobile)
   - Margin Bottom: 24px (16px mobile)
   - Display: Block, centered

2. **Title**
   - Font Size: 16px (15px mobile)
   - Font Weight: 700 (bold)
   - Color: #1A1A1A (dark gray)
   - Margin Bottom: 12px

3. **Description**
   - Font Size: 14px (13px mobile)
   - Color: #666666 (medium gray)
   - Line Height: 1.6
   - Descriptive, benefit-focused text

### Card Styling
- **Background:** White (#FFFFFF)
- **Border Radius:** 10px
- **Padding:** 40px 24px (32px 20px tablet, 28px 20px mobile)
- **Box Shadow:** 0 2px 8px rgba(0, 0, 0, 0.08)
- **Text Align:** Center
- **No Hover Effects** - Static informational section

## Default Trust Features

1. **🔬 Prescription Guaranteed**
   - "Every pair made to your exact prescription by certified opticians"

2. **🚚 Fast Delivery Across Pakistan**
   - "Delivered to your door in 3–5 business days. Free above Rs 3,000"

3. **💳 Easy Payment**
   - "Cash on Delivery, EasyPaisa & JazzCash accepted"

4. **🔄 Hassle-Free Returns**
   - "7-day return policy. Not satisfied? We'll fix it"

## Customization from Shopify Admin

### Section Settings
- **Section Title** - Change "Why Choose Zaman Optics?" to custom text

### Block Settings (per feature card)
Each of the 4 feature card blocks can be customized with:
- **Icon** - Any emoji or symbol (e.g., 🔬, 🚚, 💳, 🔄, etc.)
- **Title** - Feature name or heading
- **Description** - Detailed explanation of the benefit

### Adding/Removing Cards
- Maximum 4 cards (limit set in schema)
- Can customize title, description, and icon
- Perfect for adding new benefits or updating existing ones

## Styling Details

### Colors
| Element | Color | Hex |
|---------|-------|-----|
| Background | Light Gray | #F5F5F5 |
| Card BG | White | #FFFFFF |
| Title | Dark Gray | #1A1A1A |
| Description | Medium Gray | #666666 |
| Shadow | Black 8% opacity | rgba(0,0,0,0.08) |

### Spacing
| Element | Desktop | Tablet | Mobile |
|---------|---------|--------|--------|
| Section Padding | 60px 2rem | 50px 1.5rem | 40px 1rem |
| Grid Gap | 2rem | 1.5rem | 1.25rem |
| Card Padding | 2.5rem 1.5rem | 2rem 1.25rem | 1.75rem 1.25rem |
| Icon Size | 32px | 32px | 28px |
| Title Size | 16px | 16px | 15px |
| Desc Size | 14px | 14px | 13px |

### Responsive Breakpoints
- **Desktop:** 990px+ (4 columns)
- **Tablet:** 750px - 989px (2 columns)
- **Mobile:** <750px (1 column)

## Technical Implementation

### Shopify Liquid Structure
```liquid
<div class="trust-features-section">
  <h2 class="trust-features-section__title">{{ section.settings.section_title }}</h2>
  
  <div class="trust-features-grid">
    {%- for block in section.blocks -%}
      <div class="trust-feature-card">
        <span class="trust-feature-card__icon">{{ block.settings.icon }}</span>
        <h3 class="trust-feature-card__title">{{ block.settings.title }}</h3>
        <p class="trust-feature-card__description">{{ block.settings.description }}</p>
      </div>
    {%- endfor -%}
  </div>
</div>
```

### CSS Grid Implementation
```css
.trust-features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);  /* Desktop: 4 columns */
  gap: 2rem;
}

@media (max-width: 989px) {
  grid-template-columns: repeat(2, 1fr);  /* Tablet: 2 columns */
}

@media (max-width: 749px) {
  grid-template-columns: 1fr;             /* Mobile: 1 column */
}
```

## Integration in templates/index.json

The section is registered in the homepage template with the following structure:
```json
"trust_features": {
  "type": "trust-features",
  "blocks": { /* 4 feature blocks */ },
  "block_order": [ /* order of blocks */ ],
  "settings": { "section_title": "Why Choose Zaman Optics?" }
}
```

The section appears in this order on the homepage:
1. Image Banner (Hero)
2. Category Grid
3. **Trust Features** ← NEW
4. Featured Collection

## Accessibility Features
- Semantic HTML: `<h2>` for section title, `<h3>` for card titles
- Proper heading hierarchy
- Text-based descriptions (not icon-only)
- Readable font sizes and contrast ratios
- Mobile-friendly touch targets (cards at least 48px height)

## Performance Considerations
- No JavaScript required
- CSS Grid for modern layout support
- Emoji icons (no image loading)
- Minimal CSS overhead
- Fast rendering and loading

## Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- CSS Grid support required
- Flexbox support required
- iOS Safari and Android browsers

## Common Customizations

### Change Section Title
1. Edit `templates/index.json` (trust_features section)
2. Modify "section_title" setting
3. Save and publish

### Change Feature Details
1. Go to Shopify Admin → Online Store → Homepage
2. Edit "Why Choose Us" section
3. Click each feature card to modify icon, title, description
4. Save and preview

### Add Custom Icons
- Replace emojis with your own (Unicode symbols)
- Or use inline SVG if custom icons needed
- Examples: ⭐, ✓, ✨, 🎯, etc.

### Adjust Colors
1. Edit `assets/section-trust-features.css` or inline styles
2. Update background-color (#F5F5F5)
3. Update card background (#FFFFFF)
4. Update text colors (#1A1A1A, #666666)
5. Test across all pages

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Section not showing | Verify section is in templates/index.json order array |
| Grid not responsive | Clear cache, check viewport meta tag |
| Text overflow | Adjust padding or font-size in CSS |
| Icons not displaying | Verify emoji is valid Unicode character |
| Spacing looks wrong | Check responsive breakpoints in CSS media queries |
| Colors not matching | Verify hex codes, clear browser cache |

## Testing Checklist

- [ ] Desktop view (4 columns) displays correctly
- [ ] Tablet view (2x2 grid) displays correctly
- [ ] Mobile view (1 column) displays correctly
- [ ] Background color (#F5F5F5) correct
- [ ] Card background (#FFFFFF) correct
- [ ] Icon emojis display properly
- [ ] Title text is bold (700 weight)
- [ ] Description text is readable
- [ ] Padding and spacing match design
- [ ] Section title is customizable from admin
- [ ] All 4 default features have correct content
- [ ] Section loads without errors
- [ ] No layout shift or jumping content
- [ ] Accessible on screen readers

## Optional Enhancements

1. **Add Icons as SVG** - Replace emojis with custom SVG icons
2. **Add Animations** - Fade-in effect on scroll
3. **Add Links** - Make cards clickable to detail pages
4. **Add Counters** - Show statistics (e.g., "10,000+ Happy Customers")
5. **Add Testimonials** - Include customer reviews with this section

## Section Schema

The section includes:
- **Editable title** - Customize from theme editor
- **4 blocks maximum** - For 4 feature cards
- **Per-block customization** - Icon, title, description
- **Preset configuration** - Default 4 features pre-loaded

---

**Last Updated:** April 3, 2026  
**Version:** 1.0  
**Status:** Ready for Production ✅

For questions or modifications, refer to the main documentation files or contact theme support.
