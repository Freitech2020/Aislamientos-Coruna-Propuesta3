import os

filepath = r'e:\DATA C\Downloads\WEBS\WEBs de SEOLIFE\Web aislamientos-coruña-nor-project\Propuesta 3\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Reduce vertical paddings
content = content.replace('py-16 md:py-20', 'py-10 md:py-14')
content = content.replace('py-20', 'py-14')
content = content.replace('py-16', 'py-10')
content = content.replace('pt-32 md:pt-40', 'pt-24 md:pt-32')

# Reduce space-y classes for section inner gaps
content = content.replace('space-y-12', 'space-y-8')
content = content.replace('space-y-10', 'space-y-6')
content = content.replace('space-y-16', 'space-y-10')

# Inject Swiper CSS and JS in the head if not present
if 'swiper-bundle.min.css' not in content:
    content = content.replace('</head>', '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />\n</head>')

if 'swiper-bundle.min.js' not in content:
    content = content.replace('</body>', '    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Padding reduced and Swiper assets injected.')
