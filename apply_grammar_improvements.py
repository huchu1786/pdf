#!/usr/bin/env python3
"""
Apply grammar and style improvements to blog posts based on guidelines.
Targets repetitive phrases, improves sentence structure, and enhances readability.
"""

import os
import re
from pathlib import Path
import html

# Grammar and style improvement rules based on guidelines
IMPROVEMENT_RULES = [
    # Repetitive phrase replacements
    {
        'pattern': r"In today's digital landscape",
        'replacement': "In the modern digital environment",
        'description': "Replace overused phrase with variation"
    },
    {
        'pattern': r"absolute superpower",
        'replacement': "significant advantage",
        'description': "Replace casual term with professional alternative"
    },
    {
        'pattern': r"massive library of utilities",
        'replacement': "comprehensive toolset",
        'description': "Replace imprecise term with specific alternative"
    },
    {
        'pattern': r"gracefully cut down on tedious administrative friction",
        'replacement': "streamline administrative processes",
        'description': "Simplify verbose phrasing"
    },
    {
        'pattern': r"mysterious cloud server somewhere overseas",
        'replacement': "remote cloud servers",
        'description': "Remove sensational language"
    },
    {
        'pattern': r"fraction of a second",
        'replacement': "quickly",
        'description': "Simplify timing description"
    },
    {
        'pattern': r"Mastering your everyday digital files",
        'replacement': "Effectively managing your digital documents",
        'description': "More professional phrasing"
    },
    {
        'pattern': r"thoroughly utilizing completely free",
        'replacement': "using free",
        'description': "Remove redundant adverbs"
    },
    {
        'pattern': r"inherently secure browser-based platforms",
        'replacement': "secure browser-based tools",
        'description': "Simplify technical description"
    },
    {
        'pattern': r"We highly recommend you boldly start by heavily exploring",
        'replacement': "We recommend starting with",
        'description': "Remove excessive adverbs"
    },
    
    # Grammar improvements
    {
        'pattern': r"(\w+) which (is|are|was|were)",
        'replacement': r"\1, which \2",
        'description': "Add comma before 'which' for non-restrictive clauses"
    },
    {
        'pattern': r"(\w+) that (is|are|was|were) (?:a|an|the) (\w+) that",
        'replacement': r"\1 that \2 \3, which",
        'description': "Avoid double 'that' constructions"
    },
    
    # Sentence structure improvements
    {
        'pattern': r"\. However,",
        'replacement': ". However,",
        'description': "Ensure proper capitalization after period"
    },
    {
        'pattern': r"(\w+), and (\w+)",
        'replacement': r"\1 and \2",
        'description': "Remove unnecessary comma before 'and' in simple lists"
    },
    
    # Active voice encouragement (simple patterns)
    {
        'pattern': r"is (?:being|been) (used|processed|handled|managed) by",
        'replacement': r"uses",
        'description': "Convert passive to active voice"
    },
    {
        'pattern': r"can be (?:easily|quickly) (done|achieved|accomplished)",
        'replacement': r"is straightforward",
        'description': "Simplify passive constructions"
    },
    
    # Vocabulary enhancements
    {
        'pattern': r"very (\w+)",
        'replacement': r"\1",  # Remove "very" - let the adjective stand alone
        'description': "Remove weak intensifier"
    },
    {
        'pattern': r"really (\w+)",
        'replacement': r"\1",
        'description': "Remove casual intensifier"
    },
    {
        'pattern': r"a lot of",
        'replacement': "many",
        'description': "More formal alternative"
    },
    
    # Technical term standardization
    {
        'pattern': r"web-based (?:tool|application)",
        'replacement': "browser-based tool",
        'description': "Standardize terminology"
    },
    {
        'pattern': r"online (?:PDF|pdf) (?:tool|editor)",
        'replacement': "browser-based PDF tool",
        'description': "Standardize terminology"
    },
    
    # Readability improvements
    {
        'pattern': r"(\w{20,})",  # Very long words
        'replacement': None,  # Flag for review
        'description': "Flag potentially complex vocabulary"
    },
]

# Additional repetitive phrases from analysis
REPETITIVE_PHRASES = [
    "Navigating government websites like the EPF portal",
    "knowing the best hacks to manipulate, compress, and edit",
    "Modern workflows—whether you are working remotely from Pune",
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
    "In the past, compressing a PDF meant uploading",
    "Because there is strictly no server upload involved",
    "you immediately bypass annoying internet upload speed bottlenecks",
    "massive 100MB documents can be heavily processed",
    "Visit the homepage",
    "read more extensive tutorials on our central blog"
]

def extract_content_section(html_content):
    """Extract the main content section from blog post HTML."""
    # Find the blog-content div
    content_match = re.search(r'<div class="blog-content">(.*?)</div>\s*</div>\s*<div class="blog-footer">', 
                             html_content, re.DOTALL)
    if content_match:
        return content_match.group(1), content_match.start(1), content_match.end(1)
    
    # Alternative pattern
    content_match = re.search(r'<div class="blog-content">(.*?)</div>\s*<div class="blog-footer">', 
                             html_content, re.DOTALL)
    if content_match:
        return content_match.group(1), content_match.start(1), content_match.end(1)
    
    # If not found, return entire content
    return html_content, 0, len(html_content)

def improve_sentence_structure(text):
    """Apply sentence structure improvements."""
    improvements = []
    
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    improved_sentences = []
    
    for sentence in sentences:
        original_sentence = sentence
        
        # Check sentence length
        word_count = len(sentence.split())
        if word_count > 35:
            # Try to split long sentences
            if ', ' in sentence:
                parts = sentence.split(', ')
                if len(parts) > 2:
                    # Split into two sentences at logical point
                    mid_point = len(parts) // 2
                    sentence = ', '.join(parts[:mid_point]) + '. ' + ', '.join(parts[mid_point:])
                    improvements.append(f"Split long sentence ({word_count} words)")
        
        # Remove redundant phrases
        redundant_phrases = [
            (r"it is important to note that", ""),
            (r"it should be noted that", ""),
            (r"it is worth mentioning that", ""),
            (r"as a matter of fact", ""),
            (r"the fact of the matter is", ""),
        ]
        
        for pattern, replacement in redundant_phrases:
            if re.search(pattern, sentence, re.IGNORECASE):
                sentence = re.sub(pattern, replacement, sentence, flags=re.IGNORECASE)
                improvements.append("Removed redundant phrase")
        
        improved_sentences.append(sentence)
    
    improved_text = ' '.join(improved_sentences)
    return improved_text, improvements

def apply_grammar_rules(text):
    """Apply grammar improvement rules."""
    improvements = []
    improved_text = text
    
    for rule in IMPROVEMENT_RULES:
        pattern = rule['pattern']
        replacement = rule['replacement']
        
        if replacement is None:
            # Flag for review
            matches = re.findall(pattern, improved_text)
            if matches:
                improvements.append(f"Flagged for review: {rule['description']} - Found: {matches[0]}")
        else:
            # Apply replacement
            original = improved_text
            improved_text = re.sub(pattern, replacement, improved_text, flags=re.IGNORECASE)
            if original != improved_text:
                improvements.append(f"Applied: {rule['description']}")
    
    return improved_text, improvements

def check_repetitive_phrases(text):
    """Check for repetitive phrases."""
    found_phrases = []
    
    for phrase in REPETITIVE_PHRASES:
        if phrase.lower() in text.lower():
            found_phrases.append(phrase)
    
    return found_phrases

def improve_blog_post(filepath, dry_run=True):
    """Apply grammar and style improvements to a blog post."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    original_content = html_content
    
    # Extract content section
    content, start_idx, end_idx = extract_content_section(html_content)
    
    if not content:
        print(f"Warning: Could not extract content section from {filepath}")
        return {'file': os.path.basename(filepath), 'changes': 0, 'improvements': []}
    
    # Track all improvements
    all_improvements = []
    
    # Check for repetitive phrases
    repetitive_phrases = check_repetitive_phrases(content)
    if repetitive_phrases:
        all_improvements.append(f"Found {len(repetitive_phrases)} repetitive phrases")
    
    # Apply grammar rules
    improved_content, grammar_improvements = apply_grammar_rules(content)
    all_improvements.extend(grammar_improvements)
    
    # Improve sentence structure
    improved_content, structure_improvements = improve_sentence_structure(improved_content)
    all_improvements.extend(structure_improvements)
    
    # Count changes
    changes = 0
    if content != improved_content:
        changes = sum(1 for i in range(min(len(content), len(improved_content))) 
                     if content[i] != improved_content[i])
    
    # Apply changes if not dry run
    if not dry_run and changes > 0:
        # Reconstruct HTML with improved content
        new_html = html_content[:start_idx] + improved_content + html_content[end_idx:]
        
        # Create backup
        backup_path = f"backups/before_grammar/{os.path.basename(filepath)}"
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Write improved file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
    
    return {
        'file': os.path.basename(filepath),
        'changes': changes,
        'improvements': all_improvements[:10],  # Limit output
        'repetitive_phrases_found': len(repetitive_phrases),
        'repetitive_examples': repetitive_phrases[:3] if repetitive_phrases else []
    }

def main():
    """Main function to apply improvements to sample posts."""
    sample_posts = [
        'blog-posts/2026-03-15-how-to-merge-pdf-files-like-a-pro-in-2024.html',
        'blog-posts/2026-03-15-how-to-compress-a-pdf-without-losing-quality-complete-guide.html',
        'blog-posts/2026-03-16-convert-pdf-to-word-complete-guide-and-tutorial.html',
        'blog-posts/2026-03-16-protect-pdf-complete-guide-and-tutorial.html',
        'blog-posts/2026-03-15-best-free-pdf-tools-in-2026-complete-guide.html'
    ]
    
    print("=" * 80)
    print("GRAMMAR AND STYLE IMPROVEMENTS - 5 SAMPLE BLOG POSTS")
    print("=" * 80)
    print("Running in DRY RUN mode (no changes will be made)")
    print("Add --apply flag to actually apply improvements")
    print()
    
    dry_run = True
    if len(os.sys.argv) > 1 and os.sys.argv[1] == '--apply':
        dry_run = False
        print("APPLYING CHANGES (not a dry run)")
        print()
    
    all_results = []
    
    for post_path in sample_posts:
        if not os.path.exists(post_path):
            print(f"Warning: File not found - {post_path}")
            continue
        
        print(f"Processing: {os.path.basename(post_path)}")
        result = improve_blog_post(post_path, dry_run=dry_run)
        all_results.append(result)
        
        print(f"  Changes detected: {result['changes']}")
        print(f"  Repetitive phrases found: {result['repetitive_phrases_found']}")
        
        if result['repetitive_examples']:
            print(f"  Example repetitive phrases: {', '.join(result['repetitive_examples'][:2])}")
        
        if result['improvements']:
            print(f"  Improvements applied:")
            for imp in result['improvements'][:3]:  # Show first 3
                print(f"    - {imp}")
        
        print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    total_changes = sum(r['changes'] for r in all_results)
    total_repetitive = sum(r['repetitive_phrases_found'] for r in all_results)
    total_improvements = sum(len(r['improvements']) for r in all_results)
    
    print(f"Total changes needed: {total_changes}")
    print(f"Total repetitive phrases found: {total_repetitive}")
    print(f"Total improvements identified: {total_improvements}")
    
    if dry_run:
        print("\nTo apply these changes, run: python apply_grammar_improvements.py --apply")
        print("Backups will be saved to: backups/before_grammar/")
    else:
        print("\nChanges have been applied. Backups saved to: backups/before_grammar/")
    
    # Save report
    report_file = 'grammar_improvements_report.txt'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("Grammar and Style Improvements Report\n")
        f.write("=" * 60 + "\n\n")
        
        for result in all_results:
            f.write(f"File: {result['file']}\n")
            f.write(f"  Changes: {result['changes']}\n")
            f.write(f"  Repetitive phrases: {result['repetitive_phrases_found']}\n")
            
            if result['improvements']:
                f.write(f"  Improvements:\n")
                for imp in result['improvements']:
                    f.write(f"    - {imp}\n")
            
            f.write("\n")
    
    print(f"\nDetailed report saved to: {report_file}")
    
    return all_results

if __name__ == '__main__':
    main()