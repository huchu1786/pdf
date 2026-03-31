import os
import re

TARGET_POSTS = [
    'blog-posts/2026-03-15-how-to-merge-pdf-files-like-a-pro-in-2024.html',
    'blog-posts/2026-03-15-how-to-compress-a-pdf-without-losing-quality-complete-guide.html',
    'blog-posts/2026-03-16-convert-pdf-to-word-complete-guide-and-tutorial.html',
    'blog-posts/2026-03-16-protect-pdf-complete-guide-and-tutorial.html',
    'blog-posts/2026-03-15-best-free-pdf-tools-in-2026-complete-guide.html'
]

REPETITIVE_PHRASES = [
    "Navigating government websites like the EPF portal",
    "In today's digital landscape",
    "absolute superpower",
    "Modern workflows—whether you are working remotely from Pune",
    "knowing the best hacks to manipulate, compress, and edit",
    "filing extensive income tax returns",
    "scrambling to upload college assignments",
    "midnight portal deadline",
    "Whether you are uploading forms to DigiLocker",
    "applying for UPSC exams online",
    "The Portable Document Format (PDF) remains the gold standard",
    "Instead of downloading massive software suites like Adobe Acrobat",
    "Everything happens entirely within your web browser",
    "This means absolutely no processing is done on external servers",
    "This represents a massive shift in how we handle data securely",
    "mysterious cloud server somewhere overseas",
    "massive library of utilities"
]

INTERLINK_MAP = {
    'merge': [
        '<a href="../split-pdf/index.html">Split PDF</a>',
        '<a href="../compress-pdf/index.html">Compress PDF</a>',
        '<a href="../organize-pdf/index.html">Organize PDF</a>'
    ],
    'compress': [
        '<a href="../resize-image/index.html">Resize PDF</a>',
        '<a href="../split-pdf/index.html">Split PDF</a>',
    ],
    'word': [
        '<a href="../word-to-pdf/index.html">Word to PDF</a>',
        '<a href="../pdf-to-excel/index.html">PDF to Excel</a>',
        '<a href="../edit-pdf/index.html">Edit PDF</a>'
    ],
    'protect': [
        '<a href="../unlock-pdf/index.html">Unlock PDF</a>',
        '<a href="../sign-pdf/index.html">Sign PDF</a>',
        '<a href="../redact-pdf/index.html">Redact PDF</a>'
    ],
    'best-free': [
        '<a href="../merge-pdf/index.html">Merge PDF</a>',
        '<a href="../split-pdf/index.html">Split PDF</a>',
        '<a href="../compress-pdf/index.html">Compress PDF</a>'
    ]
}

def enhance_blog(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (Not Found)")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Repetitive Phrases
    for phrase in REPETITIVE_PHRASES:
        content = content.replace(phrase, "")

    # Inject Interlinks at the end of content
    topic_key = ""
    if 'merge' in filepath: topic_key = "merge"
    elif 'compress' in filepath: topic_key = "compress"
    elif 'word' in filepath: topic_key = "word"
    elif 'protect' in filepath: topic_key = "protect"
    elif 'best-free' in filepath: topic_key = "best-free"

    if topic_key and '<div class="related-posts">' not in content:
        links = INTERLINK_MAP.get(topic_key, [])
        link_html = " ".join([f'<li>{l}</li>' for l in links])
        
        related_section = f'''
        <div class="related-posts" style="margin-top: 2rem; background: var(--bg2); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--border);">
            <h3 style="margin-top: 0">Recommended Next Steps</h3>
            <ul>
                {link_html}
            </ul>
        </div>
        '''
        
        # Insert before the end of article/blog-content
        if '</div>\n            <div class="blog-footer">' in content:
            content = content.replace('</div>\n            <div class="blog-footer">', f'{related_section}</div>\n            <div class="blog-footer">')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"✓ Enhanced: {filepath}")

def main():
    print("Starting Phase 1 Blog Enhancements...")
    for post in TARGET_POSTS:
        enhance_blog(post)
    print("Optimization Complete.")

if __name__ == '__main__':
    main()
