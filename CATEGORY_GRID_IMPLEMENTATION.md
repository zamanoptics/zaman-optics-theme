# Category Grid Section - Implementation Guide

## Overview
The **Shop by Category** section is a card-based category navigation component for the homepage. It displays 6 category cards in a responsive grid layout with customizable images and links.

## File Created
- `sections/category-grid.liquid` - Main section file
- `assets/section-category-grid.css` - Styling (optional, included inline in section)
- **Modified:** `templates/index.json` - Added section to homepage

## Features

### Layout
- **Desktop:** 3-column grid (3 cards per row)
- **Tablet:** 2-column grid (2 cards per row)
- **Mobile:** 1-column grid (1 card per row, full width)

### Card Components
Each category card includes:
1. **Image Placeholder (200px height)**
   - Light gray background (#F5F5F5)
   - Accepts uploaded images from Shopify admin
   - Placeholder text if no image uploaded
   - Proper aspect ratio handling with object-fit: cover

2. **Category Name**
   - Font size: 16px (1rem)
   - Font weight: 600
   - Color: #1A1A1A (dark gray)
   - Centered alignment

3. **Category Subtitle**
   - Font size: 13px (0.8125rem)
   - Color: #666666 (medium gray)
   - Centered alignment
   - Positioned below category name

### Interactions
- **Hover Effect:**
  - Card lifts up: `transform: translateY(-4px)`
  - Blue border appears: `border-color: #6BA3BE`
  - Shadow deepens: `0 8px 20px rgba(0, 0, 0, 0.12)`
  - Entire card is clickable (anchor tag wrapper)

### Default Categories
1. **Eyeglasses** → `/collections/eyeglasses` — "Prescription Frames"
2. **Sunglasses** → `/collections/sunglasses` — "UV Protection"
3. **Blue Light Glasses** → `/collections/blue-light-glasses` — "Screen Protection"
4. **Kids Glasses** → `/collections/kids-glasses` — "For Ages 4–16"
5. **New Arrivals** → `/collections/all?sort_by=created-descending` — "Just Landed"
6. **Best Sellers** → `/collections/all?sort_by=best-selling` — "Most Popular"

### Additional Elements
- **Section Title:** "Shop by Category" (centered, 32px/2rem, bold)
- **Footer Link:** "View All Collections →" (centered, blue text #6BA3BE)

## Customization from Shopify Admin

### Section Settings
- **Section Title** - Change the main heading text

### Block Settings (per category card)
Each of the 6 category card blocks can be customized with:
- **Category Name** - Display name of the category
- **Category Subtitle** - Short description text
- **Category Link** - URL/collection link
- **Category Image** - Upload an image from Shopify (optional)

## Styling Details

### Colors
| Element | Color | Hex |
|---------|-------|-----|
| Heading | Dark Gray | #1A1A1A |
| Subtitle | Medium Gray | #666666 |
| Link Text | Ivory Blue | #6BA3BE |
| Link Hover | Darker Blue | #4A7A94 |
| Image Background | Light Gray | #F5F5F5 |
| Card Shadow | Black with opacity | rgba(0, 0, 0, 0.08) |
| Card Background | White | #FFFFFF |
| Card Border (hover) | Ivory Blue | #6BA3BE |

### Spacing
| Element | Value |
|---------|-------|
| Section Padding (Desktop) | 4rem 2rem |
| Grid Gap (Desktop) | 2rem |
| Card Padding | 1.5rem |
| Image Height | 200px |
| Name/Subtitle Gap | 0.5rem |

### Responsive Breakpoints
- **Desktop:** 1000px+
- **Tablet:** 750px - 989px (2 columns, reduced padding)
- **Mobile:** <750px (1 column, optimized spacing)

## Technical Implementation

### Shopify Liquid Structure
```liquid
<!-- Category Grid Section -->
<div class="category-grid-section">
  <h2>Section Title</h2>
  
  <div class="category-grid">
    {%- for block in section.blocks -%}
      <a href="{{ block.settings.category_link }}" class="category-card">
        <div class="category-card__image-wrapper">
          <!-- Image or placeholder -->
        </div>
        <div class="category-card__content">
          <h3 class="category-card__name">{{ Name }}</h3>
          <p class="category-card__subtitle">{{ Subtitle }}</p>
        </div>
      </a>
    {%- endfor -%}
  </div>
  
  <a href="/collections/all" class="category-grid-section__link">
    View All Collections →
  </a>
</div>
```

### CSS Grid Implementation
```css
.category-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* Desktop: 3 columns */
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
"category_grid": {
  "type": "category-grid",
  "blocks": { /* 6 category blocks */ },
  "block_order": [ /* order of blocks */ ],
  "settings": { "section_title": "Shop by Category" }
}
```

The section appears in this order on the homepage:
1. Image Banner (Hero)
2. **Category Grid** ← NEW
3. Featured Collection

## Image Handling

### For Merchants Uploading Images
1. Go to Shopify Admin → Online Store → Homepage
2. Click "Add section" or edit existing "Shop by Category" section
3. For each category card, click "Select image" to upload
4. Recommended image dimensions: **500px × 500px or square aspect ratio**
5. Images will automatically crop to fit the 200px height container

### Image Specifications
- Supported formats: PNG, JPG, GIF, WebP
- Aspect ratio: Any (will use object-fit: cover)
- Recommended: Square (1:1) for best visual results
- Size: Optimize to <100KB for faster loading

## Accessibility Features
- Semantic HTML: `<a>` for entire card link, `<h2>` and `<h3>` for headings
- Proper contrast ratios for WCAG compliance
- Image alt text automatically populated from category name
- Screen reader friendly link text

## Performance Considerations
- CSS Grid for modern layout support
- Responsive image sizing with Shopify's `image_tag` filter
- Efficient image loading with size hints
- No JavaScript required for basic functionality

## Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- CSS Grid support required
- Flexbox support required
- iOS Safari and Android browsers

## Common Customizations

### Change Grid Columns
Modify the `grid-template-columns` property in CSS:
```css
/* 4 columns instead of 3 */
.category-grid {
  grid-template-columns: repeat(4, 1fr);
}
```

### Adjust Card Height
Modify `.category-card__image-wrapper` height:
```css
.category-card__image-wrapper {
  height: 250px; /* Change from 200px */
}
```

### Change Hover Effect
Modify the `.category-card:hover` styles:
```css
.category-card:hover {
  transform: scale(1.02); /* Scale instead of translateY */
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Images not displaying | Ensure image is uploaded in Shopify admin; check file format |
| Grid not responsive | Verify CSS is being loaded; check viewport meta tag in theme |
| Text overflow | Adjust padding or font-size in responsive breakpoints |
| Cards not clickable | Ensure link URL is valid; check href attribute value |
| Placeholder text showing | Upload image in Shopify admin for that category card |

## Testing Checklist

- [ ] Desktop view (3 columns) displays correctly
- [ ] Tablet view (2 columns) displays correctly
- [ ] Mobile view (1 column) displays correctly
- [ ] Hover effect (lift + blue border) works on desktop
- [ ] Cards are clickable and navigate to correct URLs
- [ ] Images display properly when uploaded
- [ ] Placeholder text displays when no image uploaded
- [ ] Title text is customizable from admin
- [ ] All 6 default categories have correct names, subtitles, and links
- [ ] "View All Collections" link works and points to /collections/all
- [ ] Section loads without JavaScript errors
