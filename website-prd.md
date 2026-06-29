# Zaman Optics Website PRD

## 1. Overview

Zaman Optics is a modern optical retail store based in Gujar Khan, Punjab, Pakistan. The Shopify storefront should make buying eyewear online feel simple, premium, and trustworthy.

The core feature is a product-page prescription workflow where customers can select a frame, choose lens options, enter/upload prescription details, and submit the configuration with the order.

## 2. Brand System

- Primary orange: `#FF8C00`
- Primary black: `#1A1A1A`
- Canvas: `#FFFFFF`
- Surface: `#F5F5F5` / warm premium gray
- Radius: `10px`
- Visual tone: minimalist, premium, spacious, soft shadows

## 3. Navigation and Collections

Primary collections:
- Eyeglasses
- Sunglasses
- Blue Light Glasses
- Kids Glasses
- Contact Lenses

Filtering dimensions:
- Frame Shape: Round, Square, Rectangle, Aviator, Cat Eye
- Material: Metal, Acetate, Plastic
- Gender: Men, Women, Unisex, Kids
- Size: Medium, Wide
- Price range

Search & Discovery should be configured in Shopify Admin for metafield-based filters. The theme also includes a fallback tag-filter UI.

## 4. Product Page Modes

### Prescription Mode

Applies to:
- Eyeglasses
- Blue Light Glasses
- Kids Glasses

Required flow:
1. Frame Only vs With Prescription
2. Manual prescription entry or upload file
3. Lens type: Single Vision, Progressive, Bifocal
4. Lens material: Standard, UV Protection, Blue Cut, Photochromic
5. Optional coatings: Anti-Glare, Anti-Scratch, Anti-Fog
6. Live quoted total
7. Add to Cart / Buy Now

Captured order data:
- Order Type
- Prescription Method
- Right Eye SPH/CYL/Axis
- Left Eye SPH/CYL/Axis
- PD
- Prescription File
- Lens Type
- Lens Material
- Coatings
- Quoted Total Rs

### Standard Mode

Applies to:
- Sunglasses

Required flow:
- Product gallery
- Variant selection if applicable
- Quantity
- Add to Cart
- Buy Now / dynamic checkout when enabled
- No prescription workflow

## 5. Pricing Note

Shopify line item properties store configuration details but do not change checkout price. For automatic lens upgrade charging, implement one of:
- Lens upgrade variants
- Add-on products
- Shopify product options/pricing app

## 6. Homepage

Required sections:
1. Announcement bar
2. Header
3. Hero
4. Category grid
5. Best Sellers
6. Why Choose Us
7. Customer Reviews
8. FAQ
9. Footer

## 7. Pakistan Localization

Required:
- PKR / Rs pricing
- Generic payment visibility only: secure online payments available
- Exact payment methods should appear only after they are confirmed live in Shopify
- Credit/debit card visibility
- WhatsApp support
- Delivery across Pakistan
- Avoid unsupported international shipping or virtual try-on claims

## 8. Static Pages

Built templates:
- Lens Guide
- Size Guide
- Prescription Guide
- FAQ
- About
- Contact

Still needs admin assignment/content confirmation for actual Shopify pages.

## 9. Launch Checklist

- Configure Search & Discovery filters
- Confirm product metafields
- Configure Pakistan shipping zones
- Enable the store's supported payment methods
- Confirm exact payment names before mentioning them in customer-facing copy
- Upload real product and category images
- Add real WhatsApp number
- Test prescription order in Shopify Admin
- Confirm lens upgrade charging approach
