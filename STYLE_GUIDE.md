# Zaman Optics Style Guide

## Brand Feel

Zaman Optics should feel premium, clean, local, trustworthy, and easy to shop. The interface should support repeated shopping tasks, not look like a generic landing page.

## Color Tokens

```css
--zaman-orange: #FF8C00;
--zaman-orange-dark: #DF7600;
--zaman-orange-soft: #FFF3E0;
--zaman-black: #1A1A1A;
--zaman-muted: #6F6A63;
--zaman-border: #E8E2DA;
--zaman-surface: #F7F7F5;
--zaman-white: #FFFFFF;
```

## Usage

- Use `#FF8C00` for primary CTAs, active states, focus rings, and small accents.
- Use `#1A1A1A` for headings, primary text, and black CTAs.
- Use white cards on warm gray or white page backgrounds.
- Avoid old blue accents. They do not belong in the current brand system.
- Do not use orange shadows as the default product-card hover. Use neutral premium shadows.

## Shape and Elevation

- Buttons: `10px`
- Inputs: `10px`
- Cards: `10px` to `16px`
- Large panels: `16px` to `22px`
- Product images: soft gray/warm surface background with `object-fit: contain`

## Buttons

Primary:
- Orange background
- White text
- 10px radius
- Slight lift on hover

Secondary:
- White background
- Black border/text
- Black background and white text on hover

Black CTA:
- Use for strong purchase actions where contrast is needed, such as Add to Cart in the prescription flow.

## Product Cards

Product cards should:
- Keep full eyewear frame visible
- Use contained product imagery
- Show price clearly in black
- Use orange only for active/CTA accents
- Avoid cropped frame images

## Prescription Flow

The prescription flow should be clear and compact:
- Frame Only and With Prescription options first
- Manual/upload prescription entry
- Lens type, material, coatings
- Quoted total shown before Add to Cart
- All selected options saved as line item properties

## Pakistan Localization

Use:
- PKR / Rs
- Cash on Delivery
- EasyPaisa
- JazzCash
- WhatsApp support
- Delivery across Pakistan

Avoid:
- Dollar pricing
- International shipping copy unless actually supported
- Virtual try-on claims unless implemented
