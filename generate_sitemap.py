#!/usr/bin/env python3
import json
from datetime import datetime

with open('tools-config.json', 'r') as f:
    config = json.load(f)

tools = config['tools']

# 生成sitemap.xml
sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://case-converter.laolin.ai/</loc>
        <lastmod>{}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
'''.format(datetime.now().strftime('%Y-%m-%d'))

for tool in tools:
    sitemap += f'''    <url>
        <loc>https://case-converter.laolin.ai/{tool['id']}.html</loc>
        <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
'''

sitemap += '</urlset>\n'

with open('sitemap.xml', 'w') as f:
    f.write(sitemap)

print(f"✅ Generated sitemap.xml with {len(tools) + 1} URLs")

# 生成robots.txt
robots = '''User-agent: *
Allow: /

Sitemap: https://case-converter.laolin.ai/sitemap.xml
'''

with open('robots.txt', 'w') as f:
    f.write(robots)

print("✅ Generated robots.txt")
