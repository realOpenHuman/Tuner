# Audio Tuner

A real-time instrument tuning tool that analyzes audio from your microphone and displays the most prominent musical notes and their intensities.

## Overview

Audio Tuner captures live audio, performs FFT analysis, and identifies the strongest frequency components. It then maps those frequencies to the nearest musical notes (e.g., A4 = 440 Hz) and visualizes the relative strength of the top 7 components. A built-in noise gate prevents jittery output in quiet environments, making it ideal for tuning guitars, pianos, or any acoustic instrument.

## Features

- 🎤 **Real‑time audio analysis** – reads from the default microphone and updates continuously  
- 🎯 **Multi‑frequency detection** – shows the 7 most dominant frequencies, each labelled with its note name and octave  
- 📊 **Intensity visualization** – displays each frequency’s strength as a percentage bar  
- 🔇 **Noise gate** – automatically suppresses faint background noise (threshold: 60 % RMS intensity)  
- 🖥️ **Clean, live interface** – clears the terminal on every update for a smooth, flicker‑free display  

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.6+ | Core language |
| PyAudio | Microphone input (PortAudio wrapper) |
| NumPy | FFT, windowing, and numerical processing |

## Project Structure

```
.
├── README.md       # This file
└── Tuner.py        # Main application script
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- PortAudio development libraries (required by PyAudio on Linux; macOS and Windows users usually get them automatically with the `pyaudio` package)
- A working microphone

### Installation

1. **Install Python dependencies**
   ```bash
   pip install pyaudio numpy
   ```

2. **Linux users: install PortAudio**
   ```bash
   sudo apt-get install portaudio19-dev
   ```

### Configuration

No configuration files or environment variables are needed. The script uses the following internal parameters, tuned for musical instrument detection:

| Parameter          | Value                |
|--------------------|----------------------|
| Sample rate        | 44 100 Hz           |
| Chunk size         | 32 768 samples       |
| Noise gate threshold | 60 % RMS intensity |
| Frequency range    | 20 Hz – 20 000 Hz    |

### Running the Project

From the terminal, start the tuner:

```bash
python Tuner.py
```

The application begins monitoring immediately. Press `Ctrl+C` to exit.

## Usage

When the tuner is running, you will see a live view similar to:

```
频率 1:   440 Hz (A4) | 相对强度:  98%
频率 2:   880 Hz (A5) | 相对强度:  45%
...
```

- In a quiet environment (below the noise gate), the last valid detection is displayed with a “quiet environment” notice.
- The output clears and refreshes in place, providing a stable view even on standard terminals.

While tuning an instrument, play a single note and observe the detected fundamental and overtones.

## Testing

This repository does not currently include automated tests.  
To manually verify functionality, run the script and check whether a known frequency source (e.g., a 440 Hz tuning fork) is correctly identified.

## Contributing

Contributions, bug reports, and feature requests are welcome.  

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/your-idea`)  
3. Commit your changes  
4. Push the branch  
5. Open a pull request  

Please follow common Python coding conventions and test your changes locally before submitting.

## License

License information was not found in this repository.  
If you are the author, consider adding a `LICENSE` file to clarify usage terms.