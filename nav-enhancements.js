(function () {
  const nav = document.getElementById('siteNav') || document.querySelector('.site-nav');
  if (!nav) return;

  // Determine relative path prefix
  let isInSubfolder = false;
  const currentScript = document.currentScript;
  if (currentScript) {
    const src = currentScript.getAttribute('src');
    if (src && src.indexOf('../') === 0) {
      isInSubfolder = true;
    }
  } else {
    // Fallback: check all script tags for relative path pattern
    const scripts = document.getElementsByTagName('script');
    for (let i = 0; i < scripts.length; i++) {
      const src = scripts[i].getAttribute('src');
      if (src && (src.indexOf('../nav-enhancements.js') >= 0 || src.indexOf('../site-enhancements.js') >= 0)) {
        isInSubfolder = true;
        break;
      }
    }
  }
  const p = isInSubfolder ? '../' : '';

  nav.innerHTML = `
    <!-- LOGO -->
    <a href="${p || 'index.html'}" class="nav-logo" aria-label="LovePDFs Home">
      I <span class="nav-logo-heart">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
      </span> PDFs
    </a>

    <!-- CENTER NAV -->
    <div class="nav-mid" id="navMid">
      <a href="${p}merge-pdf/index.html" class="nav-link ilv-link">Merge PDF</a>
      <a href="${p}split-pdf/index.html" class="nav-link ilv-link">Split PDF</a>
      <a href="${p}compress-pdf/index.html" class="nav-link ilv-link">Compress PDF</a>

      <!-- Convert PDF Dropdown -->
      <div class="ilv-dropdown" id="convertDropdown">
        <button class="ilv-dropdown-btn" type="button" aria-haspopup="true" aria-expanded="false">
          Convert PDF <svg class="ilv-caret" viewBox="0 0 10 6" width="10" height="6" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 1l4 4 4-4"/></svg>
        </button>
        <div class="ilv-dropdown-panel" role="menu">
          <ul class="ilv-col">
            <li class="ilv-group-title">Convert to PDF</li>
            <li><a href="${p}jpg-to-pdf/index.html" role="menuitem">JPG to PDF</a></li>
            <li><a href="${p}word-to-pdf/index.html" role="menuitem">Word to PDF</a></li>
            <li><a href="${p}ppt-to-pdf/index.html" role="menuitem">PowerPoint to PDF</a></li>
            <li><a href="${p}excel-to-pdf/index.html" role="menuitem">Excel to PDF</a></li>
            <li><a href="${p}html-to-pdf/index.html" role="menuitem">HTML to PDF</a></li>
            <li><a href="${p}image-to-pdf/index.html" role="menuitem">Image to PDF</a></li>
          </ul>
          <ul class="ilv-col">
            <li class="ilv-group-title">Convert from PDF</li>
            <li><a href="${p}pdf-to-jpg/index.html" role="menuitem">PDF to JPG</a></li>
            <li><a href="${p}pdf-to-word/index.html" role="menuitem">PDF to Word</a></li>
            <li><a href="${p}pdf-to-ppt/index.html" role="menuitem">PDF to PowerPoint</a></li>
            <li><a href="${p}pdf-to-excel/index.html" role="menuitem">PDF to Excel</a></li>
            <li><a href="${p}pdf-to-pdfa/index.html" role="menuitem">PDF to PDF/A</a></li>
          </ul>
        </div>
      </div>

      <!-- All PDF Tools Dropdown -->
      <div class="ilv-dropdown ilv-dropdown--full" id="allToolsDropdown">
        <button class="ilv-dropdown-btn" type="button" aria-haspopup="true" aria-expanded="false">
          All PDF Tools <svg class="ilv-caret" viewBox="0 0 10 6" width="10" height="6" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 1l4 4 4-4"/></svg>
        </button>
        <div class="ilv-dropdown-panel ilv-panel--wide" role="menu">
          <ul class="ilv-col">
            <li class="ilv-group-title">Organize PDF</li>
            <li><a href="${p}merge-pdf/index.html">Merge PDF</a></li>
            <li><a href="${p}split-pdf/index.html">Split PDF</a></li>
            <li><a href="${p}organize-pdf/index.html">Organize PDF</a></li>
            <li><a href="${p}remove-pages-pdf/index.html">Remove Pages</a></li>
            <li><a href="${p}extract-pages-pdf/index.html">Extract Pages</a></li>
            <li><a href="${p}rotate-pdf/index.html">Rotate PDF</a></li>
          </ul>
          <ul class="ilv-col">
            <li class="ilv-group-title">Optimize PDF</li>
            <li><a href="${p}compress-pdf/index.html">Compress PDF</a></li>
            <li><a href="${p}repair-pdf/index.html">Repair PDF</a></li>
            <li><a href="${p}ocr-extract-text/index.html">OCR PDF</a></li>
            <li class="ilv-group-title" style="margin-top:1rem">Edit PDF</li>
            <li><a href="${p}edit-pdf/index.html">Edit PDF</a></li>
            <li><a href="${p}add-watermark-pdf/index.html">Add Watermark</a></li>
            <li><a href="${p}add-page-numbers-pdf/index.html">Page Numbers</a></li>
            <li><a href="${p}crop-pdf/index.html">Crop PDF</a></li>
          </ul>
          <ul class="ilv-col">
            <li class="ilv-group-title">Convert to PDF</li>
            <li><a href="${p}jpg-to-pdf/index.html">JPG to PDF</a></li>
            <li><a href="${p}word-to-pdf/index.html">Word to PDF</a></li>
            <li><a href="${p}ppt-to-pdf/index.html">PowerPoint to PDF</a></li>
            <li><a href="${p}excel-to-pdf/index.html">Excel to PDF</a></li>
            <li><a href="${p}html-to-pdf/index.html">HTML to PDF</a></li>
            <li><a href="${p}image-to-pdf/index.html">Image to PDF</a></li>
          </ul>
          <ul class="ilv-col">
            <li class="ilv-group-title">Convert from PDF</li>
            <li><a href="${p}pdf-to-jpg/index.html">PDF to JPG</a></li>
            <li><a href="${p}pdf-to-word/index.html">PDF to Word</a></li>
            <li><a href="${p}pdf-to-ppt/index.html">PDF to PowerPoint</a></li>
            <li><a href="${p}pdf-to-excel/index.html">PDF to Excel</a></li>
            <li class="ilv-group-title" style="margin-top:1rem">PDF Security</li>
            <li><a href="${p}unlock-pdf/index.html">Unlock PDF</a></li>
            <li><a href="${p}protect-pdf/index.html">Protect PDF</a></li>
            <li><a href="${p}sign-pdf/index.html">Sign PDF</a></li>
          </ul>
          <ul class="ilv-col">
            <li class="ilv-group-title">Image Tools</li>
            <li><a href="${p}compress-image/index.html">Compress Image</a></li>
            <li><a href="${p}resize-image/index.html">Resize Image</a></li>
            <li><a href="${p}crop-image/index.html">Crop Image</a></li>
            <li><a href="${p}jpg-to-png/index.html">JPG to PNG</a></li>
            <li><a href="${p}png-to-jpg/index.html">PNG to JPG</a></li>
            <li><a href="${p}image-to-pdf/index.html">Image to PDF</a></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- RIGHT ACTIONS -->
    <div class="nav-right">
      <!-- Hamburger for mobile -->
      <button class="nav-hamburger" id="navHamburger" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  `;

  // ── Dropdown Logic ──
  nav.querySelectorAll('.ilv-dropdown').forEach(function (dd) {
    const btn = dd.querySelector('.ilv-dropdown-btn');
    const panel = dd.querySelector('.ilv-dropdown-panel');

    function closeDD() {
      dd.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    }
    function openDD() {
      // close siblings
      nav.querySelectorAll('.ilv-dropdown').forEach(function (o) {
        if (o !== dd) { o.classList.remove('open'); o.querySelector('.ilv-dropdown-btn').setAttribute('aria-expanded', 'false'); }
      });
      dd.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
    }

    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      dd.classList.contains('open') ? closeDD() : openDD();
    });

    // Hover on desktop
    dd.addEventListener('mouseenter', function () { if (window.innerWidth > 900) openDD(); });
    dd.addEventListener('mouseleave', function () { if (window.innerWidth > 900) closeDD(); });

    document.addEventListener('click', function (e) {
      if (!dd.contains(e.target)) closeDD();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeDD();
    });
  });

  // ── Mobile hamburger ──
  const hamburger = nav.querySelector('#navHamburger');
  const navMid = nav.querySelector('#navMid');
  let mobileOpen = false;

  if (hamburger && navMid) {
    hamburger.addEventListener('click', function (e) {
      e.stopPropagation();
      mobileOpen = !mobileOpen;
      navMid.classList.toggle('mobile-open', mobileOpen);
      hamburger.setAttribute('aria-expanded', String(mobileOpen));
    });

    document.addEventListener('click', function (e) {
      if (mobileOpen && !navMid.contains(e.target) && !hamburger.contains(e.target)) {
        mobileOpen = false;
        navMid.classList.remove('mobile-open');
        hamburger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // ── Active link highlighting ──
  const path = window.location.pathname.replace(/\/index\.html$/, '/');
  nav.querySelectorAll('a[href]').forEach(function (a) {
    const href = a.getAttribute('href').replace(/^\.\.\//, '/').replace(/index\.html$/, '');
    if (href !== '/' && href !== '' && path.includes(href.replace(/^\//, ''))) {
      a.classList.add('active');
    }
  });

})();
