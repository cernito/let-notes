#!/usr/bin/env python3
"""
Generate HTML lecture pages from Markdown files
Run this script whenever you update your .md files to regenerate the HTML pages
"""

import os
import re
import subprocess

def create_html_from_md(md_file, html_file, lecture_num):
    """Convert a markdown file to HTML with our custom template"""
    
    print(f"Processing {md_file}...", end=" ")
    
    # Read the markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract title from YAML frontmatter
    title_match = re.search(r'title:\s*"([^"]+)"', md_content)
    title = title_match.group(1) if title_match else f"Přednáška {lecture_num}"
    
    # Remove YAML frontmatter
    md_content = re.sub(r'^---.*?---\n', '', md_content, flags=re.DOTALL)
    
    # Save to temp file for pandoc
    temp_md = '/tmp/temp_lecture.md'
    with open(temp_md, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    # Convert markdown to HTML using pandoc
    try:
        result = subprocess.run(
            ['pandoc', temp_md, '-f', 'markdown', '-t', 'html', '--mathjax'],
            capture_output=True,
            text=True,
            check=True
        )
        content_html = result.stdout
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Pandoc failed for {md_file}")
        print(e.stderr)
        return None
    except FileNotFoundError:
        print("ERROR: Pandoc not found. Please install pandoc.")
        return None
    
    # Create full HTML with our template
    html_template = f'''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="cs" xml:lang="cs">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="theme-color" content="#3498db" />
  <meta name="author" content="Tomáš Černík" />
  <meta name="description" content="{title} - Studijní materiály">
  <title>{title}</title>
  <style>
    code{{white-space: pre-wrap;}}
    span.smallcaps{{font-variant: small-caps;}}
    div.columns{{display: flex; gap: min(4vw, 1.5em);}}
    div.column{{flex: auto; overflow-x: auto;}}
    div.hanging-indent{{margin-left: 1.5em; text-indent: -1.5em;}}
    ul.task-list[class]{{list-style: none;}}
    ul.task-list li input[type="checkbox"] {{
      font-size: inherit;
      width: 0.8em;
      margin: 0 0.8em 0.2em -1.6em;
      vertical-align: middle;
    }}
  </style>
  <link rel="stylesheet" href="styles.css" />
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js" type="text/javascript"></script>
</head>
<body>

<!-- Controls Panel -->
<div class="controls-panel">
  <div class="search-box">
    <input type="text" id="searchInput" placeholder="🔍 Hledat v poznámkách..." />
  </div>
  <div class="controls-buttons">
    <button class="btn" onclick="window.location.href='index.html'" title="Zpět na hlavní stránku">🏠 Domů</button>
    <button class="btn" onclick="toggleAllSections()">Rozbalit vše</button>
    <button class="btn" onclick="collapseAllSections()">Sbalit vše</button>
    <button class="btn btn-icon" onclick="toggleTheme()" title="Přepnout tmavý režim">🌙</button>
    <button class="btn btn-icon" onclick="window.print()" title="Vytisknout">🖨️</button>
  </div>
  <div class="progress-container">
    <div class="progress-bar" id="progressBar"></div>
  </div>
</div>

<header id="title-block-header">
  <h1 class="title">{title}</h1>
  <p class="author">Tomáš Černík</p>
</header>

{content_html}

<script>
// Detect if user is on mobile
const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

// Add collapsible class to all sectionboxes
document.querySelectorAll('.sectionbox').forEach(box => {{
  box.classList.add('collapsible');
}});

// Theme Toggle
function toggleTheme() {{
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  html.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  const btn = event.target.closest('.btn-icon');
  if (btn) {{
    btn.textContent = newTheme === 'dark' ? '☀️' : '🌙';
  }}
  
  const metaTheme = document.querySelector('meta[name="theme-color"]');
  if (metaTheme) {{
    metaTheme.content = newTheme === 'dark' ? '#1a1d23' : '#3498db';
  }}
}}

// Load saved theme
(function() {{
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  const themeBtn = document.querySelector('.btn-icon');
  if (themeBtn && savedTheme === 'dark') {{
    themeBtn.textContent = '☀️';
  }}
  
  const metaTheme = document.querySelector('meta[name="theme-color"]');
  if (metaTheme) {{
    metaTheme.content = savedTheme === 'dark' ? '#1a1d23' : '#3498db';
  }}
}})();

// Collapsible sections with touch optimization
document.querySelectorAll('.sectionbox.collapsible > h2').forEach(header => {{
  header.addEventListener('click', function(e) {{
    e.preventDefault();
    this.parentElement.classList.toggle('collapsed');
    updateProgress();
    
    if (isMobile && !this.parentElement.classList.contains('collapsed')) {{
      setTimeout(() => {{
        this.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}, 100);
    }}
  }});
  
  header.addEventListener('touchstart', function(e) {{
    this.style.webkitUserSelect = 'none';
    this.style.userSelect = 'none';
  }});
}});

function toggleAllSections() {{
  document.querySelectorAll('.sectionbox.collapsible').forEach(section => {{
    section.classList.remove('collapsed');
  }});
  updateProgress();
}}

function collapseAllSections() {{
  document.querySelectorAll('.sectionbox.collapsible').forEach(section => {{
    section.classList.add('collapsed');
  }});
  updateProgress();
  
  if (isMobile) {{
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }}
}}

// Search functionality
const searchInput = document.getElementById('searchInput');
let searchTimeout;

searchInput.addEventListener('input', function() {{
  clearTimeout(searchTimeout);
  const delay = isMobile ? 400 : 300;
  
  searchTimeout = setTimeout(() => {{
    const query = this.value.toLowerCase().trim();
    const sections = document.querySelectorAll('.sectionbox');
    let firstMatch = null;
    
    sections.forEach(section => {{
      section.classList.remove('highlight');
      
      if (query === '') {{
        section.style.display = '';
        return;
      }}
      
      const text = section.textContent.toLowerCase();
      if (text.includes(query)) {{
        section.style.display = '';
        section.classList.add('highlight');
        section.classList.remove('collapsed');
        if (!firstMatch) firstMatch = section;
      }} else {{
        section.style.display = 'none';
      }}
    }});
    
    if (isMobile && firstMatch && query !== '') {{
      setTimeout(() => {{
        firstMatch.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}, 100);
    }}
    
    updateProgress();
  }}, delay);
}});

if (isMobile) {{
  document.addEventListener('touchstart', function(e) {{
    if (!searchInput.contains(e.target) && searchInput.value === '') {{
      searchInput.blur();
    }}
  }});
}}

// Progress tracking
function updateProgress() {{
  const sections = document.querySelectorAll('.sectionbox.collapsible');
  const expanded = document.querySelectorAll('.sectionbox.collapsible:not(.collapsed)');
  const percentage = (expanded.length / sections.length) * 100;
  document.getElementById('progressBar').style.width = percentage + '%';
}}

// Scroll progress indicator
let scrollTimeout;
window.addEventListener('scroll', function() {{
  clearTimeout(scrollTimeout);
  scrollTimeout = setTimeout(() => {{
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    document.getElementById('progressBar').style.width = scrolled + '%';
  }}, isMobile ? 50 : 0);
}}, {{ passive: true }});

// Initialize
updateProgress();

// Auto-collapse all sections on mobile
if (isMobile) {{
  document.querySelectorAll('.sectionbox.collapsible').forEach(section => {{
    section.classList.add('collapsed');
  }});
  updateProgress();
}}

// Keyboard shortcuts (desktop only)
if (!isMobile) {{
  document.addEventListener('keydown', function(e) {{
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {{
      e.preventDefault();
      searchInput.focus();
    }}
    
    if ((e.ctrlKey || e.metaKey) && e.key === 'd') {{
      e.preventDefault();
      toggleTheme();
    }}
  }});
}}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
  anchor.addEventListener('click', function (e) {{
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {{
      target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
  }});
}});

if ('vibrate' in navigator && isMobile) {{
  document.querySelectorAll('.sectionbox.collapsible > h2').forEach(header => {{
    header.addEventListener('click', function() {{
      navigator.vibrate(10);
    }});
  }});
}}

if (isMobile) {{
  if (navigator.hardwareConcurrency && navigator.hardwareConcurrency < 4) {{
    document.documentElement.style.setProperty('--transition-fast', '0ms');
    document.documentElement.style.setProperty('--transition-normal', '0ms');
    document.documentElement.style.setProperty('--transition-slow', '0ms');
  }}
}}
</script>

</body>
</html>'''
    
    # Write the HTML file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"✓ Created {html_file}")
    return title


def main():
    """Main function to generate all lecture HTML files"""
    
    print("=" * 60)
    print("Generating HTML Lecture Pages")
    print("=" * 60)
    print()
    
    # Check if pandoc is installed
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
    except FileNotFoundError:
        print("ERROR: Pandoc is not installed!")
        print("Please install pandoc: https://pandoc.org/installing.html")
        return
    
    # Generate HTML for all lectures
    lecture_titles = {}
    
    for i in range(1, 18):
        num = f"{i:02d}"
        md_file = f"lecture{num}.md"
        html_file = f"lecture{num}.html"
        
        if os.path.exists(md_file):
            title = create_html_from_md(md_file, html_file, i)
            if title:
                lecture_titles[i] = title
        else:
            print(f"⚠ Warning: {md_file} not found, skipping...")
    
    print()
    print("=" * 60)
    print(f"✅ Successfully generated {len(lecture_titles)} HTML files!")
    print("=" * 60)
    print()
    print("Generated lectures:")
    for num, title in lecture_titles.items():
        print(f"  {num:2d}. {title}")
    print()
    print("Next steps:")
    print("  1. Review the generated HTML files")
    print("  2. Upload to GitHub (index.html, lectureXX.html, styles.css)")
    print("  3. Push changes")
    print()


if __name__ == "__main__":
    main()
