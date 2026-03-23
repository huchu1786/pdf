import sys
sys.path.insert(0, '.')
from create_interlink_sections import detect_blog_topic, generate_interlink_section

filename = '2026-03-15-how-to-merge-pdf-files-like-a-pro-in-2024.html'
topic = detect_blog_topic(filename)
print(f"Topic for {filename}: {topic}")
html = generate_interlink_section(topic)
print("\nGenerated HTML:")
print(html)