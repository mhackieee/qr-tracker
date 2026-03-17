import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def generate_qr(envelope_id, out_dir='qr_output'):
    os.makedirs(out_dir, exist_ok=True)
    qr = qrcode.QRCode(box_size=6, border=2)
    qr.add_data(envelope_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    w, h = img.size
    new_img = Image.new('RGB', (w, h+30), 'white')
    new_img.paste(img, (0,0))
    draw = ImageDraw.Draw(new_img)
    font = ImageFont.load_default()
    draw.text((5,h+5), envelope_id, fill='black', font=font)
    out_path = os.path.join(out_dir, f"{envelope_id}.png")
    new_img.save(out_path)
    return out_path

if __name__ == "__main__":
    for i in range(1,21):
        eid = f"ENV-2026-{i:04d}"
        generate_qr(eid)
    print("Generated sample QR codes in qr_output/")
