# Zaman Optics Shopify Theme

Custom Shopify/Dawn theme for **Zaman Optics**, an optical retailer in Gujar Khan, Punjab, Pakistan.

The theme is built around a premium minimalist eyewear shopping experience with a product-page prescription lens workflow, collection filtering, Pakistan payment trust cues, and guide pages for lens, size, and prescription education.

## Current Status

Last updated: May 21, 2026

### Built
- Premium global design system in `assets/premium-design.css`
- Custom two-row desktop header and mobile drawer
- Dismissible announcement bar
- Homepage hero, category grid, featured products, trust section, reviews, and FAQ
- Custom collection page with left filter sidebar, mobile filter drawer, sort controls, and premium product cards
- Product page mode detection:
  - `prescription` for eyeglasses, blue light glasses, and kids glasses
  - `standard` for sunglasses
- Prescription workflow with:
  - Frame Only / With Prescription toggle
  - Manual prescription entry for OD/OS SPH, CYL, Axis, and PD
  - Prescription file upload
  - Lens type, lens material, and coating options
  - Live quoted total
  - Shopify line item properties for order admin visibility
- Cart page displays line item properties and payment trust badges
- Static guide templates:
  - Lens guide
  - Size guide
  - Prescription guide
  - FAQ
  - About
  - Contact uses Dawn contact form with Zaman styling
- Branded 404 page
- Footer with shop/help/contact links and Pakistan payment badges

### Important Shopify Limitation

The prescription workflow stores a **quoted total** and all selected options as line item properties. Shopify line item properties do not change the checkout price by themselves.

To charge lens upgrades automatically, use one of these approaches:
- Create paid lens-upgrade variants
- Add hidden lens add-on products to cart
- Use a Shopify product options/pricing app

The current implementation is intentionally honest: it captures the configuration and quoted total for staff confirmation.

## Development

```bash
shopify theme dev --store zaman-optics-2.myshopify.com
shopify theme pull
shopify theme push
```

If the store URL has changed, confirm it before running Shopify CLI commands.

## Git Workflow

```bash
git status
git add .
git commit -m "Update storefront functionality"
git push origin main
```

## Key Files

| Area | Files |
|---|---|
| Global design | `assets/premium-design.css`, `assets/base.css` |
| Header | `sections/header.liquid`, `assets/zaman-header.css` |
| Homepage | `templates/index.json`, `sections/image-banner.liquid`, `sections/category-grid.liquid`, `sections/featured-products.liquid`, `sections/why-choose-us.liquid`, `sections/reviews.liquid`, `sections/faq.liquid` |
| Collections | `sections/main-collection-product-grid.liquid` |
| Product page | `sections/main-product.liquid`, `snippets/buy-buttons.liquid`, `snippets/prescription-workflow.liquid`, `assets/section-prescription.css` |
| Cart | `sections/main-cart-items.liquid`, `sections/main-cart-footer.liquid` |
| Static pages | `sections/page-lens-guide.liquid`, `sections/page-size-guide.liquid`, `sections/page-prescription-guide.liquid`, `sections/page-faq.liquid`, `sections/page-about.liquid` |
| Footer | `sections/footer.liquid`, `assets/footer-custom.css` |
| Product upload/admin setup | `PRODUCT_UPLOAD_GUIDE.md` |
| Store structure guide | `ZAMAN_OPTICS_STORE_GUIDE.md`, `ZAMAN_OPTICS_STORE_GUIDE.pdf` |

## Design Rules

- Primary orange: `#FF8C00`
- Primary black: `#1A1A1A`
- Surface gray: `#F5F5F5`
- Canvas white: `#FFFFFF`
- Border radius: `10px`
- UI feel: minimalist, premium, spacious, soft shadows

## Admin Tasks Still Required

- Install and configure Shopify Search & Discovery for metafield filters
- Confirm product metafields are populated consistently
- Configure Pakistan shipping zones
- Enable Cash on Delivery
- Configure EasyPaisa/JazzCash/card payment methods
- Upload real hero, category, and product photography
- Add real WhatsApp number and live contact details
- Test a complete live order from product page to Shopify Admin

## Product Upload Rules

Use `PRODUCT_UPLOAD_GUIDE.md` when adding products. At minimum, each product needs a product type, collection, price, two images, fallback tags, and these required metafields:

- `custom.product_mode`
- `custom.frame_shape`
- `custom.material`
- `custom.gender`
- `custom.size`
