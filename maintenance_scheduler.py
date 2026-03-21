#!/usr/bin/env python3
"""
Automated maintenance scheduler for LovePDFs website
Run this script regularly to maintain and enhance your site
"""

import os
import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path

class MaintenanceScheduler:
    def __init__(self, base_dir="/home/rameez/Downloads/ilovepdfs"):
        self.base_dir = Path(base_dir)
        self.log_file = self.base_dir / "maintenance_log.json"
        self.load_maintenance_log()
    
    def load_maintenance_log(self):
        """Load maintenance history"""
        if self.log_file.exists():
            with open(self.log_file, 'r') as f:
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
        with open(self.log_file, 'w') as f:
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
        print(f"🔄 Running: {description}")
        try:
            result = subprocess.run(
                ["python3", script_name],
                cwd=self.base_dir,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                print(f"✅ Success: {description}")
                self.log_task(script_name, True, result.stdout)
                return True
            else:
                print(f"❌ Error: {description}")
                print(f"Error output: {result.stderr}")
                self.log_task(script_name, False, result.stderr)
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏰ Timeout: {description}")
            self.log_task(script_name, False, "Script timed out after 5 minutes")
            return False
        except Exception as e:
            print(f"💥 Exception: {description} - {e}")
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
        """Create a new blog post"""
        return self.run_script(
            "blog_manager.py",
            "Create daily blog post"
        )
    
    def update_sitemap(self):
        """Update sitemap with latest pages"""
        sitemap_content = self.generate_sitemap()
        sitemap_file = self.base_dir / "sitemap.xml"
        with open(sitemap_file, 'w') as f:
            f.write(sitemap_content)
        print("✅ Updated sitemap.xml")
        return True
    
    def generate_sitemap(self):
        """Generate XML sitemap"""
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
    <priority>0.7</priority>
  </url>""")
        
        # Add blog posts
        blog_dir = self.base_dir / "blog-posts"
        if blog_dir.exists():
            for post_file in blog_dir.glob("*.html"):
                urls.append(f"""  <url>
    <loc>{base_url}/blog-posts/{post_file.stem}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>""")
        
        sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""
        
        return sitemap
    
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
        print("🚀 Starting LovePDFs maintenance routine...")
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
        with open(report_file, 'w') as f:
            f.write(report)
        success_count += 1
        
        # Save log
        self.save_maintenance_log()
        
        print("=" * 50)
        print(f"🎉 Maintenance complete: {success_count}/{total_tasks} tasks successful")
        print(f"📊 Report saved to: maintenance_report.md")
        
        return success_count == total_tasks

def main():
    """Main maintenance routine"""
    scheduler = MaintenanceScheduler()
    scheduler.run_full_maintenance()

if __name__ == "__main__":
    main()
