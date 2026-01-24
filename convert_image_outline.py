#!/usr/bin/env python3
"""
Image Converter: Add white outline to transparent images
Converts images to transparent background with white outline
"""

from PIL import Image, ImageFilter, ImageDraw, ImageOps
import numpy as np
import sys
import os

def remove_background_simple(img, threshold=240):
    """
    Simple background removal for logos with white/light backgrounds
    Converts near-white pixels to transparent
    """
    img = img.convert('RGBA')
    data = np.array(img)

    # Get RGB channels
    r, g, b, a = data.T

    # Find white/light areas (all RGB values above threshold)
    white_areas = (r > threshold) & (g > threshold) & (b > threshold)

    # Set alpha to 0 (transparent) for white areas
    data[..., 3] = np.where(white_areas.T, 0, 255)

    return Image.fromarray(data)

def add_white_outline(img, outline_width=3):
    """
    Add white outline to image using dilation method
    """
    img = img.convert('RGBA')

    # Extract alpha channel
    alpha = img.split()[3]

    # Create outline by dilating (expanding) the alpha channel
    outline = alpha
    for i in range(outline_width):
        outline = outline.filter(ImageFilter.MaxFilter(3))

    # Create white outline layer
    outline_layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
    outline_layer.putalpha(outline)

    # Composite original image over white outline
    result = Image.alpha_composite(outline_layer, img)

    return result

def add_white_glow(img, glow_radius=5, glow_intensity=0.8):
    """
    Add soft white glow effect around image
    """
    img = img.convert('RGBA')

    # Create glow layer
    glow = Image.new('RGBA', img.size, (0, 0, 0, 0))

    # Extract alpha and blur it for glow effect
    alpha = img.split()[3]
    glow_alpha = alpha.filter(ImageFilter.GaussianBlur(glow_radius))

    # Create white glow with reduced opacity
    glow_data = np.array(glow)
    glow_alpha_data = np.array(glow_alpha)
    glow_data[..., 0] = 255  # R
    glow_data[..., 1] = 255  # G
    glow_data[..., 2] = 255  # B
    glow_data[..., 3] = (glow_alpha_data * glow_intensity).astype(np.uint8)  # A

    glow = Image.fromarray(glow_data)

    # Composite original over glow
    result = Image.alpha_composite(glow, img)

    return result

def add_purple_glow(img, glow_radius=5, glow_intensity=0.8):
    """
    Add soft light purple glow effect around image
    """
    img = img.convert('RGBA')

    # Create glow layer
    glow = Image.new('RGBA', img.size, (0, 0, 0, 0))

    # Extract alpha and blur it for glow effect
    alpha = img.split()[3]
    glow_alpha = alpha.filter(ImageFilter.GaussianBlur(glow_radius))

    # Create light purple glow (matching your site's purple accent)
    glow_data = np.array(glow)
    glow_alpha_data = np.array(glow_alpha)
    glow_data[..., 0] = 167  # R - light purple
    glow_data[..., 1] = 139  # G
    glow_data[..., 2] = 250  # B - #a78bfa
    glow_data[..., 3] = (glow_alpha_data * glow_intensity).astype(np.uint8)  # A

    glow = Image.fromarray(glow_data)

    # Composite original over glow
    result = Image.alpha_composite(glow, img)

    return result

def invert_colors(img):
    """
    Invert RGB colors while preserving alpha channel
    """
    img = img.convert('RGBA')
    data = np.array(img)

    # Extract alpha channel
    alpha = data[..., 3]

    # Invert RGB channels where alpha > 0
    data[..., 0] = np.where(alpha > 0, 255 - data[..., 0], 0)  # R
    data[..., 1] = np.where(alpha > 0, 255 - data[..., 1], 0)  # G
    data[..., 2] = np.where(alpha > 0, 255 - data[..., 2], 0)  # B

    return Image.fromarray(data)

def convert_to_white(img):
    """
    Convert all colored pixels to white while preserving alpha channel
    """
    img = img.convert('RGBA')
    data = np.array(img)

    # Extract alpha channel
    alpha = data[..., 3]

    # Set all RGB channels to white where alpha > 0
    data[..., 0] = np.where(alpha > 0, 255, 0)  # R
    data[..., 1] = np.where(alpha > 0, 255, 0)  # G
    data[..., 2] = np.where(alpha > 0, 255, 0)  # B

    return Image.fromarray(data)

def extract_white_pixels(img, threshold=200):
    """
    Keep only near-white pixels and make everything else transparent
    Useful for logos that are white on a colored or dark background
    """
    img = img.convert('RGBA')
    data = np.array(img)

    # Get RGB channels
    r, g, b, a = data.T

    # Find NON-white areas (any RGB value below threshold)
    # We use .T because numpy arrays are indexed [y, x, c] but we transposed earlier
    non_white_areas = (r < threshold) | (g < threshold) | (b < threshold)

    # Set alpha to 0 for non-white areas
    data[..., 3] = np.where(non_white_areas.T, 0, 255)

    return Image.fromarray(data)

def process_image(input_path, output_path, outline_width=3, remove_bg=True,
                  bg_threshold=240, add_glow=False, glow_radius=5,
                  convert_white=False, purple_glow=False, invert=False,
                  keep_only_white=False):
    """
    Main processing function
    """
    print(f"Processing: {input_path}")

    # Load image
    img = Image.open(input_path)

    # Specific logic for keeping only white pixels (prioritizes this over background removal)
    if keep_only_white:
        print("  - Extracting only white pixels...")
        img = extract_white_pixels(img, threshold=bg_threshold)
    elif remove_bg:
        print("  - Removing background...")
        img = remove_background_simple(img, threshold=bg_threshold)
    else:
        img = img.convert('RGBA')

    # Invert colors if requested (before converting to white)
    if invert:
        print("  - Inverting colors...")
        img = invert_colors(img)

    # Convert to white if requested
    if convert_white:
        print("  - Converting all colors to white...")
        img = convert_to_white(img)

    # Add white outline
    if outline_width > 0:
        print(f"  - Adding {outline_width}px white outline...")
        img = add_white_outline(img, outline_width=outline_width)

    # Add glow effect if requested
    if purple_glow:
        print(f"  - Adding purple glow effect (radius={glow_radius})...")
        img = add_purple_glow(img, glow_radius=glow_radius)
    elif add_glow:
        print(f"  - Adding white glow effect (radius={glow_radius})...")
        img = add_white_glow(img, glow_radius=glow_radius)

    # Save result
    img.save(output_path, 'PNG')
    print(f"  [OK] Saved to: {output_path}")

    return img

def batch_process_logos():
    """
    Batch process all logos in images/logos/ folder
    """
    logos_dir = "images/logos"

    if not os.path.exists(logos_dir):
        print(f"Error: {logos_dir} directory not found!")
        return

    # Get all image files in logos directory
    image_files = []
    for ext in ['*.jpg', '*.jpeg', '*.png']:
        image_files.extend([f for f in os.listdir(logos_dir) if f.lower().endswith(ext[1:])])

    if not image_files:
        print(f"No image files found in {logos_dir}")
        return

    print("=" * 60)
    print("Batch Logo Converter: White + Purple Glow")
    print("=" * 60)
    print(f"\nFound {len(image_files)} logos to process\n")

    for i, filename in enumerate(sorted(image_files), 1):
        # Skip results of previous runs
        if filename.endswith("-white-purple.png") or filename.endswith("-white-purple-white-purple.png"):
            continue

        input_path = os.path.join(logos_dir, filename)
        # Create output filename
        name_without_ext = os.path.splitext(filename)[0]
        output_filename = f"{name_without_ext}-white-purple.png"
        output_path = os.path.join(logos_dir, output_filename)

        print(f"[{i}/{len(image_files)}] Processing: {filename}")

        try:
            # Look for specific horizontal logo
            is_horizontal_logo = 'bridges' in filename.lower() and 'horizontal' in filename.lower()
            # Special handling for black logos (like Bridges square)
            do_invert = 'black' in filename.lower() and 'transparent' in filename.lower()
            
            process_image(
                input_path,
                output_path,
                outline_width=0,
                remove_bg=not is_horizontal_logo,
                bg_threshold=220 if is_horizontal_logo else 240,
                convert_white=not (do_invert or is_horizontal_logo), # If we invert/extract white, it's already white
                purple_glow=True,
                glow_radius=10,
                invert=do_invert,
                keep_only_white=is_horizontal_logo
            )
        except Exception as e:
            print(f"  [ERROR] Failed to process {filename}: {str(e)}")

        print()  # Add spacing between logos

    print("=" * 60)
    print("[SUCCESS] Batch processing complete!")
    print("=" * 60)
    print(f"\nProcessed {len(image_files)} logos")
    print(f"Output directory: {logos_dir}")
    print("\nAll logos converted to white with purple glow!")

def main():
    """
    Process UT logo with white outline
    """
    input_file = "images/ut-logo.png"
    output_file = "images/ut-logo-outlined.png"

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return

    print("=" * 60)
    print("Image Converter: White Outline")
    print("=" * 60)

    # Convert to white with purple glow (recommended for dark site)
    print("\n[1] White logo with purple glow (RECOMMENDED)")
    output_white_purple = output_file.replace('.png', '-white-purple.png')
    process_image(
        input_file,
        output_white_purple,
        outline_width=0,
        remove_bg=False,
        convert_white=True,
        purple_glow=True,
        glow_radius=10
    )

    print("\n[2] White logo with white glow")
    output_white_glow = output_file.replace('.png', '-white-glow.png')
    process_image(
        input_file,
        output_white_glow,
        outline_width=0,
        remove_bg=False,
        convert_white=True,
        add_glow=True,
        glow_radius=8
    )

    print("\n[3] White logo with outline + purple glow")
    output_white_outline = output_file.replace('.png', '-white-outline.png')
    process_image(
        input_file,
        output_white_outline,
        outline_width=2,
        remove_bg=False,
        convert_white=True,
        purple_glow=True,
        glow_radius=8
    )

    print("\n[4] Original orange with purple glow")
    output_orange_purple = output_file.replace('.png', '-orange-purple.png')
    process_image(
        input_file,
        output_orange_purple,
        outline_width=0,
        remove_bg=False,
        purple_glow=True,
        glow_radius=10
    )

    print("\n" + "=" * 60)
    print("[SUCCESS] Processing complete!")
    print("=" * 60)
    print("\nGenerated files:")
    print(f"  1. {output_white_purple} (white + purple glow - RECOMMENDED)")
    print(f"  2. {output_white_glow} (white + white glow)")
    print(f"  3. {output_white_outline} (white + outline + purple glow)")
    print(f"  4. {output_orange_purple} (original color + purple glow)")
    print("\nThe purple glow matches your site's accent color (#a78bfa)!")

if __name__ == "__main__":
    # Check if PIL/Pillow is installed
    try:
        import PIL
        import numpy
    except ImportError:
        print("Error: Required libraries not installed.")
        print("\nPlease install with:")
        print("  pip install Pillow numpy")
        sys.exit(1)

    # Check if --batch flag is provided
    if len(sys.argv) > 1 and sys.argv[1] == "--batch":
        batch_process_logos()
    else:
        main()
