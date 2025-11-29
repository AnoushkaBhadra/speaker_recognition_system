# Speaker Recognition System

This repository contains code and notebooks for a small speaker recognition project (3 speakers). The project includes scripts to organize audio files, extract features, train an SVM speaker classifier, and test external clips.

## Quick overview
- `setup_project.py` — creates the directory structure and copies/renames audio files from `audio_clips/` into `data/processed/{speaker}/`.
- `notebooks/cleaned_ver.ipynb` — cleaned notebook for feature extraction, model training, evaluation and testing.
- `notebooks/speaker_recognition.ipynb` — (interactive) notebook with utilities and test helpers.

## Clone the repository
Open PowerShell and run:

```powershell
git clone https://github.com/AnoushkaBhadra/speaker_recognition_system.git
cd speaker_recognition_system
```

## Create a Python virtual environment (Windows PowerShell)
Run these commands from the repository root:

```powershell
# create virtual environment
python -m venv venv

# activate the virtual environment
venv\Scripts\Activate

# install required packages (minimal set used in the notebooks)
python -m pip install --upgrade pip
python -m pip install numpy librosa matplotlib seaborn scikit-learn pandas soundfile
```

Note: If you have a `requirements.txt` file, replace the install line with `python -m pip install -r requirements.txt`.

## Run `setup_project.py`
`setup_project.py` prepares the project directory structure and copies audio files into `data/processed/`.

Steps:

1. Ensure your original audio directories are in `audio_clips/` (project root). The expected folders are `Anoushka/`, `Ayushman/`, `Saumi/` (or update `setup_project.py` constants).

The original audio clip folder structure should be like this: 
```
your_project_folder/
└── audio_clips/
    ├── Anoushka/
    │   ├── rec_3.wav
    │   ├── rec_3_2.wav
    │   └── ... (60 total clips)
    ├── Ayushman/
    │   ├── record_out(1).wav
    │   ├── record_out(2).wav
    │   └── ... (60 total clips)
    └── Saumi/
        ├── clip1.wav
        ├── recording_2.wav
        └── ... (60 total clips)
```

Important:

- ach speaker should have their own folder inside audio_clips/
- Folder names should match the speaker names (case-sensitive)
- Audio files can have ANY names - the setup script will rename them
- Supported format: .wav files (recommended: 16kHz sample rate)

Note: Even if the sample files are not of 16kHz, the model will downsample it to 16000 Hz

2. From the project root (PowerShell activated venv):

```powershell
python setup_project.py
```

What `setup_project.py` does:
- Creates output directories under `data/processed/` and `data/features/`, and `models/` if they don't exist.
- Copies `.wav` files from `audio_clips/<OriginalName>/` into `data/processed/<label>/` and renames them using a consistent convention (e.g. `anoushka_001.wav`).
- Prints a summary with counts for each speaker.

If the script warns that some folders are missing, confirm the folder names inside `audio_clips/` and update `setup_project.py` constants at the top if necessary.

## Running the notebook `cleaned_ver.ipynb`
Open the notebook after activating the virtual environment:

```powershell
# From repo root with venv activated
jupyter notebook notebooks/cleaned_ver.ipynb
```

Recommended workflow inside `cleaned_ver.ipynb`:
1. Run the setup / import cells to load libraries.
2. Run the data-loading cell to read audio from `data/processed/`.
3. Run feature extraction cells and training cells in order. Notebooks usually expect you to run cells sequentially.
4. Use the testing cells to test external clips (drop them into `test_folder/` and run the testing cell. Create `test_folder/` in the root directory if not already present.).

## Notes & troubleshooting
- If a test clip is misclassified, first check recording quality: background noise, clipping, or different microphone/sampling rate often cause mismatches. Re-recording in similar conditions as training usually fixes it.
- The notebook uses a `CONFIDENCE_THRESHOLD` to detect unknown speakers. If you want the predicted label to always show the speaker with the highest probability, update the `predict_speaker` logic (already adjusted in `speaker_recognition.ipynb` in this repo).
- If you add new audio files, re-run feature extraction and retrain the model in the notebook.
- If packages fail to install, ensure you have a supported Python version (3.8+ recommended) and internet access from the environment.

## Where outputs are saved
- Extracted features: `data/features/X_features.npy`, `data/features/y_labels.npy`
- Trained model and preprocessors: `models/svm_model.pkl`, `models/scaler.pkl`, `models/label_encoder.pkl`
- Test results CSV (from notebook runs): `testing_results.csv` (project root)

---
