```markdown
# Audio Tuner (音频调谐器)

A real‑time instrument tuning tool that detects musical frequencies through your microphone.

## Overview

Audio Tuner captures environmental sounds via microphone, performs FFT analysis, and identifies the strongest frequency components. It maps each frequency to the nearest musical note (e.g., A4 = 440 Hz) and displays the relative intensity of the top 7 components. A built‑in noise gate suppresses low‑level background noise, providing a clean, continuously updating display ideal for tuning musical instruments.

## Features

- 🎤 **Real‑time analysis**: Capture audio from the default microphone and analyse frequency content on the fly.
- 🎯 **Multi‑frequency detection**: Show the 7 most prominent frequencies with their corresponding note names and octaves.
- 📊 **Intensity visualisation**: Display each frequency’s relative strength as a percentage bar.
- 🔇 **Noise gate**: Automatically ignore audio input when the overall level is below 60 % (RMS‑based), reducing flickering in quiet environments.
- 🖥️ **Clean interface**: Clears the terminal on each update for a smooth, readable visualisation.

## Tech Stack

- **Language**: Python 3.6+
- **Core libraries**: PyAudio (PortAudio binding), NumPy
- **Signal processing**: FFT with a Hamming window, RMS intensity measurement

## Project Structure

```
.
├── README.md       # This file
└── Tuner.py        # Main application script
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- PortAudio development libraries (required by PyAudio on Linux)
- A working microphone

### Installation

1. **Install Python dependencies**
   ```bash
   pip install pyaudio numpy
   ```

2. **Linux users – install PortAudio**
   ```bash
   sudo apt-get install portaudio19-dev
   ```
   macOS and Windows users typically get the required libraries automatically with the `pyaudio` pip package.

### Configuration

No configuration file or environment variables are needed. The script uses the default system microphone and internal parameters optimised for musical tuning:

| Parameter         | Value       |
|-------------------|-------------|
| Sample rate       | 44 100 Hz   |
| Chunk size        | 32 768 samples |
| Noise gate threshold | 60 % RMS intensity |
| Frequency range   | 20 Hz – 20 000 Hz |

### Running the Project

Start the tuner from the terminal:

```bash
python Tuner.py
```

The application will begin listening immediately. Press `Ctrl+C` to stop.

## Usage

Once running, you will see a live view of the top 7 frequencies and their strengths, for example:

```
频率 1:   440 Hz (A4) | 相对强度:  98%
频率 2:   880 Hz (A5) | 相对强度:  45%
...
```

- When the environment is quiet (below the noise gate), the output will pause and show the last valid detection.
- The display clears and refreshes in place, giving a stable view even on standard terminals.

Use this while tuning an instrument: play a note and observe the detected fundamental and overtones.

## Testing

This repository does not include automated tests at this time.  
To manually verify behaviour, run the script and check that frequencies from a known source (e.g., a tuning fork at 440 Hz) are correctly identified.

## Contributing

Contributions, bug reports, and feature requests are welcome.  

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-idea`).
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

Please follow common Python coding conventions and test your changes before submitting.

## License

License information was not found in this repository.  
If you are the author, consider adding a `LICENSE` file to clarify usage terms.
```