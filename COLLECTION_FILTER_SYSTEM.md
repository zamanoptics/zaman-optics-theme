# Zaman Optics - Collection Filter System Documentation

## Overview

A comprehensive product grid filter system for the Zaman Optics Shopify theme with responsive design, featuring a desktop sidebar and mobile drawer implementation.

## Features

### Desktop Layout
- **Left Sidebar Filters**: White background (#FFFFFF) with #E8E8E8 right border
- **3-Column Product Grid**: Responsive grid layout alongside sidebar
- **Sticky Filter Panel**: Filters remain visible while scrolling
- **Collapsible Filter Groups**: Frame Shape, Material, Size, Gender, Color, Price Range
- **Active Filter Tags**: Dismissible tags showing selected filters
- **Clear All Filters Button**: One-click filter reset

### Mobile Layout
- **Filter & Sort Button**: Slide-up drawer toggle with active filter count badge (#6BA3BE)
- **Full-Screen Drawer**: Overlay-style filter panel
- **Header with Close Button**: Clear navigation within mobile drawer
- **Responsive Grid**: 2-column layout that adapts to screen size

### Filter Options
- **Frame Shape**: Aviator, Wayfarer, Cat Eye, Round, Rectangle, etc.
- **Material**: Acetate, Metal, Titanium, etc.
- **Size**: Small, Medium, Large
- **Gender**: Men, Women, Unisex
- **Color**: Available product colors
- **Price Range**: Min/Max price inputs with dynamic updates

### Sort Options
- Featured
- Price: Low to High
- Price: High to Low
- Newest
- Best Selling

## File Structure

### CSS Files
- **`assets/collection-filters-enhanced.css`** (620+ lines)
  - Complete styling for filter sidebar
  - Mobile drawer styles
  - Responsive breakpoints (750px for mobile, 1024px for tablet)
  - Custom checkbox styling (#6BA3BE primary color)
  - Filter tag and badge styling
  - Accessibility features

### JavaScript Files
- **`assets/collection-filters-enhanced.js`** (70+ lines)
  - Mobile drawer open/close functionality
  - Filter badge count management
  - Accessibility enhancements
  - Shopify theme editor integration

### Section Files
- **`sections/main-collection-product-grid.liquid`** (Updated)
  - Mobile filter button with badge
  - Mobile filter header with close button
  - Enhanced filter wrapper
  - Integration of new assets

## Design System Colors

```css
--filter-blue: #6BA3BE              /* Primary checkbox/active state */
--filter-blue-hover: #4A7A94         /* Hover state */
--filter-border: #E8E8E8             /* Border and divider lines */
--filter-bg: #FFFFFF                 /* Background */
--text-primary: #1A1A1A              /* Primary text */
--text-secondary: #666666            /* Secondary text */
```

## Responsive Behavior

### Desktop (1025px+)
- Sidebar displayed on left (250px width)
- Products grid takes remaining width
- Filter groups expanded by default (first group open)
- Sort dropdown visible above product count

### Tablet (751px - 1024px)
- Sidebar positioned above product grid
- Full width filter section
- Checkbox styling maintained

### Mobile (750px and below)
- "Filter & Sort" button appears at top
- Sidebar hidden (slides in as drawer)
- Full-screen overlay when open
- Filter badge shows active filter count
- All filter groups collapsed by default
- Responsive 2-column product grid

## Implementation Details

### Mobile Filter Button

```html
<button type="button" class="mobile-filter-sort-button">
  <svg class="filter-icon"><!-- Filter icon --></svg>
  <span>Filter & Sort</span>
  <span class="filter-count-badge">3</span>
</button>
```

The badge automatically updates as users toggle filters.

### Filter Drawer

```html
<aside class="facets-wrapper mobile-open">
  <div class="filters-header">
    <h2>Filters</h2>
    <button class="filters-header__close">×</button>
  </div>
  <!-- Filter groups -->
</aside>
```

Clicking the close button (×) dismisses the drawer and allows scrolling again.

### Active Filter Tags

```html
<div class="active-facets">
  <span class="active-facets__button-inner">
    Color: Blue
    <svg><!-- Close icon --></svg>
  </span>
</div>
```

Each tag includes a close button for removing individual filters.

### Checkbox Styling

Custom checkboxes with:
- Bordered style by default
- #6BA3BE background when checked
- Smooth transitions
- Checkmark indicator
- Hover states with border color change

## URL Parameters

Filter selections are preserved in URL parameters:
- `?filter.p.product.frame_shape=aviator`
- `?filter.p.product.material=acetate`
- `?filter.p.product.price=50-200`

**Pagination** automatically maintains active filters:
- `/collections/eyewear?page=2&filter.p.product.color=black`

## Accessibility Features

- ✅ Keyboard navigation (Tab, Enter, Space, Escape)
- ✅ ARIA labels and roles
- ✅ Focus indicators on all interactive elements
- ✅ Semantic HTML structure
- ✅ Visually-hidden text for screen readers
- ✅ Focus trapping in mobile drawer
- ✅ Reduced motion support

## Customization Guide

### Change Primary Color

Edit `assets/collection-filters-enhanced.css`:

```css
:root {
  --filter-blue: #YourColor;
  --filter-blue-hover: #YourHoverColor;
}
```

### Modify Sidebar Width

```css
.facets-vertical {
  grid-template-columns: 300px 1fr; /* Change 250px to desired width */
}
```

### Adjust Filter Groups

Edit the facets snippet to customize which filter groups appear:

```liquid
{% render 'facets',
  results: collection,
  enable_filtering: section.settings.enable_filtering,
  enable_sorting: section.settings.enable_sorting,
  filter_type: section.settings.filter_type,
  paginate: paginate
%}
```

### Add/Remove Sort Options

Modify the sort dropdown in the `facets` snippet or section settings.

## Performance Considerations

- CSS uses native grid and flexbox for optimal performance
- Minimal JavaScript (no heavy DOM manipulation)
- Filter changes trigger native Shopify facets.js
- Mobile drawer uses CSS transforms for smooth animations
- Lazy loading compatible with existing quick-add features

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari 14+, Chrome Mobile)

## Testing Checklist

- [ ] Desktop filter sidebar displays correctly
- [ ] Mobile filter button shows/hides drawer
- [ ] Filter badge count updates accurately
- [ ] Active filters display as dismissible tags
- [ ] "Clear All Filters" button works
- [ ] Close button closes mobile drawer
- [ ] Filters persist across pagination
- [ ] Keyboard navigation works
- [ ] Responsive behavior at breakpoints
- [ ] Sort dropdown functions
- [ ] Product count displays correctly
- [ ] No layout shift on drawer open/close

## Integration with Existing Systems

The enhanced filter system:
- ✅ Uses existing Shopify `facets.js` for filtering logic
- ✅ Maintains compatibility with component-facets.css
- ✅ Works with pagination component
- ✅ Integrates with theme editor
- ✅ Supports quick-add functionality
- ✅ Compatible with all product card types

## Troubleshooting

### Badge not showing count
- Ensure JavaScript file is loaded: `collection-filters-enhanced.js`
- Check browser console for errors
- Verify checkboxes have correct selector: `.facets__display-vertical input[type="checkbox"]`

### Mobile drawer not closing
- Check if CSS transitions are disabled in browser settings
- Verify close button element exists
- Check for JavaScript errors in console

### Filters not persisting on pagination
- Confirm collection uses standard Shopify pagination
- Check URL parameters are being passed correctly
- Verify facets.js is properly initialized

### Checkbox color not appearing
- Ensure CSS custom property `--filter-blue` is defined
- Check for CSS specificity conflicts
- Verify browser supports CSS custom properties

## Future Enhancement Ideas

- Animated transitions between filter states
- Filter search/quick-select for large filter lists
- Visual swatch options for color/material filters
- Price slider instead of input fields
- Filter presets/saved searches
- Analytics integration for popular filters
- A/B testing for filter layouts

## Support & Maintenance

For updates or customizations:
1. Test changes in theme preview first
2. Backup existing CSS/JS files
3. Use theme editor live preview
4. Monitor console for deprecation warnings
5. Update documentation with custom changes
