#!/usr/bin/env python3
"""
Automated maintenance scheduler for LovePDFs website
Run this script regularly to maintain and enhance your site
"""

import os
import subprocess
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

class MaintenanceScheduler:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.log_file = self.base_dir / "maintenance_log.json"
        self.load_maintenance_log()
    
    def load_maintenance_log(self):
        """Load maintenance history"""
        if self.log_file.exists():
            with open(self.log_file, 'r', encoding='utf-8') as f:
                self.log = json.load(f)
        else:
            self.log = {
                "last_run": None,
                "tasks_completed": [],
                "errors": [],
                "stats": {
                    "tools_generated": 0,
                    "pages_enhanced": 0,
                    "blogs_created": 0,
                    "internal_links_added": 0
                }
            }
    
    def save_maintenance_log(self):
        """Save maintenance history"""
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(self.log, f, indent=2, default=str)
    
    def log_task(self, task_name, success=True, details=""):
        """Log a maintenance task"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "task": task_name,
            "success": success,
            "details": details
        }
        
        if success:
            self.log["tasks_completed"].append(entry)
        else:
            self.log["errors"].append(entry)
        
        self.log["last_run"] = datetime.now().isoformat()
    
    def run_script(self, script_name, description):
        """Run a maintenance script and log results"""
        print(f"[RUN] Running: {description}")
        try:
            result = subprocess.run(
                [sys.executable, script_name],
                cwd=self.base_dir,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                print(f"[SUCCESS] Success: {description}")
                self.log_task(script_name, True, result.stdout)
                return True
            else:
                print(f"[ERROR] Error: {description}")
                print(f"Error output: {result.stderr}")
                self.log_task(script_name, False, result.stderr)
                return False
                
        except subprocess.TimeoutExpired:
            print(f"[TIMEOUT] Timeout: {description}")
            self.log_task(script_name, False, "Script timed out after 5 minutes")
            return False
        except Exception as e:
            print(f"[EXCEPTION] Exception: {description} - {e}")
            self.log_task(script_name, False, str(e))
            return False
    
    def check_and_generate_missing_tools(self):
        """Generate any missing tool pages"""
        return self.run_script(
            "generate_tool_pages_fixed.py",
            "Generate missing tool pages"
        )
    
    def enhance_internal_links(self):
        """Enhance internal linking on tool pages"""
        return self.run_script(
            "enhance_internal_links.py",
            "Enhance internal linking"
        )
    
    def add_content_to_tools(self):
        """Add comprehensive content to tool pages"""
        return self.run_script(
            "enhance_tool_content.py",
            "Add comprehensive content to tools"
        )
    
    def create_daily_blog_post(self):
        """Create a new blog post (disabled for AdSense compliance)"""
        print("[INFO] Programmatic blog creation is disabled to comply with Google AdSense quality guidelines.")
        return True
    
    def update_sitemap(self):
        """Update sitemap with latest pages"""
        sitemap_content = self.generate_sitemap()
        sitemap_file = self.base_dir / "sitemap.xml"
        with open(sitemap_file, 'w', encoding='utf-8') as f:
            f.write(sitemap_content)
        print("[SUCCESS] Updated sitemap.xml")
        return True
    
    def generate_sitemap(self):
        """Generate XML sitemap including only the 30 authorized indexable pages"""
        base_url = "https://lovepdfs.in"
        existing_urls = set()
        existing_urls.add(base_url + "/")
                    
        # 2. Add authorized static informational pages (9 pages)
        static_pages = [
            "about",
            "contact",
            "privacy",
            "terms",
            "security",
            "faq",
            "pricing",
            "features",
            "blog"
        ]
        for page in static_pages:
            existing_urls.add(f"{base_url}/{page}")
            
        # 3. Add 16 major tools (only if index.html exists and has index robots tag)
        MAJOR_TOOLS = {
            'merge-pdf', 'compress-pdf', 'split-pdf', 'pdf-to-word', 'word-to-pdf',
            'sign-pdf', 'protect-pdf', 'unlock-pdf', 'jpg-to-pdf', 'pdf-to-jpg',
            'edit-pdf', 'compress-image', 'png-to-jpg', 'jpg-to-png', 'image-to-pdf',
            'pdf-to-text'
        }
        for tool_name in MAJOR_TOOLS:
            tool_dir = self.base_dir / tool_name
            index_file = tool_dir / "index.html"
            if index_file.exists():
                # Let's verify it is set to index
                with open(index_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                if 'content="index, follow"' in content:
                    existing_urls.add(f"{base_url}/{tool_name}/")
            
        # 4. Add the 4 indexable blog posts
        INDEXABLE_BLOG_SLUGS = {
            'merge-pdfs', 'reduce-pdf-size', 'electronic-signatures', 'password-security'
        }
        for slug in INDEXABLE_BLOG_SLUGS:
            blog_file = self.base_dir / f"blog-{slug}.html"
            if blog_file.exists():
                # Verify robots tag is index, follow
                with open(blog_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                if 'content="index, follow"' in content:
                    existing_urls.add(f"{base_url}/blog-{slug}")
                
        sorted_urls = list(existing_urls)
        def sort_key(url):
            if url == base_url + "/":
                return ""
            return url
        sorted_urls.sort(key=sort_key)
        
        xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for url in sorted_urls:
            xml_content += f'  <url>\n    <loc>{url}</loc>\n  </url>\n'
        xml_content += '</urlset>'
        
        return xml_content

    
    def generate_maintenance_report(self):
        """Generate a maintenance report"""
        report = f"""
# LovePDFs Maintenance Report
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- **Last Run:** {self.log.get('last_run', 'Never')}
- **Tasks Completed:** {len(self.log['tasks_completed'])}
- **Errors:** {len(self.log['errors'])}

## Statistics
- **Tools Generated:** {self.log['stats']['tools_generated']}
- **Pages Enhanced:** {self.log['stats']['pages_enhanced']}
- **Blogs Created:** {self.log['stats']['blogs_created']}
- **Internal Links Added:** {self.log['stats']['internal_links_added']}

## Recent Tasks
"""
        
        for task in self.log['tasks_completed'][-5:]:
            report += f"- {task['timestamp']}: {task['task']} ✅\n"
        
        if self.log['errors']:
            report += "\n## Recent Errors\n"
            for error in self.log['errors'][-3:]:
                report += f"- {error['timestamp']}: {error['task']} ❌\n"
        
        return report
    
    def run_full_maintenance(self):
        """Run complete maintenance routine"""
        print("[INFO] Starting LovePDFs maintenance routine...")
        print("=" * 50)
        
        success_count = 0
        total_tasks = 6
        
        # Task 1: Generate missing tools
        if self.check_and_generate_missing_tools():
            success_count += 1
            self.log['stats']['tools_generated'] += 1
        
        # Task 2: Enhance internal links
        if self.enhance_internal_links():
            success_count += 1
            self.log['stats']['internal_links_added'] += 1
        
        # Task 3: Add content to tools
        if self.add_content_to_tools():
            success_count += 1
            self.log['stats']['pages_enhanced'] += 1
        
        # Task 4: Create blog post
        if self.create_daily_blog_post():
            success_count += 1
            self.log['stats']['blogs_created'] += 1
        
        # Task 5: Update sitemap
        if self.update_sitemap():
            success_count += 1
        
        # Task 6: Generate report
        report = self.generate_maintenance_report()
        report_file = self.base_dir / "maintenance_report.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        success_count += 1
        
        # Save log
        self.save_maintenance_log()
        
        print("=" * 50)
        print(f"[INFO] Maintenance complete: {success_count}/{total_tasks} tasks successful")
        print(f"[INFO] Report saved to: maintenance_report.md")
        
        return success_count == total_tasks

def main():
    """Main maintenance routine"""
    scheduler = MaintenanceScheduler()
    scheduler.run_full_maintenance()

if __name__ == "__main__":
    main()
