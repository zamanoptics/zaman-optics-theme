# Collection Filter System - Visual Testing Guide

## Desktop View (1025px+)

### Expected Layout
```
┌─────────────────────────────────────────────────────────────────┐
│                     Collection Page Header                       │
└─────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────┐
│ 📊 Sort By: [Featured ▼]                                          │
│ Product Count: Showing 16 of 150 products                         │
└──────────────────────────────────────────────────────────────────┘
┌───────────────┬───────────────────────────────────────────────────┐
│   FILTERS     │          PRODUCT GRID (3 COLUMNS)                 │
│               │                                                   │
│ Active Filters│  [Color: Blue ✕]  [Size: Medium ✕]              │
│ [Clear All]   │                                                   │
│               │  ┌──────────┬──────────┬──────────┐              │
│ Frame Shape   │  │ Product 1│ Product 2│ Product 3│              │
│ ✓ Aviator(24) │  ├──────────┼──────────┼──────────┤              │
│ ✓ Wayfarer(18)│  │ Product 4│ Product 5│ Product 6│              │
│ ☐ Cat Eye (12)│  ├──────────┼──────────┼──────────┤              │
│ ☐ Round  (8)  │  │ Product 7│ Product 8│ Product 9│              │
│ + Show More   │  └──────────┴──────────┴──────────┘              │
│               │                                                   │
│ Material      │  [Pagination: 1 2 3 4 ... Next]                  │
│ ✓ Acetate (30)│                                                   │
│ ☐ Metal  (20) │                                                   │
│ ☐ Titanium(15)│                                                   │
│               │                                                   │
│ Size          │                                                   │
│ ✓ Small  (10) │                                                   │
│ ✓ Medium (35) │                                                   │
│ ☐ Large  (25) │                                                   │
│               │                                                   │
│ Color         │                                                   │
│ ✓ Black  (40) │                                                   │
│ ☐ Brown  (30) │                                                   │
│ ☐ Gold   (25) │                                                   │
│               │                                                   │
│ Price Range   │                                                   │
│ [$50] - [$200]│                                                   │
│ [Apply Price] │                                                   │
└───────────────┴───────────────────────────────────────────────────┘
```

### Interactions
- ✅ Click filter group headers to expand/collapse
- ✅ Checkboxes toggle blue (#6BA3BE) when selected
- ✅ Active filters show as dismissible tags
- ✅ "Clear All Filters" button visible when filters active
- ✅ Sidebar stays visible when scrolling
- ✅ Product grid reflows when filters applied

### Verification Checklist
- [ ] Sidebar width is 250px (or configured width)
- [ ] Sidebar has white background (#FFFFFF)
- [ ] Right border is light gray (#E8E8E8)
- [ ] Checkbox styling is custom (not native)
- [ ] Checkboxes turn blue (#6BA3BE) when selected
- [ ] Filter tags display above product grid
- [ ] Each tag has close button (✕)
- [ ] "Clear All Filters" link visible when filters active
- [ ] Hover effects work on all interactive elements
- [ ] Filter counts show in parentheses (e.g., "Aviator (24)")
- [ ] Disabled filters have reduced opacity
- [ ] Sticky positioning works on scroll

---

## Tablet View (751px - 1024px)

### Expected Layout
```
┌───────────────────────────────────────────────────────────────┐
│                  Collection Page Header                       │
└───────────────────────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────────────┐
│ FILTERS (Full Width Above Grid)                               │
├───────────────────────────────────────────────────────────────┤
│ [Color: Blue ✕]  [Size: Medium ✕]                            │
│ [Clear All Filters]                                           │
├───────────────────────────────────────────────────────────────┤
│ Frame Shape [v]   Material [v]   Size [v]   Color [v]         │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────┬──────────────────┐                     │
│  │    Product 1     │    Product 2     │                     │
│  ├──────────────────┼──────────────────┤                     │
│  │    Product 3     │    Product 4     │                     │
│  ├──────────────────┼──────────────────┤                     │
│  │    Product 5     │    Product 6     │                     │
│  └──────────────────┴──────────────────┘                     │
│                                                               │
│                 [Pagination]                                 │
└───────────────────────────────────────────────────────────────┘
```

### Interactions
- ✅ Filters stack horizontally or as expandable groups
- ✅ 2-column product grid
- ✅ Same filter functionality as desktop
- ✅ All tags and buttons functional

### Verification Checklist
- [ ] Sidebar no longer on left
- [ ] Filters appear above product grid
- [ ] Product grid is 2 columns
- [ ] Filter functionality unchanged
- [ ] Active filter tags display
- [ ] Clear All button works

---

## Mobile View (≤750px)

### Initial State
```
┌──────────────────────────────────────────┐
│   Collection Header / Breadcrumb          │
├──────────────────────────────────────────┤
│ [🔍 Filter & Sort]         [Badge: 3]    │
├──────────────────────────────────────────┤
│                                          │
│  ┌──────────────┬──────────────┐        │
│  │  Product 1   │  Product 2   │        │
│  ├──────────────┼──────────────┤        │
│  │  Product 3   │  Product 4   │        │
│  ├──────────────┼──────────────┤        │
│  │  Product 5   │  Product 6   │        │
│  └──────────────┴──────────────┘        │
│                                          │
│       [Pagination: 1 2 3 ...]            │
└──────────────────────────────────────────┘
```

### Filter Button States

**Normal State:**
```
┌─────────────────────────────────┐
│ 🔍 Filter & Sort                │
└─────────────────────────────────┘
```

**With Active Filters (Badge Shows Count):**
```
┌──────────────────────────────────┐
│ 🔍 Filter & Sort         [3]     │  ← Blue badge shows 3 active
└──────────────────────────────────┘
```

### Filter Drawer Open
```
┌──────────────────────────────────────────┐
│ Filters                          [✕]     │  ← Close button
├──────────────────────────────────────────┤
│ Frame Shape                      [v]     │  ← Collapsible
│ ☑ Aviator (24)                          │
│ ☑ Wayfarer (18)                         │
│ ☐ Cat Eye (12)                          │
│ ☐ Round (8)                             │
│ ☐ Rectangle (15)                        │
│ + Show More                             │
│                                          │
│ Material                         [>]     │  ← Collapsed
│                                          │
│ Size                             [>]     │  ← Collapsed
│                                          │
│ Gender                           [>]     │  ← Collapsed
│                                          │
│ Color                            [>]     │  ← Collapsed
│                                          │
│ Price Range                      [>]     │  ← Collapsed
│                                          │
│ ────────────────────────────────────    │
│ [Clear All Filters]                      │
│                                          │
│ 📊 Sort By: [Featured ▼]                 │
│                                          │
│ Product Count: Showing 12 of 150         │
└──────────────────────────────────────────┘
```

### Interactions
- ✅ Click "Filter & Sort" button to open drawer
- ✅ Drawer slides up as full-screen overlay
- ✅ Body scroll disabled while drawer open
- ✅ Click close button (✕) to dismiss drawer
- ✅ Click outside drawer area to close (optional)
- ✅ First filter group expanded by default
- ✅ Other groups collapsed to save space
- ✅ Badge count updates as filters selected
- ✅ "Clear All Filters" visible at bottom

### Verification Checklist
- [ ] "Filter & Sort" button appears at 750px and below
- [ ] Button has filter icon (3 horizontal lines)
- [ ] Badge displays only when filters active
- [ ] Badge shows correct count
- [ ] Badge has blue background (#6BA3BE)
- [ ] Button click opens full-screen drawer
- [ ] Drawer covers entire screen
- [ ] Drawer has semi-transparent backdrop (optional)
- [ ] Close button (✕) in top-right corner
- [ ] First filter group expanded initially
- [ ] Other groups collapsed initially
- [ ] Clicking group header expands/collapses
- [ ] Checkboxes work in drawer
- [ ] Filter counts display accurately
- [ ] Active filters show checkmarks
- [ ] "Show More" button works
- [ ] "Clear All Filters" button at bottom
- [ ] Sort dropdown visible in drawer
- [ ] Product count displays
- [ ] Scroll allowed within drawer
- [ ] Body scroll disabled when drawer open
- [ ] Close button closes drawer
- [ ] Drawer closes when window resizes to desktop
- [ ] No layout shift on open/close

---

## Interactive Element Testing

### Checkbox Behavior

**Default State:**
```
☐ Aviator (24)
```
- Border: Gray (#999)
- Background: White
- Text: Dark (#1A1A1A)

**Hover State:**
```
☐ Aviator (24)  ← Border becomes blue
```
- Border: Blue (#6BA3BE)
- Cursor: Pointer

**Checked State:**
```
☑ Aviator (24)  ← Blue background with checkmark
```
- Background: Blue (#6BA3BE)
- Border: Blue (#6BA3BE)
- Checkmark: White (✓)
- Text: Blue (#6BA3BE) - emphasis

**Disabled State:**
```
☐ Round (0)     ← Reduced opacity
```
- Opacity: 50%
- Cursor: Not-allowed
- Cannot interact

### Filter Tag Behavior

**Tag Display:**
```
[Color: Blue ✕]  [Size: Medium ✕]
```

**Tag Hover:**
```
[Color: Blue ✕]  ← Background darkens
```
- Background: #ebebeb
- Border: Blue (#6BA3BE)

**Tag Click:**
```
Click ✕ to remove filter
```
- Removes tag from display
- Updates URL parameters
- Refreshes product grid
- Updates badge count

### Button Interactions

**Mobile Filter Button - Normal:**
```
[🔍 Filter & Sort]
```
- Background: White (#FFFFFF)
- Border: Light Gray (#E8E8E8)
- Text: Dark (#1A1A1A)

**Mobile Filter Button - Hover:**
```
[🔍 Filter & Sort]  ← Background lightens
```
- Background: #f5f5f5
- Border: Blue (#6BA3BE)
- Cursor: Pointer

**Mobile Filter Button - Active (Drawer Open):**
```
[🔍 Filter & Sort]  ← May show pressed state
```
- Background: #ebebeb
- Border: Blue (#6BA3BE)

**Close Button - Normal:**
```
[✕]
```
- Background: Transparent
- Color: Dark (#1A1A1A)
- Size: Appropriate for touch (40x40px minimum)

**Close Button - Hover:**
```
[✕]  ← Color changes to blue
```
- Color: Blue (#6BA3BE)
- Cursor: Pointer

---

## Responsive Breakpoints Testing

### Breakpoint 1: 750px (Mobile/Desktop threshold)
- **Below 750px:** Mobile view (Filter button visible, sidebar hidden)
- **At 750px:** Transition to mobile
- **Above 750px:** Tablet/Desktop view (Filter button hidden, sidebar shown)

**Test Steps:**
1. Load page at 1200px (desktop)
2. Resize browser window to 751px
3. Verify sidebar still visible
4. Resize to 750px
5. Verify sidebar hidden and button appears
6. Resize back to 751px
7. Verify sidebar reappears and button hidden

### Breakpoint 2: 1024px (Tablet/Desktop threshold)
- **Below 1024px:** Sidebar above grid (stacked)
- **At 1024px:** Transition to sidebar layout
- **Above 1024px:** Sidebar beside grid (side-by-side)

**Test Steps:**
1. Load page at 1200px (sidebar beside grid)
2. Resize to 1024px
3. Verify grid layout adjusted
4. Resize to 750px
5. Verify mobile layout

---

## Performance Testing

### Load Time Checks
- [ ] CSS loads without blocking render (<5s)
- [ ] JavaScript loads asynchronously (<3s)
- [ ] No layout shift on page load (CLS < 0.1)
- [ ] Filter interactions responsive (<100ms)
- [ ] Drawer animation smooth (60fps)

### Memory Usage
- [ ] No memory leaks on filter toggle
- [ ] No accumulation on repeated filtering
- [ ] Efficient event listener management

### Animation Smoothness
- [ ] Drawer open/close smooth
- [ ] Filter group collapse/expand smooth
- [ ] Checkbox checked animation smooth
- [ ] Badge count update instant

---

## Accessibility Testing

### Keyboard Navigation
- [ ] Tab key moves through filters
- [ ] Enter/Space toggles checkboxes
- [ ] Tab order is logical
- [ ] Focus indicators visible
- [ ] Escape closes drawer (optional)

### Screen Reader Testing
- [ ] Filter group labels announced
- [ ] Checkbox states announced (checked/unchecked)
- [ ] Badge count announced
- [ ] Button purposes clear
- [ ] Error messages announced

### Color Contrast
- [ ] Text on background meets WCAG AA (4.5:1)
- [ ] Active filter tags readable
- [ ] Checkbox labels readable
- [ ] No color-only information

### Reduced Motion
- [ ] Works without animations
- [ ] Transitions respect prefers-reduced-motion
- [ ] No layout issues with animations disabled

---

## Edge Cases & Error Handling

### No Filters Available
```
[No filters configured]
Filter button should appear disabled or hidden
```

### No Products Matching Filters
```
[Product grid shows empty message]
"We couldn't find any products matching your filters"
"Clear filters to see all products"
```

### Very Long Filter Names
```
Frame Shape: "Extra Extra Large Round Frame"
Should wrap or truncate appropriately
```

### Many Active Filters
```
[Filter Tag 1] [Filter Tag 2] [Filter Tag 3] [Filter Tag 4]
[Filter Tag 5] [Filter Tag 6]
```
Tags should wrap to multiple lines if needed

### Very Long Filter Lists
```
Material: 50+ options
"Show More" button should paginate the list
```

### Slow Network
- Filters should still function
- Loading state should be visible
- No timeout errors

### JavaScript Disabled
- [ ] Page still loads
- [ ] Products visible
- [ ] Filters may not work (graceful degradation)

---

## Cross-Browser Testing

| Browser | Version | Desktop | Tablet | Mobile | Notes |
|---------|---------|---------|--------|--------|-------|
| Chrome | Latest | ✅ | ✅ | ✅ | Primary testing |
| Firefox | Latest | ✅ | ✅ | ✅ | |
| Safari | Latest | ✅ | ✅ | ✅ | Test on actual device |
| Edge | Latest | ✅ | ✅ | ✅ | |
| Chrome Mobile | Latest | | ✅ | ✅ | Use DevTools |
| Safari iOS | Latest | | ✅ | ✅ | Test on device |
| Chrome Android | Latest | | ✅ | ✅ | Test on device |

---

## Deployment Checklist

- [ ] All CSS files minified
- [ ] All JavaScript files minified
- [ ] Assets properly linked in section file
- [ ] No 404 errors for asset files
- [ ] Mobile button appears at correct breakpoint
- [ ] Desktop sidebar displays correctly
- [ ] Filter drawer opens/closes smoothly
- [ ] All interactive elements functional
- [ ] No console errors or warnings
- [ ] Accessibility features working
- [ ] Theme preview shows correct styling
- [ ] Performance metrics acceptable
- [ ] All browsers tested
- [ ] Responsive design verified
- [ ] Documentation complete
- [ ] Ready for production deploy

---

## Test Result Template

Use this template to document your testing results:

```
Test Date: ________________
Tester: ____________________
Browser: ___________________
Device: ____________________
OS: _______________________

Desktop View (1025px+):
  Sidebar Display: ☐ Pass ☐ Fail
  Filter Styling: ☐ Pass ☐ Fail
  Checkbox Colors: ☐ Pass ☐ Fail
  Active Tags: ☐ Pass ☐ Fail
  Clear All Button: ☐ Pass ☐ Fail
  Sticky Sidebar: ☐ Pass ☐ Fail

Mobile View (≤750px):
  Filter Button: ☐ Pass ☐ Fail
  Badge Count: ☐ Pass ☐ Fail
  Drawer Open: ☐ Pass ☐ Fail
  Drawer Close: ☐ Pass ☐ Fail
  Filter Groups: ☐ Pass ☐ Fail
  Checkboxes: ☐ Pass ☐ Fail

Interactions:
  Filter Toggle: ☐ Pass ☐ Fail
  Tag Removal: ☐ Pass ☐ Fail
  Pagination: ☐ Pass ☐ Fail
  Sort Dropdown: ☐ Pass ☐ Fail

Performance:
  Load Time: __________ ms
  Animation FPS: _______ fps
  CLS Score: __________ 

Accessibility:
  Keyboard Nav: ☐ Pass ☐ Fail
  Screen Reader: ☐ Pass ☐ Fail
  Color Contrast: ☐ Pass ☐ Fail
  Focus Indicators: ☐ Pass ☐ Fail

Issues Found:
1. ___________________
2. ___________________
3. ___________________

Overall Status: ☐ Ready ☐ Needs Fixes ☐ Blocked

Notes:
________________________________
________________________________
________________________________
```
