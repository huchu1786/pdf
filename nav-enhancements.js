(function () {
  const nav = document.querySelector('.site-nav');
  if (!nav || document.querySelector('.nav-dropdown')) return;

  const navRight = nav.querySelector('.nav-right');
  if (!navRight) return;

  // Determine if we're in a subdirectory by checking the URL
  const url = window.location.href;
  const isInSubfolder = /\/(merge-pdf|compress-pdf|split-pdf|word-counter|gst-calculator|currency-converter|pdf-to-word|pdf-to-excel|all-tools|pdf-tools|image-tools|calculator-tools|age-calculator|bmi-calculator|color-picker|compare-pdf|add-watermark-pdf|add-page-numbers-pdf|alternate-mix-pdf|blog|features|contact|compress-image|crop-image|jpg-to-png|png-to-jpg|crop-pdf|deskew-pdf|edit-pdf|edit-pdf-metadata|email-validator|excel-to-pdf|extract-images-pdf|extract-pages-pdf|flatten-pdf|grayscale-pdf|header-footer-pdf|html-to-pdf|jpg-to-pdf|json-formatter|loan-calculator|password-generator|qr-code-generator|ocr-extract-text|organize-pdf|pdf-to-jpg|pdf-to-pdfa|pdf-to-ppt|pdf-to-text|ppt-to-pdf|protect-pdf|redact-pdf|remove-annotations-pdf|remove-pages-pdf|repair-pdf|resize-image|resize-pdf|rotate-pdf|sign-pdf|word-to-pdf|unlock-pdf|csv-to-excel|date-calculator|percentage-calculator|word-counter|passport-photo)\//.test(url);
  const prefix = isInSubfolder ? '../' : '';

  const groups = [
    {
      title: 'Browse',
      links: [
        ['All Tools', prefix + 'all-tools.html'],
        ['PDF Tools', prefix + 'pdf-tools/index.html'],
        ['Image Tools', prefix + 'image-tools/index.html'],
        ['Calculator Tools', prefix + 'calculator-tools/index.html'],
        ['Blog Guides', prefix + 'blog.html']
      ]
    },
    {
      title: 'Popular',
      links: [
        ['Merge PDF', prefix + 'merge-pdf/index.html'],
        ['Compress PDF', prefix + 'compress-pdf/index.html'],
        ['Split PDF', prefix + 'split-pdf/index.html'],
        ['Passport Photo', prefix + 'passport-photo.html'],
        ['Word Counter', prefix + 'word-counter/index.html'],
        ['GST Calculator', prefix + 'gst-calculator/index.html'],
        ['Currency Converter', prefix + 'currency-converter/index.html']
      ]
    }
  ];

  const quickLinks = [
    ['Home', prefix + 'index.html'],
    ['All Tools', prefix + 'all-tools.html'],
    ['PDF Tools', prefix + 'pdf-tools/index.html'],
    ['Image Tools', prefix + 'image-tools/index.html'],
    ['Passport Photo', prefix + 'passport-photo.html'],
    ['Calculator Tools', prefix + 'calculator-tools/index.html'],
    ['Blog', prefix + 'blog.html'],
    ['Features', prefix + 'features.html'],
    ['Contact', prefix + 'contact.html']
  ];

  const dropdown = document.createElement('div');
  dropdown.className = 'nav-dropdown';
  dropdown.innerHTML = `
    <button class="nav-dropdown-toggle" type="button" aria-expanded="false" aria-haspopup="true" aria-label="Open navigation menu">
      <span class="nav-dropdown-label">Explore</span>
      <span class="nav-dropdown-caret">&#9662;</span>
    </button>
    <div class="nav-dropdown-panel" role="menu">
      <div class="nav-dropdown-grid">
        ${groups.map((group) => `
          <div class="nav-dropdown-group">
            <div class="nav-dropdown-title">${group.title}</div>
            <div class="nav-dropdown-list">
              ${group.links.map(([label, href]) => `<a href="${href}" role="menuitem">${label}</a>`).join('')}
            </div>
          </div>
        `).join('')}
      </div>
      <div class="nav-dropdown-note">Jump between tools, calculators, and guides without going back to the homepage.</div>
    </div>
  `;

  navRight.insertBefore(dropdown, navRight.firstChild);

  const mobileToggle = document.createElement('button');
  mobileToggle.className = 'nav-mobile-toggle';
  mobileToggle.type = 'button';
  mobileToggle.setAttribute('aria-expanded', 'false');
  mobileToggle.setAttribute('aria-label', 'Open site navigation');
  mobileToggle.innerHTML = 'Explore &#9662;';
  navRight.insertBefore(mobileToggle, dropdown);

  const mobilePanel = document.createElement('div');
  mobilePanel.className = 'nav-mobile-panel';
  mobilePanel.style.display = 'none'; // Initial state
  mobilePanel.innerHTML = `
    <div class="nav-dropdown-grid">
      ${groups.map((group) => `
        <div class="nav-dropdown-group">
          <div class="nav-dropdown-title">${group.title}</div>
          <div class="nav-dropdown-list">
            ${group.links.map(([label, href]) => `<a href="${href}" role="menuitem">${label}</a>`).join('')}
          </div>
        </div>
      `).join('')}
    </div>
    <div class="nav-dropdown-note">Jump between tools, calculators, and guides without going back to the homepage.</div>
  `;
  nav.insertAdjacentElement('afterend', mobilePanel);

  const toggle = dropdown.querySelector('.nav-dropdown-toggle');
  const panel = dropdown.querySelector('.nav-dropdown-panel');

  // Ensure initial hidden state for panel
  panel.style.display = 'none';
  panel.style.opacity = '0';
  panel.style.pointerEvents = 'none';

  function closeMenu() {
    dropdown.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    panel.style.display = 'none';
    panel.style.opacity = '0';
    panel.style.pointerEvents = 'none';
  }

  function openMenu() {
    dropdown.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    panel.style.display = 'block';
    setTimeout(() => {
      panel.style.opacity = '1';
      panel.style.pointerEvents = 'auto';
    }, 10);
  }

  function closeMobileMenu() {
    mobilePanel.classList.remove('open');
    mobilePanel.style.display = 'none';
    mobileToggle.setAttribute('aria-expanded', 'false');
  }

  function openMobileMenu() {
    mobilePanel.classList.add('open');
    mobilePanel.style.display = 'block';
    mobileToggle.setAttribute('aria-expanded', 'true');
  }

  function syncResponsive() {
    const isMobile = window.innerWidth <= 900;
    if (isMobile) {
      // Mobile: show one clean menu (mobile panel). Hide desktop dropdown to avoid overlap.
      dropdown.style.display = 'none';
      closeMenu();
    } else {
      dropdown.style.display = '';
    }
  }

  syncResponsive();

  toggle.addEventListener('click', function (event) {
    event.stopPropagation();
    if (dropdown.classList.contains('open')) closeMenu();
    else openMenu();
  });

  dropdown.addEventListener('mouseenter', function () {
    if (window.innerWidth > 900) openMenu();
  });

  dropdown.addEventListener('mouseleave', function () {
    if (window.innerWidth > 900) closeMenu();
  });

  document.addEventListener('click', function (event) {
    if (!dropdown.contains(event.target)) closeMenu();
    if (!mobilePanel.contains(event.target) && !mobileToggle.contains(event.target)) closeMobileMenu();
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      closeMenu();
      closeMobileMenu();
    }
  });

  mobileToggle.addEventListener('click', function (event) {
    event.stopPropagation();
    if (mobilePanel.classList.contains('open')) closeMobileMenu();
    else openMobileMenu();
  });

  window.addEventListener('resize', function () {
    syncResponsive();
    if (window.innerWidth > 900) closeMobileMenu();
  });

  panel.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      closeMenu();
    });
    if (window.location.pathname.replace(/\/index\.html$/, '/').endsWith(link.getAttribute('href').replace(/^\.\.\//, '/').replace(/index\.html$/, ''))) {
      link.style.color = 'var(--red)';
      link.style.background = 'var(--red-tint)';
    }
  });

  mobilePanel.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      closeMobileMenu();
    });
    const normalizedHref = link.getAttribute('href').replace(/^\.\.\//, '/').replace(/index\.html$/, '/');
    if (window.location.pathname.replace(/\/index\.html$/, '/').endsWith(normalizedHref)) {
      link.style.color = 'var(--red)';
      link.style.borderColor = 'var(--red)';
      link.style.background = 'var(--red-tint)';
    }
  });
})();
