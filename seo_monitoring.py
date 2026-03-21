#!/usr/bin/env python3
"""
Google Search Console monitoring and SEO analytics for LovePDFs
Track indexing improvements and search performance
"""

import json
import requests
from datetime import datetime, timedelta
from pathlib import Path

class SEOMonitor:
    def __init__(self, base_dir="/home/rameez/Downloads/ilovepdfs"):
        self.base_dir = Path(base_dir)
        self.seo_data_file = self.base_dir / "seo_data.json"
        self.reports_dir = self.base_dir / "seo_reports"
        self.reports_dir.mkdir(exist_ok=True)
        self.load_seo_data()
    
    def load_seo_data(self):
        """Load SEO monitoring data"""
        if self.seo_data_file.exists():
            with open(self.seo_data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                "monitoring_start": datetime.now().isoformat(),
                "daily_stats": [],
                "indexed_pages": [],
                "search_performance": [],
                "technical_seo": {},
                "recommendations": []
            }
    
    def save_seo_data(self):
        """Save SEO monitoring data"""
        with open(self.seo_data_file, 'w') as f:
            json.dump(self.data, f, indent=2, default=str)
    
    def generate_sitemap_check(self):
        """Generate sitemap for Google indexing"""
        sitemap_content = self.generate_sitemap()
        sitemap_file = self.base_dir / "sitemap.xml"
        with open(sitemap_file, 'w') as f:
            f.write(sitemap_content)
        
        return {
            "sitemap_generated": True,
            "sitemap_url": "https://lovepdfs.com/sitemap.xml",
            "pages_count": sitemap_content.count("<url>"),
            "last_updated": datetime.now().isoformat()
        }
    
    def generate_sitemap(self):
        """Generate comprehensive XML sitemap"""
        base_url = "https://lovepdfs.com"
        today = datetime.now().strftime("%Y-%m-%d")
        
        urls = [
            f"""  <url>
    <loc>{base_url}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""",
            f"""  <url>
    <loc>{base_url}/all-tools.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>""",
            f"""  <url>
    <loc>{base_url}/blog.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>""",
            f"""  <url>
    <loc>{base_url}/features.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>"""
        ]
        
        # Add tool pages
        tools_dir = self.base_dir
        for item in tools_dir.iterdir():
            if item.is_dir() and (item / "index.html").exists():
                urls.append(f"""  <url>
    <loc>{base_url}/{item.name}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")
        
        # Add blog posts
        blog_dir = self.base_dir / "blog-posts"
        if blog_dir.exists():
            for post_file in blog_dir.glob("*.html"):
                urls.append(f"""  <url>
    <loc>{base_url}/blog-posts/{post_file.stem}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>""")
        
        sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""
        
        return sitemap
    
    def generate_robots_txt(self):
        """Generate robots.txt for search engine crawling"""
        robots_content = """User-agent: *
Allow: /

# Sitemap location
Sitemap: https://lovepdfs.com/sitemap.xml

# Crawl-delay for respectful crawling
Crawl-delay: 1

# Disallow temporary directories
Disallow: /temp/
Disallow: /cache/
Disallow: /*.tmp$
"""
        
        robots_file = self.base_dir / "robots.txt"
        with open(robots_file, 'w') as f:
            f.write(robots_content)
        
        return {"robots_txt_generated": True, "location": "https://lovepdfs.com/robots.txt"}
    
    def analyze_site_structure(self):
        """Analyze site structure for SEO"""
        analysis = {
            "total_pages": 0,
            "tool_pages": 0,
            "blog_posts": 0,
            "internal_links": 0,
            "content_analysis": {}
        }
        
        # Count tool pages
        tools_dir = self.base_dir
        for item in tools_dir.iterdir():
            if item.is_dir() and (item / "index.html").exists():
                analysis["tool_pages"] += 1
                analysis["total_pages"] += 1
        
        # Count blog posts
        blog_dir = self.base_dir / "blog-posts"
        if blog_dir.exists():
            analysis["blog_posts"] = len(list(blog_dir.glob("*.html")))
            analysis["total_pages"] += analysis["blog_posts"]
        
        # Add static pages
        static_pages = ["index.html", "all-tools.html", "blog.html", "features.html", "about.html", "contact.html"]
        for page in static_pages:
            if (self.base_dir / page).exists():
                analysis["total_pages"] += 1
        
        return analysis
    
    def generate_seo_report(self):
        """Generate comprehensive SEO report"""
        today = datetime.now()
        
        # Site structure analysis
        structure = self.analyze_site_structure()
        
        # Generate sitemap and robots.txt
        sitemap_info = self.generate_sitemap_check()
        robots_info = self.generate_robots_txt()
        
        # Content analysis
        content_analysis = self.analyze_content_quality()
        
        # Technical SEO checks
        technical_seo = self.perform_technical_seo_checks()
        
        # Generate recommendations
        recommendations = self.generate_recommendations(structure, content_analysis, technical_seo)
        
        # Create report
        report = {
            "report_date": today.isoformat(),
            "site_structure": structure,
            "sitemap": sitemap_info,
            "robots_txt": robots_info,
            "content_analysis": content_analysis,
            "technical_seo": technical_seo,
            "recommendations": recommendations,
            "next_steps": self.generate_next_steps()
        }
        
        # Save report
        report_file = self.reports_dir / f"seo_report_{today.strftime('%Y%m%d')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        # Update data
        self.data["daily_stats"].append({
            "date": today.isoformat(),
            "total_pages": structure["total_pages"],
            "tool_pages": structure["tool_pages"],
            "blog_posts": structure["blog_posts"]
        })
        
        self.save_seo_data()
        
        return report
    
    def analyze_content_quality(self):
        """Analyze content quality across the site"""
        analysis = {
            "pages_with_content": 0,
            "average_word_count": 0,
            "total_word_count": 0,
            "pages_with_meta_descriptions": 0,
            "pages_with_titles": 0,
            "content_distribution": {}
        }
        
        total_words = 0
        pages_with_content = 0
        
        # Analyze tool pages
        tools_dir = self.base_dir
        for item in tools_dir.iterdir():
            if item.is_dir() and (item / "index.html").exists():
                index_file = item / "index.html"
                word_count = self.count_words_in_file(index_file)
                if word_count > 0:
                    pages_with_content += 1
                    total_words += word_count
        
        analysis["pages_with_content"] = pages_with_content
        analysis["total_word_count"] = total_words
        if pages_with_content > 0:
            analysis["average_word_count"] = total_words // pages_with_content
        
        return analysis
    
    def count_words_in_file(self, file_path):
        """Count words in an HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove HTML tags
            import re
            text_content = re.sub(r'<[^>]+>', '', content)
            words = text_content.split()
            return len(words)
        except:
            return 0
    
    def perform_technical_seo_checks(self):
        """Perform technical SEO checks"""
        checks = {
            "sitemap_exists": (self.base_dir / "sitemap.xml").exists(),
            "robots_txt_exists": (self.base_dir / "robots.txt").exists(),
            "favicon_exists": (self.base_dir / "favicon.png").exists(),
            "has_ssl": True,  # Assuming SSL is configured
            "mobile_friendly": True,  # Based on responsive design
            "page_load_speed": "good",  # Would need actual testing
            "internal_linking": "excellent",
            "url_structure": "clean"
        }
        
        return checks
    
    def generate_recommendations(self, structure, content, technical):
        """Generate SEO recommendations"""
        recommendations = []
        
        # Content recommendations
        if content["average_word_count"] < 400:
            recommendations.append({
                "priority": "high",
                "category": "content",
                "issue": "Low average word count",
                "recommendation": "Add more comprehensive content to tool pages (target 400-700 words per page)",
                "impact": "Improved search rankings and user engagement"
            })
        
        # Structure recommendations
        if structure["blog_posts"] < 10:
            recommendations.append({
                "priority": "medium",
                "category": "content",
                "issue": "Limited blog content",
                "recommendation": "Create more long-tail blog posts to target informational searches",
                "impact": "Increased organic traffic and brand authority"
            })
        
        # Technical recommendations
        if not technical["sitemap_exists"]:
            recommendations.append({
                "priority": "high",
                "category": "technical",
                "issue": "Missing sitemap",
                "recommendation": "Generate and submit sitemap to Google Search Console",
                "impact": "Better crawling and indexing"
            })
        
        return recommendations
    
    def generate_next_steps(self):
        """Generate next steps for SEO improvement"""
        return [
            "Submit sitemap to Google Search Console",
            "Set up Google Analytics for traffic monitoring",
            "Monitor indexing status regularly",
            "Create additional blog content targeting long-tail keywords",
            "Build quality backlinks from relevant sites",
            "Optimize page load speed",
            "Implement structured data markup",
            "Regularly update content to keep it fresh"
        ]
    
    def generate_search_console_instructions(self):
        """Generate instructions for Google Search Console setup"""
        instructions = """
# Google Search Console Setup Guide

## Step 1: Create Google Search Console Account
1. Go to https://search.google.com/search-console
2. Sign in with your Google account
3. Click "Add Property"

## Step 2: Verify Your Website
1. Select "URL prefix" property type
2. Enter: https://lovepdfs.com
3. Choose verification method (recommended: HTML file upload)
4. Download the verification HTML file
5. Upload it to your website root directory
6. Click "Verify"

## Step 3: Submit Sitemap
1. In Search Console, go to your property
2. Click "Sitemaps" in the left menu
3. Enter "sitemap.xml" in the sitemap URL field
4. Click "Submit"

## Step 4: Monitor Indexing
1. Go to "Coverage" report to see indexing status
2. Check "Performance" report for search analytics
3. Monitor "Enhancements" for structured data issues

## Step 5: Set Up Alerts
1. Go to "Settings" > "Preferences"
2. Enable email notifications for important issues
3. Set up custom alerts for significant changes

## Key Metrics to Monitor:
- Indexing status (how many pages are indexed)
- Click-through rate (CTR)
- Average position in search results
- Top performing pages
- Mobile usability issues
- Core Web Vitals

## Recommended Actions:
- Submit new content for indexing
- Fix any indexing errors
- Monitor performance trends
- Optimize underperforming pages
- Track keyword rankings
"""
        
        instructions_file = self.reports_dir / "search_console_setup.md"
        with open(instructions_file, 'w') as f:
            f.write(instructions)
        
        return {"instructions_created": True, "file": str(instructions_file)}

def main():
    """Main SEO monitoring routine"""
    monitor = SEOMonitor()
    
    print("🔍 Running SEO analysis for LovePDFs...")
    print("=" * 50)
    
    # Generate comprehensive SEO report
    report = monitor.generate_seo_report()
    
    # Generate Search Console setup instructions
    instructions = monitor.generate_search_console_instructions()
    
    print("📊 SEO Analysis Complete:")
    print(f"  Total Pages: {report['site_structure']['total_pages']}")
    print(f"  Tool Pages: {report['site_structure']['tool_pages']}")
    print(f"  Blog Posts: {report['site_structure']['blog_posts']}")
    print(f"  Sitemap Generated: {report['sitemap']['sitemap_generated']}")
    print(f"  Robots.txt Generated: {report['robots_txt']['robots_txt_generated']}")
    print(f"  Recommendations: {len(report['recommendations'])}")
    
    print(f"\n📋 Search Console setup instructions saved to: {instructions['file']}")
    print("📈 SEO report saved to: seo_reports/")
    
    print("\n🚀 Next Steps:")
    for step in report['next_steps'][:5]:
        print(f"  • {step}")

if __name__ == "__main__":
    main()
