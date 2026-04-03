// Enhanced Collection Filter System - Mobile Drawer & Filter Management
// Zaman Optics

class CollectionFilterManager {
  constructor() {
    this.filterButton = document.querySelector('.mobile-filter-sort-button');
    this.filterWrapper = document.querySelector('.facets-wrapper');
    this.closeButton = document.querySelector('.filters-header__close');
    this.html = document.documentElement;
    
    this.init();
  }

  init() {
    if (!this.filterButton || !this.filterWrapper) return;

    // Mobile filter button toggle
    this.filterButton.addEventListener('click', () => this.toggleFilters());
    
    // Close button in drawer
    if (this.closeButton) {
      this.closeButton.addEventListener('click', () => this.closeFilters());
    }

    // Close on overlay click
    document.addEventListener('click', (e) => {
      if (e.target === this.filterWrapper && window.innerWidth <= 750) {
        this.closeFilters();
      }
    });

    // Update filter badge count
    this.updateFilterBadge();

    // Update filter badge when checkboxes change
    const checkboxes = document.querySelectorAll('.facets__display-vertical input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', () => this.updateFilterBadge());
    });

    // Close filters when window resizes to desktop
    window.addEventListener('resize', () => {
      if (window.innerWidth > 750) {
        this.filterWrapper.classList.remove('mobile-open');
        this.html.style.overflow = '';
      }
    });

    // Collapse all filter groups initially on mobile
    if (window.innerWidth <= 750) {
      const filterDetails = document.querySelectorAll('.facets__disclosure-vertical');
      filterDetails.forEach((detail, index) => {
        if (index > 0) {
          detail.removeAttribute('open');
        }
      });
    }
  }

  toggleFilters() {
    if (this.filterWrapper.classList.contains('mobile-open')) {
      this.closeFilters();
    } else {
      this.openFilters();
    }
  }

  openFilters() {
    this.filterWrapper.classList.add('mobile-open');
    this.html.style.overflow = 'hidden';
    
    // Focus management for accessibility
    const firstFocusable = this.filterWrapper.querySelector('button, input, [tabindex]');
    if (firstFocusable) {
      firstFocusable.focus();
    }
  }

  closeFilters() {
    this.filterWrapper.classList.remove('mobile-open');
    this.html.style.overflow = '';
  }

  updateFilterBadge() {
    const checkedFilters = document.querySelectorAll(
      '.facets__display-vertical input[type="checkbox"]:checked'
    ).length;
    
    const badge = document.querySelector('.filter-count-badge');
    if (badge) {
      if (checkedFilters > 0) {
        badge.textContent = checkedFilters;
        badge.style.display = 'inline-flex';
      } else {
        badge.style.display = 'none';
      }
    }
  }
}

// Initialize on DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new CollectionFilterManager();
  });
} else {
  new CollectionFilterManager();
}

// Handle Shopify theme editor updates
if (window.Shopify && window.Shopify.designMode) {
  document.addEventListener('shopify:section:load', () => {
    new CollectionFilterManager();
  });
}
