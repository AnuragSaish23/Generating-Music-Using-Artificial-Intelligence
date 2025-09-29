# Generating-Music-Using-Artificial-Intelligence
A Music Information Retrieval (MIR) project implementing recommendation, classification, content-based retrieval, transcription, and AI-based music generation using L-Systems, Cellular Automata, and Markov Chains

### Project Overview
This project demonstrates algorithmic music generation using AI techniques. It focuses on creating melodies, drum patterns, and chord progressions using:

- **L-Systems** → For chord progression generation.
- **Markov Chains** → For melody generation.
- **Cellular Automata** → For drum pattern generation.

The outputs are generated in MIDI and MusicXML formats and can be visualized in MuseScore or other music software.

### Folder Structure

```text
Generating-Music-Using-Artificial-Intelligence/
│
├── src/ # Source code modules
│ ├── piano_generation/ # L-System chord generation
│ ├── cellular_automata/ # Drum pattern generation
│
├── results/ # Generated music outputs (MIDI, MusicXML)
|
├── images/ # Screenshots, diagrams, piano rolls
|
|── notebooks/ # Jupyter notebooks for experiments
├
|── requirements.txt # Project dependencies
|
└── README.md # Project overview and instructions
```

### Installation 

**1.Clone the repository**
git clone https://github.com/AnuragSaish23/Generating-Music-Using-Artificial-Intelligence.git
cd Generating-Music-Using-Artificial-Intelligence

**2.Install Dependencies**
pip install -r requirements.txt

**3.Set up MuseScore Path**
from music21 import environment
environment.set('musicxmlPath', r'D:/MuseScore/bin/MuseScore4.exe')

### How The Project Works 

**1. L-Systems (Chord Progression)**

- Generates sequences of chords based on an axiom and production rules.
- Converts generated sequences into music21 chord objects.
- Exports the output as MusicXML to view in MuseScore.

Example:
- Axiom: A
- Rules: A → ABC, B → BA, C → E
- Output: Chord progression like Cmaj → Dmin → E → …

**2. Markov Chains (Melody Generation)**

- Trains on sequences of notes (pitch + duration).
- Uses a transition matrix to generate melodies probabilistically.
- Converts generated notes into music21 streams.
- Output can be viewed as MusicXML or MIDI.

**3. Cellular Automata (Drum Patterns)**

- Generates drum patterns for instruments: Kick, Snare, Hi-Hat, Clap.
- Uses rules for syncopation, filling gaps, accenting, and mutation.
- Converts patterns into music21 streams and exports to MIDI.
- Optional random fills can be added for variation.

#### Author
**Anurag Saish - Manipal University Jaipur - B.Tech Computer Science Engineerg 2026**
