import os
import re

footer_template = """<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <div class="footer-logo"><div class="nav-logo-heart">
      <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
    </div>
    love<span>pdfs</span></div>
      <div class="footer-tagline">Every PDF & Image tool you'll ever need — 100% free, private, running entirely in your browser.</div>
      <div class="footer-contact"><a href="{prefix}contact.html">Contact us</a></div>
      <div class="footer-badges"><span class="fbadge">🔒 SSL</span><span class="fbadge">⚡ WebAssembly</span><span class="fbadge">✦ Always Free</span></div>
    </div>
    <div><div class="footer-col-title">Product</div><div class="footer-links"><a href="{prefix}index.html">Home</a><a href="{prefix}features.html">Features</a><a href="{prefix}pricing.html">Pricing</a><a href="{prefix}all-tools.html">Tools</a><a href="{prefix}faq.html">FAQ</a></div></div>
    <div><div class="footer-col-title">Solutions</div><div class="footer-links"><a href="{prefix}business.html">Business</a><a href="{prefix}education.html">Education</a></div></div>
    <div><div class="footer-col-title">Legal</div><div class="footer-links"><a href="{prefix}security.html">Security</a><a href="{prefix}privacy.html">Privacy policy</a><a href="{prefix}terms.html">Terms & conditions</a><a href="{prefix}cookies.html">Cookies</a></div></div>
    <div><div class="footer-col-title">Company</div><div class="footer-links"><a href="{prefix}about.html">About us</a><a href="{prefix}contact.html">Contact us</a><a href="{prefix}blog.html">Blog</a><a href="{prefix}press.html">Press</a></div></div>
  </div>
  <div class="footer-bottom" style="max-width:1240px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem">
    <div class="footer-copy" style="font-size:0.8rem;color:var(--muted)">&copy; LovePDFs 2026 &reg; · Private & Local Processing</div>
    <div class="footer-sitemap"><a href="{prefix}sitemap.xml" style="color:var(--muted);font-size:0.82rem;text-decoration:none;transition:color 0.2s">Sitemap</a></div>
  </div>
</footer>"""

pattern = re.compile(r'<footer[^>]*>.*?</footer>', re.DOTALL)

for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.html'):
            filepath = os.path.join(root, filename)
            
            # Skip hidden dirs or node_modules or app folders if any
            norm_path = filepath.replace('\\', '/')
            if '/.' in norm_path or '/node_modules' in norm_path or '/backups' in norm_path or '/pdf_tools_app' in norm_path or '/quiz_app' in norm_path:
                continue

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine prefix: if in a subdirectory (e.g. ./merge-pdf/index.html), we need "../"
            rel_path = os.path.relpath(filepath, '.')
            rel_path_norm = rel_path.replace('\\', '/')
            depth = rel_path_norm.count('/')
            prefix = "../" * depth
            
            new_footer = footer_template.replace('{prefix}', prefix)
            
            if pattern.search(content):
                new_content = pattern.sub(new_footer, content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated footer in {filepath}")
            else:
                print(f"No footer found in {filepath}")
