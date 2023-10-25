# GCodeTestGUI



GCodeTestGUI is a simple GUI application built with Streamlit that generates lines of G-code (G01) for patterns of motion to facilitate testing and calibrating the X-Y motion of a 3D printer. This tool allows you to create custom G-code sequences for fine-tuning your 3D printer's movements. Used for course activities in IMEC 3501.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Customizable G-code generation**: Create custom patterns of motion by specifying printing bed parameters.
- **Visual representation**: Visualize the generated G-code motion pattern on the GUI for better understanding.
- **Export G-code**: Generate G-code lines and send directly to the 3D printer.
- **User-friendly interface**: Built using Streamlit, a user-friendly Python framework, making it easy to use even for beginners.

## Getting Started

Follow these instructions to get GCodeTestGUI up and running on your local machine.

### Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Python (3.8 or higher)
- pip (Python package manager)

### Installation

1. Create a virtual environment (recommended) to manage dependencies:
    
   ```bash
    python -m venv gcodeenv
    gcodeenv\Scripts\activate
    ```
2. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/GCodeTestGUI.git
    ```
3. Navigate to the project directory and install requirements

   ```bash
   cd GCodeTestGUI
   pip install -r requirements.txt
    ```

### Usage

To start the GCodeTestGUI application, run the following command in your terminal within the project directory.

   ```bash
   streamlit run GUI.py
   ```

This will start the Streamlit development server and open the application in your default web browser. Use the user interface to specify the parameters for your G-code pattern and generate the desired motion sequences. Visualize the pattern and export the generated G-code for use with your 3D printer.