#!/usr/bin/env python3
"""
Generate comprehensive schema markup for enhanced SERP appearance
Includes Organization, WebSite, WebApplication, Article, and HowTo schemas
"""

import json
from datetime import datetime
from pathlib import Path

class SchemaGenerator:
    def __init__(self, base_dir="/home/rameez/Downloads/ilovepdfs"):
        self.base_dir = Path(base_dir)
        self.site_url = "https://lovepdfs.com"
    
    def generate_organization_schema(self):
        """Generate Organization schema markup"""
        schema = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "LovePDFs",
            "url": self.site_url,
            "logo": f"{self.site_url}/favicon.png",
            "description": "Free online PDF and image tools platform offering 40+ professional tools for document management",
            "sameAs": [
                # Add social media URLs when available
            ],
            "contactPoint": {
                "@type": "ContactPoint",
                "email": "huchusim@gmail.com",
                "contactType": "customer service"
            },
            "founder": {
                "@type": "Person",
                "name": "LovePDFs Team"
            },
            "foundingDate": "2024",
            "areaServed": "Worldwide",
            "knowsLanguage": ["en"],
            "makesOffer": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": "PDF Tools",
                        "description": "Free online PDF manipulation tools"
                    },
                    "price": "0",
                    "priceCurrency": "USD"
                }
            ]
        }
        return schema
    
    def generate_website_schema(self):
        """Generate WebSite schema markup"""
        schema = {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "LovePDFs",
            "url": self.site_url,
            "description": "Free online platform offering PDF and image tools such as compress PDF, merge PDF, resize images, and convert files instantly",
            "potentialAction": {
                "@type": "SearchAction",
                "target": {
                    "@type": "EntryPoint",
                    "urlTemplate": f"{self.site_url}/?q={{search_term_string}}"
                },
                "query-input": "required name=search_term_string"
            },
            "publisher": {
                "@type": "Organization",
                "name": "LovePDFs"
            },
            "inLanguage": "en-US"
        }
        return schema
    
    def generate_webapp_schema(self, tool_name=None, tool_url=None):
        """Generate WebApplication schema for tools"""
        if tool_name and tool_url:
            # Specific tool schema
            schema = {
                "@context": "https://schema.org",
                "@type": "WebApplication",
                "name": tool_name,
                "url": tool_url,
                "description": f"Free online {tool_name} tool - Process files instantly in your browser",
                "applicationCategory": "UtilitiesApplication",
                "operatingSystem": "Any",
                "browserRequirements": "Requires JavaScript",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD"
                },
                "featureList": [
                    "Browser-based processing",
                    "No file uploads required",
                    "Instant processing",
                    "Privacy-focused",
                    "No registration needed"
                ],
                "screenshot": f"{self.site_url}/favicon.png",
                "softwareVersion": "1.0",
                "author": {
                    "@type": "Organization",
                    "name": "LovePDFs"
                }
            }
        else:
            # General webapp schema
            schema = {
                "@context": "https://schema.org",
                "@type": "WebApplication",
                "name": "LovePDFs - Free PDF & Image Tools",
                "url": self.site_url,
                "description": "Free online platform offering 40+ PDF and image tools for document management",
                "applicationCategory": "UtilitiesApplication",
                "operatingSystem": "Any",
                "browserRequirements": "Requires JavaScript",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD"
                },
                "featureList": [
                    "PDF merging and splitting",
                    "PDF compression and conversion",
                    "Image resizing and conversion",
                    "Document editing and security",
                    "Calculator tools",
                    "Browser-based processing",
                    "Privacy-focused design"
                ],
                "screenshot": f"{self.site_url}/favicon.png",
                "softwareVersion": "1.0",
                "author": {
                    "@type": "Organization",
                    "name": "LovePDFs"
                }
            }
        return schema
    
    def generate_article_schema(self, title, url, description, author="LovePDFs Team"):
        """Generate Article schema for blog posts"""
        schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "url": url,
            "description": description,
            "datePublished": datetime.now().strftime("%Y-%m-%d"),
            "dateModified": datetime.now().strftime("%Y-%m-%d"),
            "author": {
                "@type": "Person",
                "name": author
            },
            "publisher": {
                "@type": "Organization",
                "name": "LovePDFs",
                "logo": {
                    "@type": "ImageObject",
                    "url": f"{self.site_url}/favicon.png"
                }
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": url
            },
            "image": f"{self.site_url}/favicon.png",
            "articleSection": "Technology",
            "wordCount": 1500,
            "inLanguage": "en-US"
        }
        return schema
    
    def generate_howto_schema(self, tool_name, steps, tool_url):
        """Generate HowTo schema for tool instructions"""
        schema = {
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": f"How to {tool_name}",
            "description": f"Step-by-step guide on how to {tool_name.lower()} using our free online tool",
            "url": tool_url,
            "image": f"{self.site_url}/favicon.png",
            "estimatedCost": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": "0"
            },
            "totalTime": "PT2M",
            "supply": [
                {
                    "@type": "HowToSupply",
                    "name": "PDF or image files"
                }
            ],
            "tool": [
                {
                    "@type": "HowToTool",
                    "name": "LovePDFs Online Tool"
                }
            ],
            "step": []
        }
        
        # Add steps
        for i, step in enumerate(steps, 1):
            step_schema = {
                "@type": "HowToStep",
                "name": f"Step {i}",
                "text": step,
                "image": f"{self.site_url}/favicon.png",
                "url": f"{tool_url}#step{i}"
            }
            schema["step"].append(step_schema)
        
        return schema
    
    def generate_faq_schema(self, faqs):
        """Generate FAQ schema markup"""
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": []
        }
        
        for faq in faqs:
            faq_item = {
                "@type": "Question",
                "name": faq["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq["answer"]
                }
            }
            schema["mainEntity"].append(faq_item)
        
        return schema
    
    def generate_breadcrumblist_schema(self, breadcrumbs):
        """Generate BreadcrumbList schema"""
        schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": []
        }
        
        for i, crumb in enumerate(breadcrumbs, 1):
            item = {
                "@type": "ListItem",
                "position": i,
                "name": crumb["name"],
                "item": crumb["url"]
            }
            schema["itemListElement"].append(item)
        
        return schema
    
    def generate_service_schema(self, service_name, description, url):
        """Generate Service schema for tool categories"""
        schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": service_name,
            "description": description,
            "url": url,
            "provider": {
                "@type": "Organization",
                "name": "LovePDFs"
            },
            "serviceType": "Online Tool",
            "areaServed": "Worldwide",
            "hasOfferCatalog": {
                "@type": "OfferCatalog",
                "name": f"{service_name} Tools",
                "itemListElement": []
            }
        }
        return schema
    
    def add_schema_to_page(self, page_path, schemas):
        """Add schema markup to a page"""
        page_file = self.base_dir / page_path
        
        if not page_file.exists():
            return False
        
        with open(page_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Generate schema JSON-LD
        schema_json = json.dumps(schemas, indent=2)
        schema_html = f"""
<script type="application/ld+json">
{schema_json}
</script>"""
        
        # Insert schema in head section
        if '</head>' in content:
            content = content.replace('</head>', schema_html + '\n</head>')
        else:
            content = schema_html + '\n' + content
        
        with open(page_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    def generate_all_tool_schemas(self):
        """Generate schemas for all tool pages"""
        tools_dir = self.base_dir
        generated_count = 0
        
        for item in tools_dir.iterdir():
            if item.is_dir() and (item / "index.html").exists():
                tool_name = item.name.replace('-', ' ').title()
                tool_url = f"{self.site_url}/{item.name}/"
                
                # Generate schemas for this tool
                schemas = [
                    self.generate_webapp_schema(tool_name, tool_url),
                    self.generate_breadcrumblist_schema([
                        {"name": "Home", "url": self.site_url},
                        {"name": "Tools", "url": f"{self.site_url}/all-tools.html"},
                        {"name": tool_name, "url": tool_url}
                    ])
                ]
                
                # Add HowTo schema with generic steps
                steps = [
                    "Upload your files to the tool",
                    "Configure the tool settings if needed",
                    "Process your files",
                    "Download the results"
                ]
                schemas.append(self.generate_howto_schema(tool_name, steps, tool_url))
                
                # Add to page
                if self.add_schema_to_page(f"{item.name}/index.html", schemas):
                    generated_count += 1
                    print(f"✓ Added schema to: {item.name}")
        
        return generated_count
    
    def generate_homepage_schema(self):
        """Generate comprehensive schema for homepage"""
        schemas = [
            self.generate_organization_schema(),
            self.generate_website_schema(),
            self.generate_webapp_schema(),
            self.generate_breadcrumblist_schema([
                {"name": "Home", "url": self.site_url}
            ])
        ]
        
        return self.add_schema_to_page("index.html", schemas)
    
    def generate_blog_schema(self, blog_title, blog_url, blog_description):
        """Generate schema for blog posts"""
        schemas = [
            self.generate_article_schema(blog_title, blog_url, blog_description),
            self.generate_breadcrumblist_schema([
                {"name": "Home", "url": self.site_url},
                {"name": "Blog", "url": f"{self.site_url}/blog.html"},
                {"name": blog_title, "url": blog_url}
            ])
        ]
        
        return schemas
    
    def generate_all_blog_schemas(self):
        """Generate schemas for all blog posts"""
        blog_dir = self.base_dir / "blog-posts"
        if not blog_dir.exists():
            return 0
        
        generated_count = 0
        for post_file in blog_dir.glob("*.html"):
            # Extract title from filename
            title = post_file.stem.replace('-', ' ').title()
            url = f"{self.site_url}/blog-posts/{post_file.stem}"
            description = f"Comprehensive guide on {title.lower()}"
            
            schemas = self.generate_blog_schema(title, url, description)
            
            if self.add_schema_to_page(f"blog-posts/{post_file.name}", schemas):
                generated_count += 1
                print(f"✓ Added schema to blog: {post_file.stem}")
        
        return generated_count
    
    def generate_comprehensive_schemas(self):
        """Generate all schema markup for the site"""
        print("🔧 Generating comprehensive schema markup...")
        print("=" * 50)
        
        total_generated = 0
        
        # Homepage schema
        if self.generate_homepage_schema():
            total_generated += 1
            print("✓ Added homepage schema")
        
        # Tool page schemas
        tool_count = self.generate_all_tool_schemas()
        total_generated += tool_count
        print(f"✓ Added schemas to {tool_count} tool pages")
        
        # Blog post schemas
        blog_count = self.generate_all_blog_schemas()
        total_generated += blog_count
        print(f"✓ Added schemas to {blog_count} blog posts")
        
        print("=" * 50)
        print(f"🎉 Total pages with schema markup: {total_generated}")
        print("📈 Enhanced SERP appearance enabled")
        
        return total_generated

def main():
    """Main schema generation routine"""
    generator = SchemaGenerator()
    generator.generate_comprehensive_schemas()

if __name__ == "__main__":
    main()
