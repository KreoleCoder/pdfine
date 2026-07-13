
def pdfs_compressor(compress):
    compress_level = 6 #Set the level of compression 0-9
    img_quality = 10 #Define the quality of images 0-100

    for page in compress.pages:
        for img in page.images:
            img.replace(img.image, quality=img_quality)
        page.compress_content_streams(level=compress_level)
