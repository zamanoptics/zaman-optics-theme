/**
 * FAQ Page Accordion Functionality
 * Vanilla JavaScript implementation for smooth open/close animations
 */

document.addEventListener('DOMContentLoaded', function() {
  const accordionTriggers = document.querySelectorAll('.faq-accordion__trigger');

  accordionTriggers.forEach(trigger => {
    trigger.addEventListener('click', function() {
      const isExpanded = this.getAttribute('aria-expanded') === 'true';
      const content = this.nextElementSibling;

      // Get the current section (parent of parent)
      const section = this.closest('.faq-page__section');
      const otherTriggers = section.querySelectorAll('.faq-accordion__trigger');

      // Close all other items in the same section
      otherTriggers.forEach(otherTrigger => {
        if (otherTrigger !== this && otherTrigger.getAttribute('aria-expanded') === 'true') {
          otherTrigger.setAttribute('aria-expanded', 'false');
          otherTrigger.nextElementSibling.hidden = true;
        }
      });

      // Toggle current item
      this.setAttribute('aria-expanded', !isExpanded);
      content.hidden = isExpanded;

      // Handle animation
      if (!isExpanded) {
        // Opening
        content.hidden = false;
        // Trigger reflow to enable transition
        content.offsetHeight;
      }
    });

    // Keyboard support
    trigger.addEventListener('keydown', function(event) {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        this.click();
      }
    });
  });

  // Optional: Support for opening accordion from URL hash
  if (window.location.hash) {
    const targetId = window.location.hash.substring(1);
    const targetElement = document.getElementById(targetId);

    if (targetElement && targetElement.classList.contains('faq-accordion__item')) {
      const trigger = targetElement.querySelector('.faq-accordion__trigger');
      if (trigger && trigger.getAttribute('aria-expanded') === 'false') {
        trigger.click();
        setTimeout(() => {
          targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 300);
      }
    }
  }
});

/**
 * Optional: Helper function to programmatically open/close accordion items
 * Usage: toggleAccordionItem('my-item-id', true)
 */
function toggleAccordionItem(itemId, shouldOpen) {
  const item = document.getElementById(itemId);
  if (!item) return false;

  const trigger = item.querySelector('.faq-accordion__trigger');
  const isCurrentlyOpen = trigger.getAttribute('aria-expanded') === 'true';

  if ((shouldOpen && !isCurrentlyOpen) || (!shouldOpen && isCurrentlyOpen)) {
    trigger.click();
    return true;
  }
  return false;
}

/**
 * Optional: Close all accordion items
 */
function closeAllAccordions() {
  const allTriggers = document.querySelectorAll('.faq-accordion__trigger');
  allTriggers.forEach(trigger => {
    if (trigger.getAttribute('aria-expanded') === 'true') {
      trigger.click();
    }
  });
}

/**
 * Optional: Open all accordion items
 */
function openAllAccordions() {
  const allTriggers = document.querySelectorAll('.faq-accordion__trigger');
  allTriggers.forEach(trigger => {
    if (trigger.getAttribute('aria-expanded') === 'false') {
      trigger.click();
    }
  });
}
