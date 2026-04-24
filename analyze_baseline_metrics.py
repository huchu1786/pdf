#!/usr/bin/env python3
"""
Analyze baseline metrics for 5 sample blog posts before improvements.
Captures word count, readability, structure, and interlinking metrics.
"""

import os
import re
from pathlib import Path
import html

def count_words(text):
    """Count words in text content (excluding HTML tags)."""
    # Remove HTML tags
    text_no_html = re.sub(r'<[^>]+>', ' ', text)
    # Remove extra whitespace and count words
    words = text_no_html.split()
    return len(words)

def extract_content_section(html_content):
    """Extract the main content section from blog post HTML."""
    # Find the blog-content div
    content_match = re.search(r'<div class="blog-content">(.*?)</div>\s*</div>\s*<div class="blog-footer">', 
                             html_content, re.DOTALL)
    if content_match:
        return content_match.group(1)
    
    # Alternative pattern
    content_match = re.search(r'<div class="blog-content">(.*?)</div>\s*<div class="blog-footer">', 
                             html_content, re.DOTALL)
    if content_match:
        return content_match.group(1)
    
    # If not found, return everything between body tags (excluding nav/footer)
    body_match = re.search(r'<body>(.*?)</body>', html_content, re.DOTALL)
    if body_match:
        body_content = body_match.group(1)
        # Remove nav and footer sections
        body_content = re.sub(r'<nav.*?</nav>', '', body_content, flags=re.DOTALL)
        body_content = re.sub(r'<footer.*?</footer>', '', body_content, flags=re.DOTALL)
        return body_content
    
    return html_content

def count_internal_links(html_content):
    """Count internal links to lovepdfs.in domain."""
    # Find all anchor tags
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>', html_content)
    
    internal_count = 0
    internal_urls = []
    
    for link in links:
        if 'lovepdfs.in' in link or link.startswith('/') or link.startswith('../'):
            internal_count += 1
            internal_urls.append(link)
    
    return internal_count, internal_urls

def analyze_structure(html_content):
    """Analyze content structure against template."""
    sections_found = {
        'introduction': False,
        'tutorial': False,
        'examples': False,
        'faq': False,
        'interlinking': False,
        'cta': False
    }
    
    # Check for section indicators
    content_lower = html_content.lower()
    
    # Introduction check (first paragraph or h2 with intro words)
    if re.search(r'<h2[^>]*>.*introduction.*</h2>', content_lower) or \
       re.search(r'<p>[^<]{100,}.*(pdf|tool|guide|tutorial).*</p>', content_lower[:2000]):
        sections_found['introduction'] = True
    
    # Tutorial check (step-by-step, how to)
    if re.search(r'<h2[^>]*>.*(step|tutorial|guide|how to).*</h2>', content_lower) or \
       re.search(r'<ol>.*<li>', content_lower, re.DOTALL):
        sections_found['tutorial'] = True
    
    # Examples check
    if re.search(r'<h2[^>]*>.*(example|use case|scenario).*</h2>', content_lower) or \
       re.search(r'<h3>.*example.*</h3>', content_lower):
        sections_found['examples'] = True
    
    # FAQ check
    if re.search(r'<h2[^>]*>.*(faq|question|answer).*</h2>', content_lower) or \
       re.search(r'<h3>.*q:.*</h3>', content_lower):
        sections_found['faq'] = True
    
    # Interlinking check (related tools section)
    if re.search(r'<div class="interlink', content_lower) or \
       re.search(r'<h2[^>]*>.*(related|also|try).*</h2>', content_lower):
        sections_found['interlinking'] = True
    
    # CTA check
    if re.search(r'<a[^>]+class="[^"]*(btn|button|cta)[^"]*"[^>]*>.*try.*</a>', content_lower) or \
       re.search(r'ready to.*<a', content_lower):
        sections_found['cta'] = True
    
    return sections_found

def calculate_readability(text):
    """Simple readability estimation based on average sentence length."""
    # Remove HTML tags
    text_no_html = re.sub(r'<[^>]+>', ' ', text)
    
    # Count sentences (periods, question marks, exclamation marks)
    sentences = re.split(r'[.!?]+', text_no_html)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if not sentences:
        return 0
    
    # Count words in each sentence
    word_counts = [len(s.split()) for s in sentences]
    
    # Average sentence length
    avg_sentence_length = sum(word_counts) / len(word_counts)
    
    # Simple readability score (lower = more readable)
    # Grade level approximation: (avg_sentence_length * 0.4) + 12
    grade_level = (avg_sentence_length * 0.4) + 12
    
    return round(grade_level, 1)

def analyze_blog_post(filepath):
    """Analyze a single blog post file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract content section
    content = extract_content_section(html_content)
    
    # Calculate metrics
    word_count = count_words(content)
    readability_score = calculate_readability(content)
    internal_link_count, internal_urls = count_internal_links(content)
    structure = analyze_structure(content)
    
    # Count examples (h3 with "example" or specific patterns)
    example_count = len(re.findall(r'<h3>.*example.*</h3>', content.lower()))
    
    # File size
    file_size_kb = os.path.getsize(filepath) / 1024
    
    return {
        'filename': os.path.basename(filepath),
        'word_count': word_count,
        'readability_score': readability_score,
        'internal_links': internal_link_count,
        'example_count': example_count,
        'file_size_kb': round(file_size_kb, 1),
        'structure': structure,
        'internal_urls': internal_urls[:5]  # First 5 URLs
    }

def main():
    """Main analysis function for 5 sample posts."""
    sample_posts = [
        'blog-posts/2026-03-15-how-to-merge-pdf-files-like-a-pro-in-2024.html',
        'blog-posts/2026-03-15-how-to-compress-a-pdf-without-losing-quality-complete-guide.html',
        'blog-posts/2026-03-16-convert-pdf-to-word-complete-guide-and-tutorial.html',
        'blog-posts/2026-03-16-protect-pdf-complete-guide-and-tutorial.html',
        'blog-posts/2026-03-15-best-free-pdf-tools-in-2026-complete-guide.html'
    ]
    
    print("=" * 80)
    print("BASELINE METRICS ANALYSIS - 5 SAMPLE BLOG POSTS")
    print("=" * 80)
    
    all_metrics = []
    
    for post_path in sample_posts:
        if not os.path.exists(post_path):
            print(f"Warning: File not found - {post_path}")
            continue
        
        print(f"\nAnalyzing: {os.path.basename(post_path)}")
        metrics = analyze_blog_post(post_path)
        all_metrics.append(metrics)
        
        print(f"  Word Count: {metrics['word_count']}")
        print(f"  Readability (Grade Level): {metrics['readability_score']}")
        print(f"  Internal Links: {metrics['internal_links']}")
        print(f"  Examples Found: {metrics['example_count']}")
        print(f"  File Size: {metrics['file_size_kb']} KB")
        
        # Structure analysis
        structure = metrics['structure']
        sections_present = [section for section, present in structure.items() if present]
        print(f"  Sections Present: {', '.join(sections_present) if sections_present else 'None identified'}")
        
        # Show sample internal links
        if metrics['internal_urls']:
            print(f"  Sample Internal Links: {', '.join(metrics['internal_urls'][:3])}")
    
    # Summary statistics
    print("\n" + "=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)
    
    if all_metrics:
        avg_word_count = sum(m['word_count'] for m in all_metrics) / len(all_metrics)
        avg_readability = sum(m['readability_score'] for m in all_metrics) / len(all_metrics)
        avg_links = sum(m['internal_links'] for m in all_metrics) / len(all_metrics)
        avg_examples = sum(m['example_count'] for m in all_metrics) / len(all_metrics)
        
        print(f"Average Word Count: {avg_word_count:.0f}")
        print(f"Average Readability (Grade Level): {avg_readability:.1f}")
        print(f"Average Internal Links: {avg_links:.1f}")
        print(f"Average Examples: {avg_examples:.1f}")
        
        # Structure compliance
        structure_counts = {section: 0 for section in all_metrics[0]['structure'].keys()}
        for metrics in all_metrics:
            for section, present in metrics['structure'].items():
                if present:
                    structure_counts[section] += 1
        
        print("\nStructure Compliance (% of posts with section):")
        for section, count in structure_counts.items():
            percentage = (count / len(all_metrics)) * 100
            print(f"  {section.capitalize()}: {count}/{len(all_metrics)} ({percentage:.0f}%)")
    
    # Save results to file
    output_file = 'baseline_metrics_report.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Baseline Metrics Report - 5 Sample Blog Posts\n")
        f.write("=" * 60 + "\n\n")
        
        for metrics in all_metrics:
            f.write(f"File: {metrics['filename']}\n")
            f.write(f"  Word Count: {metrics['word_count']}\n")
            f.write(f"  Readability: {metrics['readability_score']}\n")
            f.write(f"  Internal Links: {metrics['internal_links']}\n")
            f.write(f"  Examples: {metrics['example_count']}\n")
            f.write(f"  File Size: {metrics['file_size_kb']} KB\n")
            
            sections_present = [s for s, p in metrics['structure'].items() if p]
            f.write(f"  Sections: {', '.join(sections_present)}\n")
            f.write("\n")
    
    print(f"\nDetailed report saved to: {output_file}")
    
    return all_metrics

if __name__ == '__main__':
    main()