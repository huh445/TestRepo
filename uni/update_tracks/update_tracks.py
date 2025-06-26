import eyed3
import os

def sanitize_filename(name):
    # Replace invalid filename characters
    return "".join(c for c in name if c.isalnum() or c in " ._-").rstrip()

def get_track_info(file_path):
    audio = eyed3.load(file_path)
    if not audio or not audio.tag:
        return None, None

    track_num = audio.tag.track_num[0] if audio.tag.track_num else None
    title = audio.tag.title if audio.tag.title else None

    return track_num, title

def rename_mp3s(folder_path):
    print(f"\nScanning folder: {folder_path}")
    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(".mp3"):
            print(f"Skipping non-MP3: {filename}")
            continue

        full_path = os.path.join(folder_path, filename)
        print(f"Processing: {filename}")

        track_num, title = get_track_info(full_path)

        if track_num is None or title is None:
            print(f"❌ Skipping {filename}: missing track number or title.")
            continue

        title_clean = sanitize_filename(title)
        new_filename = f"{track_num}. {title_clean}.mp3"
        new_path = os.path.join(folder_path, new_filename)

        if os.path.exists(new_path):
            print(f"⚠️  Skipping rename: {new_filename} already exists.")
            continue

        os.rename(full_path, new_path)
        print(f"✅ Renamed: {filename} → {new_filename}")


# === USAGE ===
if __name__ == "__main__":
    folder = input("Enter the path to your folder of MP3s: ").strip('"')
    rename_mp3s(folder)