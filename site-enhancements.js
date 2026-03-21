(function () {
  const path = window.location.pathname || '';
  const parts = path.split('/').filter(Boolean);
  const last = parts[parts.length - 1] || '';
  const endsWithFile = /\.[a-z0-9]+$/i.test(last);
  const prefix = endsWithFile ? (parts.length > 1 ? '../' : '') : (parts.length >= 1 ? '../' : '');

  const toHref = function (target) {
    return prefix + target;
  };

  const catalog = [
    { slug: 'passport-photo', name: 'Passport Photo Maker', category: 'image', path: 'passport-photo.html' },
    { slug: 'merge-pdf', name: 'Merge PDF', category: 'pdf', path: 'merge-pdf/index.html' },
    { slug: 'compress-pdf', name: 'Compress PDF', category: 'pdf', path: 'compress-pdf/index.html' },
    { slug: 'split-pdf', name: 'Split PDF', category: 'pdf', path: 'split-pdf/index.html' },
    { slug: 'rotate-pdf', name: 'Rotate PDF', category: 'pdf', path: 'rotate-pdf/index.html' },
    { slug: 'unlock-pdf', name: 'Unlock PDF', category: 'pdf', path: 'unlock-pdf/index.html' },
    { slug: 'protect-pdf', name: 'Protect PDF', category: 'pdf', path: 'protect-pdf/index.html' },
    { slug: 'add-watermark-pdf', name: 'Add Watermark', category: 'pdf', path: 'add-watermark-pdf/index.html' },
    { slug: 'remove-pages-pdf', name: 'Remove Pages', category: 'pdf', path: 'remove-pages-pdf/index.html' },
    { slug: 'organize-pdf', name: 'Organize PDF', category: 'pdf', path: 'organize-pdf/index.html' },
    { slug: 'crop-pdf', name: 'Crop PDF', category: 'pdf', path: 'crop-pdf/index.html' },
    { slug: 'pdf-to-word', name: 'PDF to Word', category: 'convert', path: 'pdf-to-word/index.html' },
    { slug: 'pdf-to-excel', name: 'PDF to Excel', category: 'convert', path: 'pdf-to-excel/index.html' },
    { slug: 'ppt-to-pdf', name: 'PowerPoint to PDF', category: 'convert', path: 'ppt-to-pdf/index.html' },
    { slug: 'pdf-to-jpg', name: 'PDF to JPG', category: 'convert', path: 'pdf-to-jpg/index.html' },
    { slug: 'word-to-pdf', name: 'Word to PDF', category: 'convert', path: 'word-to-pdf/index.html' },
    { slug: 'excel-to-pdf', name: 'Excel to PDF', category: 'convert', path: 'excel-to-pdf/index.html' },
    { slug: 'jpg-to-pdf', name: 'JPG to PDF', category: 'convert', path: 'jpg-to-pdf/index.html' },
    { slug: 'edit-pdf', name: 'Edit PDF', category: 'pdf', path: 'edit-pdf/index.html' },
    { slug: 'extract-pages-pdf', name: 'Extract Pages', category: 'pdf', path: 'extract-pages-pdf/index.html' },
    { slug: 'repair-pdf', name: 'Repair PDF', category: 'pdf', path: 'repair-pdf/index.html' },
    { slug: 'ocr-extract-text', name: 'OCR / Extract Text', category: 'pdf', path: 'ocr-extract-text/index.html' },
    { slug: 'sign-pdf', name: 'Sign PDF', category: 'pdf', path: 'sign-pdf/index.html' },
    { slug: 'redact-pdf', name: 'Redact PDF', category: 'pdf', path: 'redact-pdf/index.html' },
    { slug: 'compare-pdf', name: 'Compare PDF', category: 'pdf', path: 'compare-pdf/index.html' },
    { slug: 'html-to-pdf', name: 'HTML to PDF', category: 'convert', path: 'html-to-pdf/index.html' },
    { slug: 'pdf-to-pdfa', name: 'PDF to PDF/A', category: 'convert', path: 'pdf-to-pdfa/index.html' },
    { slug: 'add-page-numbers-pdf', name: 'Page Numbers', category: 'pdf', path: 'add-page-numbers-pdf/index.html' },
    { slug: 'pdf-to-ppt', name: 'PDF to PowerPoint', category: 'convert', path: 'pdf-to-ppt/index.html' },
    { slug: 'grayscale-pdf', name: 'Grayscale PDF', category: 'pdf', path: 'grayscale-pdf/index.html' },
    { slug: 'flatten-pdf', name: 'Flatten PDF', category: 'pdf', path: 'flatten-pdf/index.html' },
    { slug: 'edit-pdf-metadata', name: 'Edit PDF Metadata', category: 'pdf', path: 'edit-pdf-metadata/index.html' },
    { slug: 'extract-images-pdf', name: 'Extract Images', category: 'pdf', path: 'extract-images-pdf/index.html' },
    { slug: 'resize-pdf', name: 'Resize PDF', category: 'pdf', path: 'resize-pdf/index.html' },
    { slug: 'alternate-mix-pdf', name: 'Alternate & Mix', category: 'pdf', path: 'alternate-mix-pdf/index.html' },
    { slug: 'header-footer-pdf', name: 'Header & Footer', category: 'pdf', path: 'header-footer-pdf/index.html' },
    { slug: 'remove-annotations-pdf', name: 'Remove Annotations', category: 'pdf', path: 'remove-annotations-pdf/index.html' },
    { slug: 'deskew-pdf', name: 'Deskew PDF', category: 'pdf', path: 'deskew-pdf/index.html' },
    { slug: 'pdf-to-text', name: 'PDF to Text', category: 'convert', path: 'pdf-to-text/index.html' },
    { slug: 'resize-image', name: 'Resize Image', category: 'image', path: 'resize-image/index.html' },
    { slug: 'crop-image', name: 'Crop Image', category: 'image', path: 'crop-image/index.html' },
    { slug: 'compress-image', name: 'Compress Image', category: 'image', path: 'compress-image/index.html' },
    { slug: 'jpg-to-png', name: 'JPG to PNG', category: 'image', path: 'jpg-to-png/index.html' },
    { slug: 'png-to-jpg', name: 'PNG to JPG', category: 'image', path: 'png-to-jpg/index.html' },
    { slug: 'age-calculator', name: 'Age Calculator', category: 'calculator', path: 'age-calculator/index.html' },
    { slug: 'word-counter', name: 'Word Counter', category: 'calculator', path: 'word-counter/index.html' },
    { slug: 'percentage-calculator', name: 'Percentage Calculator', category: 'calculator', path: 'percentage-calculator/index.html' },
    { slug: 'gst-calculator', name: 'GST Calculator', category: 'calculator', path: 'gst-calculator/index.html' },
    { slug: 'loan-calculator', name: 'Loan Calculator', category: 'calculator', path: 'loan-calculator/index.html' },
    { slug: 'bmi-calculator', name: 'BMI Calculator', category: 'calculator', path: 'bmi-calculator/index.html' },
    { slug: 'date-calculator', name: 'Date Calculator', category: 'calculator', path: 'date-calculator/index.html' },
    { slug: 'currency-converter', name: 'Currency Converter', category: 'calculator', path: 'currency-converter/index.html' },
    { slug: 'password-generator', name: 'Password Generator', category: 'utility', path: 'password-generator/index.html' },
    { slug: 'qr-code-generator', name: 'QR Code Generator', category: 'utility', path: 'qr-code-generator/index.html' },
    { slug: 'color-picker', name: 'Color Picker', category: 'utility', path: 'color-picker/index.html' },
    { slug: 'json-formatter', name: 'JSON Formatter', category: 'utility', path: 'json-formatter/index.html' },
    { slug: 'email-validator', name: 'Email Validator', category: 'utility', path: 'email-validator/index.html' },
    { slug: 'csv-to-excel', name: 'CSV to Excel', category: 'utility', path: 'csv-to-excel/index.html' }
  ];

  const hubLinks = [
    { name: 'All Tools', href: toHref('all-tools.html') },
    { name: 'PDF Tools', href: toHref('pdf-tools/index.html') },
    { name: 'Image Tools', href: toHref('image-tools/index.html') },
    { name: 'Passport Photo', href: toHref('passport-photo.html') },
    { name: 'Calculator Tools', href: toHref('calculator-tools/index.html') },
    { name: 'Blog Guides', href: toHref('blog.html') }
  ];

  const featuredLinks = [
    'age-calculator',
    'word-counter',
    'percentage-calculator',
    'gst-calculator',
    'loan-calculator',
    'bmi-calculator',
    'currency-converter',
    'passport-photo',
    'merge-pdf',
    'compress-pdf',
    'split-pdf'
  ];

  const styleId = 'lp-related-hub-style';
  if (!document.getElementById(styleId)) {
    const style = document.createElement('style');
    style.id = styleId;
    style.textContent = [
      '.lp-related-hub{margin:3rem 0 0;padding:2rem;border:2px solid var(--border);border-radius:24px;background:linear-gradient(135deg,var(--card),var(--bg2));box-shadow:0 18px 40px rgba(0,0,0,0.06);}',
      '.lp-related-hub h2{margin:0 0 0.75rem;font-family:\'Fraunces\',serif;font-size:clamp(1.6rem,3vw,2.2rem);color:var(--text);}',
      '.lp-related-hub p{margin:0 0 1.2rem;color:var(--muted);line-height:1.75;font-size:1rem;max-width:820px;}',
      '.lp-related-hub-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem;}',
      '.lp-link-group{background:var(--card);border:1.5px solid var(--border);border-radius:18px;padding:1rem 1rem 1.1rem;}',
      '.lp-link-group-title{margin:0 0 0.85rem;font-size:0.76rem;font-weight:900;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);}',
      '.lp-related-hub-links{display:flex;flex-wrap:wrap;gap:0.65rem;}',
      '.lp-related-hub-links a{padding:0.72rem 0.95rem;border:2px solid var(--border);border-radius:999px;background:linear-gradient(180deg,var(--card),var(--bg2));color:var(--text);text-decoration:none;font-weight:700;transition:all .2s ease;box-shadow:0 4px 10px rgba(0,0,0,0.04);}',
      '.lp-related-hub-links a:hover{border-color:var(--red);color:var(--red);transform:translateY(-2px);box-shadow:0 10px 18px rgba(232,50,26,0.12);}',
      '@media(max-width:640px){.lp-related-hub{padding:1.35rem}.lp-related-hub-grid{grid-template-columns:1fr;}}'
    ].join('');
    document.head.appendChild(style);
  }

  if (document.querySelector('.lp-related-hub')) return;

  const currentSlug = parts[parts.length - 1] === 'index.html' ? parts[parts.length - 2] : parts[parts.length - 1];
  const current = catalog.find(function (item) {
    return item.slug === currentSlug;
  });

  const container = document.querySelector('.seo-long-content') ||
    document.querySelector('.seo-content') ||
    document.querySelector('.content-section') ||
    document.querySelector('.page-wrap');
  if (!container) return;

  const withHref = function (item) {
    return {
      slug: item.slug,
      name: item.name,
      category: item.category,
      href: toHref(item.path)
    };
  };

  const featuredToolLinks = featuredLinks
    .map(function (slug) {
      return catalog.find(function (item) {
        return item.slug === slug;
      });
    })
    .filter(Boolean)
    .filter(function (item) {
      return !current || item.slug !== current.slug;
    })
    .map(withHref);

  const peerLinks = current ? catalog
    .filter(function (item) {
      return item.slug !== current.slug && item.category === current.category;
    })
    .slice(0, 8)
    .map(withHref) : [];

  const supportLinks = catalog
    .filter(function (item) {
      return !current || item.slug !== current.slug;
    })
    .filter(function (item) {
      return !current || item.category !== current.category;
    })
    .slice(0, current ? 6 : 8)
    .map(withHref);

  const renderLinks = function (links) {
    return links.map(function (link) {
      return '<a href="' + link.href + '">' + link.name + '</a>';
    }).join('');
  };

  const section = document.createElement('section');
  section.className = 'lp-related-hub';
  section.innerHTML = `
    <h2>Explore More LovePDFs Tools</h2>
    <p>Keep moving through related tools without going back to the homepage. This helps visitors discover the rest of the toolkit and strengthens internal linking across the site.</p>
    <div class="lp-related-hub-grid">
      <div class="lp-link-group">
        <div class="lp-link-group-title">Start Here</div>
        <div class="lp-related-hub-links">
          ${hubLinks.map(function (link) { return '<a href="' + link.href + '">' + link.name + '</a>'; }).join('')}
        </div>
      </div>
      <div class="lp-link-group">
        <div class="lp-link-group-title">${current ? 'Related ' + (current.category === 'calculator' ? 'Calculators' : 'Tools') : 'Popular Picks'}</div>
        <div class="lp-related-hub-links">
          ${renderLinks(current ? peerLinks : featuredToolLinks.slice(0, 8))}
        </div>
      </div>
      <div class="lp-link-group">
        <div class="lp-link-group-title">Popular Picks</div>
        <div class="lp-related-hub-links">
          ${renderLinks(featuredToolLinks)}
        </div>
      </div>
      <div class="lp-link-group">
        <div class="lp-link-group-title">More to Explore</div>
        <div class="lp-related-hub-links">
          ${renderLinks(supportLinks)}
        </div>
      </div>
    </div>
  `;

  const footer = document.querySelector('.site-footer');
  if (footer && footer.parentNode) {
    footer.parentNode.insertBefore(section, footer);
  } else {
    container.appendChild(section);
  }
})();
