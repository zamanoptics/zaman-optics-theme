import os

header_css_content = """
.farmart-header {
  background-color: var(--color-background-primary, #FFFFFF);
  border-bottom: 1px solid var(--color-border-light, #E8E8E8);
}

.farmart-header__top {
  padding: 15px 0;
  border-bottom: 1px solid var(--color-border-light, #E8E8E8);
}

.farmart-header__top-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
}

.farmart-header__logo img {
  max-width: 100%;
  height: auto;
}

.farmart-search-form {
  display: flex;
  width: 100%;
  max-width: 600px;
  border: 2px solid var(--color-brand-primary, #FF8C00);
  border-radius: 5px;
  overflow: hidden;
}

.farmart-search-input {
  flex-grow: 1;
  padding: 10px 15px;
  border: none;
  outline: none;
}

.farmart-search-btn {
  background-color: var(--color-brand-primary, #FF8C00);
  color: #FFFFFF;
  border: none;
  padding: 0 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.farmart-header__icons {
  display: flex;
  align-items: center;
  gap: 20px;
}

.farmart-icon-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
  color: var(--color-text, #1A1A1A);
  position: relative;
}

.farmart-icon-label {
  font-size: 12px;
  margin-top: 5px;
}

.farmart-cart-count {
  position: absolute;
  top: -5px;
  right: 0;
  background-color: var(--color-brand-primary, #FF8C00);
  color: #FFFFFF;
  font-size: 10px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.farmart-header__bottom {
  padding: 10px 0;
}

.farmart-nav__list {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 30px;
}

.farmart-nav__link {
  text-decoration: none;
  color: var(--color-text, #1A1A1A);
  font-weight: 600;
  transition: color 0.3s;
}

.farmart-nav__link:hover, .farmart-nav__link--active {
  color: var(--color-brand-primary, #FF8C00);
}
"""

header_liquid_content = """{{ 'section-header.css' | asset_url | stylesheet_tag }}
<header class="farmart-header">
  <!-- Top Row: Logo, Search, User/Cart -->
  <div class="farmart-header__top">
    <div class="page-width farmart-header__top-inner">
      <!-- Main Logo -->
      <div class="farmart-header__logo">
        {% if section.settings.logo != blank %}
          {%- assign image_size = section.settings.logo_width | append: 'x' -%}
          <img srcset="{{ section.settings.logo | img_url: image_size }} 1x, {{ section.settings.logo | img_url: image_size, scale: 2 }} 2x"
            src="{{ section.settings.logo | img_url: image_size }}"
            loading="lazy"
            class="header__heading-logo"
            width="{{ section.settings.logo.width }}"
            height="{{ section.settings.logo.height }}"
            alt="{{ section.settings.logo.alt | default: shop.name | escape }}">
        {% else %}
          <span class="h2">{{ shop.name }}</span>
        {% endif %}
      </div>
      
      <!-- Center Search Bar -->
      <div class="farmart-header__search">
        <form action="{{ routes.search_url }}" method="get" role="search" class="farmart-search-form">
          <input class="farmart-search-input" type="search" name="q" placeholder="I'm shopping for..." value="{{ search.terms | escape }}">
          <button class="farmart-search-btn" type="submit">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
          </button>
        </form>
      </div>
      
      <!-- Right Icons -->
      <div class="farmart-header__icons">
        {% if shop.customer_accounts_enabled %}
          <a href="{% if customer %}{{ routes.account_url }}{% else %}{{ routes.account_login_url }}{% endif %}" class="farmart-icon-link">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
               <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
               <circle cx="12" cy="7" r="4"></circle>
            </svg>
            <span class="farmart-icon-label">{% if customer %}Account{% else %}Sign In{% endif %}</span>
          </a>
        {% endif %}
        
        <a href="{{ routes.cart_url }}" class="farmart-icon-link farmart-cart-icon">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
             <circle cx="9" cy="21" r="1"></circle>
             <circle cx="20" cy="21" r="1"></circle>
             <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
          </svg>
          <span class="farmart-icon-label">Cart</span>
          <span class="farmart-cart-count">{{ cart.item_count }}</span>
        </a>
      </div>
    </div>
  </div>
  
  <!-- Bottom Row: Navigation menu -->
  <div class="farmart-header__bottom">
    <div class="page-width">
      <nav class="farmart-nav">
        <ul class="farmart-nav__list">
          {%- for link in linklists[section.settings.menu].links -%}
            <li class="farmart-nav__item">
              <a href="{{ link.url }}" class="farmart-nav__link {% if link.active %}farmart-nav__link--active{% endif %}">
                {{ link.title }}
              </a>
            </li>
          {%- endfor -%}
        </ul>
      </nav>
    </div>
  </div>
</header>
{% schema %}
{
  "name": "t:sections.header.name",
  "class": "section-header",
  "settings": [
    {
      "type": "image_picker",
      "id": "logo",
      "label": "t:sections.header.settings.logo.label"
    },
    {
      "type": "range",
      "id": "logo_width",
      "min": 50,
      "max": 250,
      "step": 10,
      "default": 100,
      "unit": "t:sections.header.settings.logo_width.unit",
      "label": "t:sections.header.settings.logo_width.label"
    },
    {
      "type": "link_list",
      "id": "menu",
      "default": "main-menu",
      "label": "t:sections.header.settings.menu.label"
    }
  ]
}
{% endschema %}
"""

with open(r"C:\Users\lenovo\Desktop\Zaman-Optics\assets\section-header.css", "w", encoding="utf-8") as f:
    f.write(header_css_content)

with open(r"C:\Users\lenovo\Desktop\Zaman-Optics\sections\header.liquid", "w", encoding="utf-8") as f:
    f.write(header_liquid_content)

print("Done generating header files.")
