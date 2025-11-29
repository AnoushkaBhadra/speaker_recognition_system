import os
import shutil
from pathlib import Path
#configurationp settings
SOURCE_DIR = "audio_clips"
SPEAKERS = ["Anoushka", "Ayushman", "Saumi"]  #original file names
SPEAKER_LABELS = ["anoushka", "ayushman","saumi"]  

#Directory structure 
DIRS_TO_CREATE = {
    "data/processed/anoushka", 
    "data/processed/ayushman", 
    "data/processed/saumi", 
    "data/features", 
    "models", 
    "notebooks"
}

def create_directories():
    print("Creating directory structure...")
    for dir_path in DIRS_TO_CREATE:
        Path(dir_path).mkdir(parents= True, exist_ok = True)
        print(f" Created: {dir_path}")

    print()

def organize_audio_files():
    """Copy and rename audio files uniformly"""
    print("Organizing audio files...")
    
    if not os.path.exists(SOURCE_DIR):
        print(f"ERROR: '{SOURCE_DIR}' folder not found!")
        print("Make sure you run this script from the project root directory.")
        return False
    
    summary = {}
    for original_name, label in zip(SPEAKERS, SPEAKER_LABELS):
        source_path = os.path.join(SOURCE_DIR, original_name)
        dest_path = os.path.join("data/processed", label)
        if not os.path.exists(source_path):
            print(f"  ⚠ WARNING: Folder '{original_name}' not found in {SOURCE_DIR}")
            continue

        wav_files = [f for f in os.listdir(source_path) if f.lower().endswith('.wav')]
        
        if not wav_files:
            print(f"  ⚠ WARNING: No .wav files found in '{original_name}'")
            continue
        wav_files.sort()

        copied_count = 0
        for idx, filename in enumerate(wav_files, 1):
            source_file = os.path.join(source_path, filename)
            new_filename = f"{label}_{idx:03d}.wav"  # e.g., anoushka_001.wav
            dest_file = os.path.join(dest_path, new_filename)
            
            shutil.copy2(source_file, dest_file)
            copied_count += 1
        
        summary[label] = copied_count
        print(f"  ✓ {original_name} → {copied_count} files copied to '{label}/'")
    
    print()
    return summary

def print_summary(summary):
    """Print organization summary"""
    print("=" * 50)
    print("SETUP COMPLETE!")
    print("=" * 50)
    print("\nAudio files organized:")
    total = 0
    for speaker, count in summary.items():
        print(f"  • {speaker}: {count} clips")
        total += count
    print(f"\nTotal: {total} audio clips")
    print("\nDirectory structure created:")
    print("  • data/processed/  - Organized audio files")
    print("  • data/features/   - For extracted features")
    print("  • models/          - For trained models")
    print("  • notebooks/       - For your .ipynb file")
    print("\n✓ Ready to start coding!")
    print("=" * 50)

def main():
    print("=" * 50)
    print("SPEAKER RECOGNITION PROJECT SETUP")
    print("=" * 50)
    print()
    

    create_directories()
    summary = organize_audio_files()
    if summary:
        print_summary(summary)
    else:
        print("\nSetup incomplete. Please check the errors above.")

if __name__ == "__main__":
    main()