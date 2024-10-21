#!/usr/bin/env python3

from jinja2 import Template
import markdown2

# Sample Markdown content
markdown_content = """
@title Main Title of the Article
@subtitle Subtitle of the Article

# Chapter 1: Introduction
This is the introduction to the article. It provides an overview of the topics that will be covered.

## Section 1.1: Background
This section provides background information necessary to understand the context of the article.

# Chapter 2: Main Content
This chapter delves into the main content of the article, discussing key points in detail.

## Section 2.1: Key Point One
Details about the first key point are discussed here.

## Section 2.2: Key Point Two
Details about the second key point are discussed here.

# Chapter 3: Conclusion
The conclusion summarizes the main points and provides final thoughts on the topic.
"""

# Function to extract main title and subtitle
def extract_titles_and_clean(markdown_text):
    lines = markdown_text.splitlines()
    main_title = ""
    subtitle = ""
    cleaned_lines = []

  for line in lines:
      if line.startswith("@title "):
          main_title = line[len("@title "):].strip()
      elif line.startswith("@subtitle "):
          subtitle = line[len("@subtitle "):].strip()
      else:
          cleaned_lines.append(line)

  cleaned_markdown = "\n".join(cleaned_lines)
  return main_title, subtitle, cleaned_markdown

# Extract main title, subtitle, and clean the markdown content
main_title, subtitle, cleaned_markdown_content = extract_titles_and_clean(markdown_content)

# Convert cleaned Markdown to HTML
html_content = markdown2.markdown(cleaned_markdown_content)

# HTML template with Jinja2
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ main_title }}</title>
  <style>
      body {
          font-family: Arial, sans-serif;
          line-height: 1.6;
          margin: 0;
          padding: 0;
          color: #333;
      }
      header {
          background-color: #f4f4f4;
          padding: 20px;
          text-align: center;
          border-bottom: 1px solid #ddd;
      }
      .main-title {
          margin: 0;
          font-size: 2.5em;
      }
      .subtitle {
          margin: 0;
          font-size: 1.5em;
          color: #666;
      }
      article {
          padding: 20px;
          max-width: 800px;
          margin: 20px auto;
      }
      h1 {
          font-size: 2em;
          margin-top: 1em;
          color: #444;
      }
      h2 {
          font-size: 1.5em;
          margin-top: 0.75em;
          color: #555;
      }
      p {
          margin: 1em 0;
      }
  </style>
</head>
<body>
  <header>
      <div class="main-title">{{ main_title }}</div>
      <div class="subtitle">{{ subtitle }}</div>
  </header>
  <article>
      {{ content|safe }}
  </article>
</body>
</html>
"""

# Render the template with the HTML content and titles
template = Template(html_template)
rendered_html = template.render(main_title=main_title, subtitle=subtitle, content=html_content)

# Save the rendered HTML to a file
with open("article.html", "w") as file:
    file.write(rendered_html)

print("article.html")
