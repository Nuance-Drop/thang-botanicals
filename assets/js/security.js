// Security Module for THANG Botanicals
// Handles input validation, rate limiting, and secure webhook submission

class SecurityManager {
  constructor() {
    this.encryptedWebhook = "{{ site.n8n_webhook_prefix }}"; // Base64 encoded
    this.submissionKey = 'thang_last_submission';
    this.rateLimitMinutes = 5;
    this.maxAttempts = 3;
    this.attemptKey = 'thang_attempts';
  }

  // Simple XOR obfuscation (not encryption, but hides from basic scrapers)
  decodeWebhook() {
    const encoded = this.encryptedWebhook;
    const decoded = atob(encoded);
    return decoded;
  }

  validateEmail(email) {
    // Strict email regex
    const re = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
    return re.test(String(email).toLowerCase());
  }

  sanitizeInput(input) {
    // Remove HTML tags and trim
    return input.replace(/<[^>]*>/g, '').trim().substring(0, 100);
  }

  checkRateLimit() {
    const lastSubmission = localStorage.getItem(this.submissionKey);
    if (!lastSubmission) return true;
    
    const now = new Date().getTime();
    const last = parseInt(lastSubmission);
    const diff = (now - last) / (1000 * 60); // minutes
    
    if (diff < this.rateLimitMinutes) {
      return false;
    }
    
    // Reset attempts after rate limit period
    localStorage.removeItem(this.attemptKey);
    return true;
  }

  getTimeUntilNext() {
    const lastSubmission = localStorage.getItem(this.submissionKey);
    if (!lastSubmission) return 0;
    
    const now = new Date().getTime();
    const last = parseInt(lastSubmission);
    const diff = (now - last) / (1000 * 60);
    return Math.ceil(this.rateLimitMinutes - diff);
  }

  incrementAttempts() {
    let attempts = parseInt(localStorage.getItem(this.attemptKey) || '0');
    attempts++;
    localStorage.setItem(this.attemptKey, attempts.toString());
    return attempts;
  }

  recordSubmission() {
    localStorage.setItem(this.submissionKey, new Date().getTime().toString());
  }

  async submitToN8N(data) {
    // CSP-compliant fetch with specific headers
    const webhookUrl = this.decodeWebhook();
    
    try {
      const response = await fetch(webhookUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
          'Origin': window.location.origin
        },
        body: JSON.stringify({
          ...data,
          timestamp: new Date().toISOString(),
          source: window.location.href,
          userAgent: navigator.userAgent.substring(0, 100) // Truncated for privacy
        })
      });
      
      if (!response.ok) throw new Error('Network response was not ok');
      return { success: true, message: 'Subscribed successfully' };
      
    } catch (error) {
      console.error('Submission error:', error);
      return { success: false, message: 'Submission failed. Please try again.' };
    }
  }

  showAlert(message, type = 'error') {
    const existing = document.querySelector('.security-alert');
    if (existing) existing.remove();
    
    const alert = document.createElement('div');
    alert.className = `alert ${type} security-alert`;
    alert.textContent = message;
    
    const form = document.getElementById('newsletter-form');
    if (form) {
      form.parentNode.insertBefore(alert, form);
      setTimeout(() => alert.remove(), 5000);
    }
  }
}

// Initialize
const security = new SecurityManager();

// Newsletter form handler
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('newsletter-form');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Rate limiting
    if (!security.checkRateLimit()) {
      const wait = security.getTimeUntilNext();
      security.showAlert(`Please wait ${wait} minutes before subscribing again.`, 'error');
      return;
    }
    
    // Get and validate inputs
    const emailInput = document.getElementById('email-input');
    const email = security.sanitizeInput(emailInput.value);
    
    if (!security.validateEmail(email)) {
      emailInput.classList.add('error');
      security.showAlert('Please enter a valid email address.', 'error');
      setTimeout(() => emailInput.classList.remove('error'), 2000);
      return;
    }
    
    // Check honeypot (anti-spam hidden field)
    const honeypot = document.getElementById('website-url');
    if (honeypot && honeypot.value) {
      // Bot detected, fake success
      security.showAlert('Subscribed successfully!', 'success');
      form.reset();
      return;
    }
    
    // Submit
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="loading-dots"><span></span><span></span><span></span></span>';
    
    const result = await security.submitToN8N({
      email: email,
      type: 'newsletter_signup',
      tags: ['coming_soon_page', '2025_launch']
    });
    
    submitBtn.disabled = false;
    submitBtn.textContent = originalText;
    
    if (result.success) {
      security.recordSubmission();
      security.showAlert(result.message, 'success');
      form.reset();
      // Trigger confetti or success animation here
    } else {
      security.incrementAttempts();
      security.showAlert(result.message, 'error');
    }
  });
});

// Export for global access
window.securityManager = security;