import instaloader
import os
from PIL import Image
from fpdf import FPDF
import requests

loader = instaloader.Instaloader()

post_url = input("Enter the Instagram post URL: ")

shortcode = post_url.split("/")[-2]

post = instaloader.Post.from_shortcode(loader.context, shortcode)

def download_carousel_as_pdf(post, target_folder):
    pdf = FPDF()
    sidecar_nodes = list(post.get_sidecar_nodes())
    total_slides = len(sidecar_nodes)

    for index, slide in enumerate(sidecar_nodes):
        if slide.is_video:
            print("Carousel contains videos, which cannot be added to PDF. Skipping video.")
            continue
        image_url = slide.display_url
        image_path = os.path.join(target_folder, f"slide_{index}.jpg")
        
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            print(f"Downloaded slide {index + 1} of {total_slides}")
        else:
            print(f"Failed to download slide {index + 1}. Status code: {response.status_code}")
            continue

        try:
            img = Image.open(image_path)
            img = img.convert('RGB') 
            pdf.add_page()
            pdf.image(image_path, x=10, y=10, w=190) 
            img.close() 
        except Exception as e:
            print(f"Error processing slide {index + 1}: {e}")
        finally:
            os.remove(image_path) 

    pdf.output(os.path.join(target_folder, f"{post.owner_username}_{shortcode}.pdf"))
    print(f"Carousel downloaded as PDF: {post.owner_username}_{shortcode}.pdf")

def download_image_as_png(post, target_folder):
    image_url = post.url
    image_path = os.path.join(target_folder, f"{post.owner_username}_{shortcode}.png")
    
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Image downloaded as PNG: {post.owner_username}_{shortcode}.png")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

def download_video_as_mp4(post, target_folder):
    if not post.is_video:
        print("This post is not a video.")
        return
    video_url = post.video_url
    video_path = os.path.join(target_folder, f"{post.owner_username}_{shortcode}.mp4")
    
    response = requests.get(video_url, stream=True)
    if response.status_code == 200:
        with open(video_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Video downloaded as MP4: {post.owner_username}_{shortcode}.mp4")
    else:
        print(f"Failed to download video. Status code: {response.status_code}")

target_folder = f"{post.owner_username}_{shortcode}"
os.makedirs(target_folder, exist_ok=True)

if post.typename == 'GraphSidecar':
    download_carousel_as_pdf(post, target_folder)
elif post.typename == 'GraphImage':
    download_image_as_png(post, target_folder)
elif post.typename == 'GraphVideo': 
    download_video_as_mp4(post, target_folder)
else:
    print("Unsupported post type.")