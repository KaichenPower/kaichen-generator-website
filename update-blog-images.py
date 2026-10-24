import os

base_dir = "D:/projects/kaichen-generator-website/content/blog"
slug = "generator-wont-start-7-causes"

languages = ["ru", "es", "fr", "de", "pt", "ar", "tr", "th", "vi", "id"]

image_line = "![A diesel generator set in our Yangzhou factory test cell](/images/blog/generator-wont-start.jpg)\n\n"

for lang in languages:
    filepath = os.path.join(base_dir, lang, f"{slug}.md")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 如果还没有图片引用，就在 frontmatter 后面加上
        if '![' not in content and '](/images/blog/' not in content:
            # 找到 frontmatter 结束位置（第二个 ---）
            parts = content.split('---', 2)
            if len(parts) >= 3:
                new_content = parts[0] + '---' + parts[1] + '---\n\n' + image_line + parts[2]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated image in {lang}")
            else:
                print(f"Skipped {lang}: cannot find frontmatter")
        else:
            print(f"Already has image: {lang}")

print("Done!")
