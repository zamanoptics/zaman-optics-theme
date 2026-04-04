# Complete Homepage & Navigation Rebuild Plan

## Status: IMPLEMENTATION IN PROGRESS

This document tracks all required changes for the complete redesign of the Zaman Optics homepage and navigation.

### PART 1: ANNOUNCEMENT BAR ✅ IN PROGRESS
**File**: `sections/announcement-bar.liquid`

Requirements:
- ✅ Background: #AFDCEC (light blue)
- ✅ Text color: #1A1A1A (black)  
- ✅ Height: 38px
- ✅ Dismiss button with localStorage
- ✅ Mobile responsive (padding adjustments)

Status: Partially updated - main content converted. Need to finish removing old Shopify code.

---

### PART 2: HEADER REDESIGN
**File**: `sections/header.liquid`

Requirements:
- Logo text "Zaman Optics" 22px bold + lens icon in #AFDCEC
- Navigation: Home | Collections | Lens Guide | Size Guide | About | Contact
- Search, Account, Cart icons on right (22px, #1A1A1A, hover #AFDCEC)
- Cart badge with count (#AFDCEC background, #1A1A1A text)
- Height: 64px with bottom border 1px #E8E8E8
- Sticky position with shadow on scroll
- Mobile: hamburger opens slide-in drawer

Status: TODO - Complete rewrite needed

---

### PART 3: CATEGORY NAVIGATION
**File**: `sections/category-nav.liquid`

Categories:
1. 👓 Eyeglasses → /collections/eyeglasses
2. Men's Frames → /collections/eyeglasses?filter.p.m.custom.gender=Men
3. Women's Frames → /collections/eyeglasses?filter.p.m.custom.gender=Women
4. 💻 Blue Light → /collections/blue-light-glasses
5. 👦 Kids Glasses → /collections/kids-glasses
6. 🕶️ Sunglasses → /collections/sunglasses
7. ✨ New Arrivals → /collections/all?sort_by=created-descending
8. 🔥 Best Sellers → /collections/all?sort_by=best-selling

Styling:
- Border: 1.5px #AFDCEC
- Hover: #AFDCEC background + shadow
- Active: #AFDCEC background + 600 weight

Status: TODO - Colors need updating from #6BA3BE to #AFDCEC

---

### PART 4: HERO SECTION
**File**: `sections/image-banner.liquid` or create new `sections/hero.liquid`

Layout: 50% text (left) | 50% image placeholder (right) on desktop

**LEFT SIDE**:
- Label: "PAKISTAN'S TRUSTED OPTICAL STORE" (11px, 600 weight, #AFDCEC, uppercase, letter-spacing 2px)
- Headline: "Find Your Perfect Pair of Glasses" (46px desktop / 30px mobile, 800 weight, #1A1A1A, line-height 1.15)
- Subheadline: Description text (17px, #555555, line-height 1.7, max-width 480px)
- Two buttons side-by-side:
  * Primary: "Shop Eyeglasses" → #AFDCEC bg, #1A1A1A text, 14px 600 weight
  * Secondary: "View All Frames" → transparent bg, 1.5px #1A1A1A border
- Trust badges (below buttons): ✓ Free Delivery | ✓ Cash on Delivery | ✓ Prescription Guaranteed

**RIGHT SIDE**:
- Placeholder: #E8F6FB background, 420px height, "Hero Image" text centered in #AFDCEC
- Make this an image setting in schema

Status: TODO - Complete redesign

---

### PART 5: COLLECTION PAGE FILTERS
**File**: `templates/collection.liquid`

Layout:
- Desktop: Left sidebar 260px (fixed) | Right content (3-column grid)
- Mobile: "Filter & Sort" button opens bottom drawer

Filter Groups:
1. **Frame Shape**: Round | Square | Rectangle | Aviator | Cat Eye
   - Param: `filter.p.m.custom.frame_shape`

2. **Material**: Metal | Acetate | Plastic
   - Param: `filter.p.m.custom.material`

3. **Gender**: Men | Women | Unisex | Kids
   - Param: `filter.p.m.custom.gender`

4. **Size**: Medium | Wide
   - Param: `filter.p.m.custom.size`

5. **Price Range**: Min/Max inputs with Apply button
   - Param: `filter.v.price`

Styling:
- Checkbox accent: #AFDCEC
- Active filters shown as dismissible tags
- "Clear All" link in #CC4444
- Sort dropdown: border 1px #E8E8E8, white background

Product Cards:
- Border: 1px #E8E8E8
- Hover: box-shadow 0 4px 16px rgba(0,0,0,0.08), border #AFDCEC
- "Add to Cart": #AFDCEC background, #1A1A1A text

Status: TODO

---

### PART 6: GLOBAL UPDATES NEEDED

#### All CSS files - Color replacements:
- [ ] Remove all #FF8C00 (orange)
- [ ] Replace #6BA3BE with #AFDCEC
- [ ] Replace #4A7A94 with #7FB8CC  
- [ ] Replace #E8F4F8 with #E8F6FB
- ✅ Already done in most files

#### All Liquid files - Text removal:
- [ ] Remove "Welcome to our store" bar completely
- [ ] Update nav to show: Home | Collections | Lens Guide | Size Guide | About | Contact
- [ ] Remove any orange color inline styles

#### Button styling across site:
- ✅ Filled buttons: #AFDCEC background, #1A1A1A text
- [ ] Outlined buttons: 1.5px #1A1A1A border, transparent background
- [ ] NO orange buttons anywhere

#### Links:
- ✅ Default: #1A1A1A
- ✅ Hover: #AFDCEC with underline

---

### HOME PAGE SECTION ORDER (templates/index.json)

Required order:
1. announcement-bar
2. header  
3. category-nav
4. image-banner (hero)
5. category-grid
6. featured-products
7. trust-features
8. footer

---

### Files to Create/Modify

#### NEW FILES:
- `sections/hero.liquid` - New hero section with redesigned layout
- `css/hero.css` - Hero styling (optional, can be inline)

#### MODIFY:
- ✅ `sections/announcement-bar.liquid` - In progress
- `sections/header.liquid` - Complete redesign
- `sections/category-nav.liquid` - Color updates  
- `sections/image-banner.liquid` - Or replace with new hero
- `templates/collection.liquid` - Add filter sidebar
- `templates/index.json` - Update section order
- All CSS files - Already updated with colors

---

### VERIFICATION CHECKLIST

After all changes:
- [ ] No #FF8C00 in any file (git grep "#FF8C00")
- [ ] No "Welcome to our store" text in HTML
- [ ] All buttons follow new color scheme
- [ ] Links are #1A1A1A by default, #AFDCEC on hover
- [ ] Announcement bar shows with localStorage dismissal
- [ ] Header sticky with 64px height
- [ ] Category nav shows 8 buttons, scrolls on mobile
- [ ] Hero has 50/50 split layout on desktop
- [ ] Collection page has left sidebar filters
- [ ] All pages responsive (tested at 320px, 750px, 990px+)

---

### NEXT IMMEDIATE STEPS

1. Finish `announcement-bar.liquid` - remove old Shopify code block
2. Create new `sections/header.liquid` with new design
3. Update `sections/category-nav.liquid` colors
4. Create new hero section
5. Update `templates/index.json` section order
6. Test announcement dismissal in browser
7. Test responsive design on mobile
8. Final color/orange audit with grep
9. Commit all changes to git

---

**Last Updated**: April 4, 2026
**Target Completion**: When all sections fully implemented
