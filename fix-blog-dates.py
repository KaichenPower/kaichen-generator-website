import os
import re

base_dir = "D:/projects/kaichen-generator-website/content/blog"

def fix_date_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配 frontmatter 中的 date 字段
    # date: 2026-10-24 -> date: "2026-10-24"
    new_content = re.sub(r'^date: (\d{4}-\d{2}-\d{2})$', r'date: "\1"', content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# 遍历所有 md 文件
count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            if fix_date_in_file(filepath):
                count += 1
                print(f"Fixed: {filepath}")

print(f"\nTotal fixed: {count}")
