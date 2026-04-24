const fs = require('fs');
const path = require('path');
const toolPages = new Set([
  ...require('../tools-data.js').map((tool) => tool.id),
  'age-calculator',
  'word-counter',
  'percentage-calculator',
  'gst-calculator',
  'loan-calculator',
  'bmi-calculator',
  'date-calculator',
  'currency-converter',
  'password-generator',
  'qr-code-generator',
  'color-picker',
  'json-formatter',
  'email-validator',
  'csv-to-excel'
]);

const rootDir = path.resolve(__dirname, '..');
const skipDirs = new Set(['node_modules', '.git']);

function walk(dir, files = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (skipDirs.has(entry.name)) continue;
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(fullPath, files);
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      files.push(fullPath);
    }
  }
  return files;
}

function relLink(fromFile, targetFile) {
  return path.relative(path.dirname(fromFile), path.join(rootDir, targetFile)).replace(/\\/g, '/');
}

function isToolPage(filePath) {
  const rel = path.relative(rootDir, filePath).replace(/\\/g, '/');
  const match = rel.match(/^([^/]+)\/index\.html$/);
  return match ? toolPages.has(match[1]) : false;
}

function replaceFooterContact(html, contactHref) {
  return html.replace(
    /<div class="footer-contact">[\s\S]*?<\/div>/g,
    `<div class="footer-contact"><a href="${contactHref}">Contact us</a></div>`
  );
}

function replaceFooterCopy(html) {
  return html.replace(
    /<div class="footer-copy"([^>]*)>[\s\S]*?<\/div>/g,
    '<div class="footer-copy"$1>&copy; LovePDFs 2026 &reg; · Private & Local Processing</div>'
  );
}

function cleanupFile(filePath) {
  const contactHref = relLink(filePath, 'contact.html');
  const enhancementsHref = relLink(filePath, 'site-enhancements.js');
  let html = fs.readFileSync(filePath, 'utf8');
  const original = html;

  html = html.replace(/https:\/\/lovepdfs\.com/g, 'https://lovepdfs.in');
  html = html.replace(/"email":\s*"hello@lovepdfs\.in",?\s*/g, '');
  html = html.replace(/href="mailto:hello@lovepdfs\.in"/g, `href="${contactHref}"`);
  html = html.replace(/hello@lovepdfs\.in/g, 'our contact page');

  html = html.replace(
    /<a[^>]*class="nav-btn-o"[^>]*>[\s\S]*?<\/a>/g,
    `<a href="${contactHref}" class="nav-btn-o">Contact</a>`
  );

  html = html.replace(
    /<a[^>]*class="contact-email-btn"[^>]*>[\s\S]*?<\/a>/g,
    `<a href="${contactHref}" class="contact-email-btn">Contact Support</a>`
  );

  html = html.replace(
    /<div class="contact-strip">[\s\S]*?<a[^>]+href="[^"]+"[^>]*>[\s\S]*?<\/a>/g,
    (match) => match.replace(/<a[^>]+href="[^"]+"[^>]*>[\s\S]*?<\/a>/, `<a href="${contactHref}">Contact Support</a>`)
  );

  html = html.replace(
    /<p class="body-p">LovePDFs was built by an independent developer passionate about free, privacy-first tools\. Contact us at our contact page\.<\/p>/g,
    '<p class="body-p">LovePDFs was built by an independent developer passionate about free, privacy-first tools. Visit our contact page if you need support or want to share feedback.</p>'
  );

  html = replaceFooterContact(html, contactHref);
  html = replaceFooterCopy(html);

  if (isToolPage(filePath) && !html.includes('site-enhancements.js')) {
    html = html.replace('</body>', `\n<script src="${enhancementsHref}"></script>\n</body>`);
  }

  if (html !== original) {
    fs.writeFileSync(filePath, html, 'utf8');
  }
}

for (const filePath of walk(rootDir)) {
  cleanupFile(filePath);
}

console.log('Deployment cleanup complete.');
