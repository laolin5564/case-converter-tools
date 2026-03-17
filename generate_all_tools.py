#!/usr/bin/env python3
import json
import os

# 读取工具配置
with open('tools-config.json', 'r') as f:
    config = json.load(f)

tools = config['tools']

# 工具分类导航
categories = {
    "text-tools": "Text Tools",
    "converters": "Converters", 
    "generators": "Generators",
    "dev-tools": "Dev Tools"
}

# 获取分类工具
def get_tools_by_category(category):
    return [t for t in tools if t.get('category') == category]

# 生成导航HTML
def generate_nav(active_id=None):
    nav_links = []
    for cat_id, cat_name in categories.items():
        cat_tools = get_tools_by_category(cat_id)
        if cat_tools:
            # 使用第一个工具作为分类入口
            first_tool = cat_tools[0]
            nav_links.append(f'<li><a href="/{first_tool["id"]}.html">{cat_name}</a></li>')
    
    return f'''<header>
        <nav>
            <a href="/" class="logo">🔧 Text Tools</a>
            <ul>
                <li><a href="/">Home</a></li>
                {chr(10).join(nav_links)}
            </ul>
        </nav>
    </header>'''

# 生成相关工具卡片
def generate_related_tools(current_id, category):
    related = [t for t in tools if t.get('category') == category and t['id'] != current_id][:7]
    # 如果同类不够，再从其他类补充
    if len(related) < 7:
        other = [t for t in tools if t.get('category') != category and t['id'] != current_id]
        related.extend(other[:7-len(related)])
    
    cards_html = []
    for tool in related:
        cards_html.append(f'''<a href="/{tool['id']}.html" class="card">
                    <h3>{tool['title']}</h3>
                    <p>{tool['description']}</p>
                </a>''')
    
    return f'''<section class="converters-list">
            <h2>Related Tools</h2>
            <div class="converter-cards">
                {chr(10).join(cards_html)}
            </div>
        </section>'''

# 生成HTML页面模板
def generate_html_page(tool):
    tool_id = tool['id']
    title = tool['title']
    description = tool['description']
    keywords = tool['keywords']
    category = tool.get('category', 'text-tools')
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Free Online Tool</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <link rel="canonical" href="https://case-converter.laolin.ai/{tool_id}.html">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🔧</text></svg>">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {generate_nav(tool_id)}

    <main>
        <section class="hero">
            <h1>{title} — Free Online Tool</h1>
            <p>{description}</p>
        </section>

        <section class="tool-section" id="toolSection">
            <!-- Tool UI will be inserted by JS -->
        </section>

        <section class="seo-content">
            <h2>About {title}</h2>
            <p>Our free {title.lower()} helps you process text quickly and efficiently. This tool is perfect for developers, writers, students, and anyone who works with text data. All processing happens in your browser - your data never leaves your device.</p>

            <h2>How to Use {title}</h2>
            <ul>
                <li>Paste or type your text in the input area</li>
                <li>Click the convert/process button</li>
                <li>Copy the result or download it</li>
                <li>All processing is instant and happens locally in your browser</li>
            </ul>

            <h2>Why Use Our {title}?</h2>
            <ul>
                <li><strong>100% Free:</strong> No registration, no limits, completely free to use</li>
                <li><strong>Privacy First:</strong> All processing happens in your browser - no server uploads</li>
                <li><strong>Fast & Easy:</strong> Instant results with a clean, simple interface</li>
                <li><strong>Mobile Friendly:</strong> Works perfectly on desktop, tablet, and mobile</li>
            </ul>
        </section>

        <section class="faq">
            <h2>Frequently Asked Questions</h2>
            <details>
                <summary>Is {title} really free?</summary>
                <p>Yes, completely free with no hidden costs or registration required.</p>
            </details>
            <details>
                <summary>Is my data safe?</summary>
                <p>Yes! All processing happens locally in your browser. Your text never leaves your device and is never sent to any server.</p>
            </details>
            <details>
                <summary>Is there a limit on text size?</summary>
                <p>There are no hard limits, but very large texts may slow down on older devices since processing happens in your browser.</p>
            </details>
            <details>
                <summary>Can I use this tool offline?</summary>
                <p>Once the page loads, basic functionality works offline since all processing is client-side JavaScript.</p>
            </details>
        </section>

        {generate_related_tools(tool_id, category)}
    </main>

    <footer>
        <p>© 2026 Text Tools. Free online text processing tools.</p>
        <p>
            <a href="/">Home</a> ·
            <a href="/word-counter.html">Word Counter</a> ·
            <a href="/character-counter.html">Character Counter</a> ·
            <a href="/base64-encode.html">Base64 Encoder</a> ·
            <a href="/json-formatter.html">JSON Formatter</a>
        </p>
    </footer>

    <script src="{tool_id}.js"></script>
</body>
</html>'''

# 生成所有HTML页面
for tool in tools:
    html_content = generate_html_page(tool)
    filename = f"{tool['id']}.html"
    with open(filename, 'w') as f:
        f.write(html_content)
    print(f"✅ Generated {filename}")

print(f"\n🎉 Generated {len(tools)} HTML pages successfully!")
