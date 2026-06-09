const fs = require('fs');
const path = require('path');
const { TOOLS_SEO } = require('./tools-data.js');

const TEMPLATE_PATH = path.join(__dirname, 'template.html');
const DIST_DIR = __dirname; 

const MAJOR_TOOLS = new Set([
  'merge-pdf', 'compress-pdf', 'split-pdf', 'pdf-to-word', 'word-to-pdf',
  'sign-pdf', 'protect-pdf', 'unlock-pdf', 'jpg-to-pdf', 'pdf-to-jpg',
  'edit-pdf', 'compress-image', 'png-to-jpg', 'jpg-to-png', 'image-to-pdf',
  'pdf-to-text'
]);

function buildPages() {
  const templateRaw = fs.readFileSync(TEMPLATE_PATH, 'utf-8');
  const sitemapUrls = [];
  const origin = 'https://lovepdfs.in';
  
  // Add homepage to sitemap
  sitemapUrls.push(`${origin}/`);

  // Add 9 static pages
  const staticPages = [
    "about",
    "contact",
    "privacy",
    "terms",
    "security",
    "faq",
    "pricing",
    "features",
    "blog"
  ];
  staticPages.forEach(page => {
    sitemapUrls.push(`${origin}/${page}`);
  });

  // Add 4 blogs
  const blogs = [
    "blog-merge-pdfs",
    "blog-reduce-pdf-size",
    "blog-electronic-signatures",
    "blog-password-security"
  ];
  blogs.forEach(blog => {
    sitemapUrls.push(`${origin}/${blog}`);
  });

  TOOLS_SEO.forEach(t => {
    // 1. Prepare directory
    const pageDir = path.join(DIST_DIR, t.id);
    if (!fs.existsSync(pageDir)) {
      fs.mkdirSync(pageDir, { recursive: true });
    }
    
    // 2. Build Instructions HTML
    const instructionsHtml = t.instructions.map(inst => `<li>${inst}</li>`).join('\n    ');
    
    // 3. Build Benefits HTML
    const benefitsHtml = t.benefits.map(b => `
      <div class="benefit-card">
        <h4>${b.title}</h4>
        <p>${b.desc}</p>
      </div>`).join('');
      
    // 4. Build FAQ HTML
    const faqsHtml = t.faqs.map(f => `
      <div class="faq-item">
        <div class="faq-q">${f.q}</div>
        <p class="faq-a">${f.a}</p>
      </div>`).join('');
      
    // 5. Build Related HTML
    const relatedHtml = t.related.map(rid => {
      const relData = TOOLS_SEO.find(x => x.id === rid);
      return relData ? `<a href="../${rid}/" class="related-chip">${relData.h1}</a>` : '';
    }).join('');

    // Determine robots value based on whether tool is major
    const isMajor = MAJOR_TOOLS.has(t.id);
    const robotsVal = isMajor ? 'index, follow' : 'noindex, follow';

    // 6. Replace Tags in Template
    let html = templateRaw
      .replace('<meta name="robots" content="noindex, follow">', `<meta name="robots" content="${robotsVal}">`)
      .replace(/\{\{TOOL_ID\}\}/g, t.toolId)
      .replace(/\{\{TITLE\}\}/g, t.title)
      .replace(/\{\{META\}\}/g, t.meta)
      .replace(/\{\{H1\}\}/g, t.h1)
      .replace(/\{\{DESC\}\}/g, t.desc)
      .replace(/\{\{INSTRUCTIONS\}\}/g, instructionsHtml)
      .replace(/\{\{BENEFITS\}\}/g, benefitsHtml)
      .replace(/\{\{FAQS\}\}/g, faqsHtml)
      .replace(/\{\{RELATED\}\}/g, relatedHtml);
      
    // 7. Write index.html
    const outPath = path.join(pageDir, 'index.html');
    fs.writeFileSync(outPath, html);
    console.log(`✅ Generated /${t.id}/index.html with robots="${robotsVal}"`);
    
    // 8. Add to sitemap only if it is a major tool
    if (isMajor) {
      sitemapUrls.push(`${origin}/${t.id}/`);
    }
  });
  
  // Sort URLs for consistency
  sitemapUrls.sort((a, b) => {
    if (a === `${origin}/`) return -1;
    if (b === `${origin}/`) return 1;
    return a.localeCompare(b);
  });

  // 9. Generate Sitemap
  const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapUrls.map(url => `  <url>\n    <loc>${url}</loc>\n  </url>`).join('\n')}
</urlset>`;
  
  fs.writeFileSync(path.join(DIST_DIR, 'sitemap.xml'), sitemapXml);
  console.log(`🗺️ Generated sitemap.xml with ${sitemapUrls.length} URLs`);
  console.log('🎉 Build complete!');
}

buildPages();
