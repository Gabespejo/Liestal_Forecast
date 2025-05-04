import os

# === Configuration ===
image_folder = "."  # same folder where images and script are
image_prefix = "Liestal_2m_11_11-"
image_suffix = "_nocbar.png"
steps = ["0000","0012", "0024", "0036", "0048", "0060"]

output_html = os.path.join(image_folder, "slider_viewer.html")

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Lead Time Viewer</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f7f7f7;
        }}
        img {{
            max-width: 90%;
            height: auto;
            border: 1px solid #ccc;
            margin-bottom: 10px;
        }}
        input[type=range] {{
            width: 60%;
        }}
    </style>
</head>
<body>

<h2>Lead Time Viewer</h2>
<img id="mainImage" src="{image_prefix}{steps[0]}{image_suffix}" alt="Lead Time Image">

<br>
<label for="leadSlider">Lead Time (h): </label>
<input type="range" min="0" max="{len(steps)-1}" value="0" id="leadSlider">

<script>
    const steps = {steps};
    const prefix = "{image_prefix}";
    const suffix = "{image_suffix}";
    const imageFolder = "";
    const slider = document.getElementById("leadSlider");
    const img = document.getElementById("mainImage");

    slider.addEventListener("input", () => {{
        const step = steps[parseInt(slider.value)];
        img.src = prefix + step + suffix;
    }});
</script>

</body>
</html>
"""

with open(output_html, "w") as f:
    f.write(html_content)

print(f"✅ HTML viewer created at: {output_html}")