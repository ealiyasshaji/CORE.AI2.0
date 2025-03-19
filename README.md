# CORE.AI2.0
STREAMLIT HACKATHON
# Arduino Who-Know?

A comprehensive web application built with Streamlit that serves as an interactive guide to Arduino circuit boards and microcontrollers.

![Arduino Who-Know? Screenshot](https://i.imgur.com/tOJYhQG.png)

## 🔌 Overview

Arduino Who-Know? is an interactive web application designed to help makers, students, and electronics enthusiasts explore and learn about different Arduino boards. The application features a sleek red and black theme and provides detailed information about various Arduino boards, their components, specifications, and compatible modules.

## ✨ Features

- **Interactive Board Selection**: Choose from multiple Arduino boards through an easy-to-use sidebar.
- **Comprehensive Information**: Access detailed specifications, component breakdowns, and compatibility data.
- **Visual Representation**: View high-quality images of each Arduino board.
- **Organized Interface**: Information is neatly organized in tabs for easy navigation.
- **Board Comparison**: Compare specifications across different Arduino boards to find the right one for your project.
- **Responsive Design**: Enjoy a seamless experience on different screen sizes.

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/arduino-who-know.git
   ```

2. Navigate to the project directory:
   ```bash
   cd arduino-who-know
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Run the Streamlit app with the following command:
```bash
streamlit run app.py
```

The application should automatically open in your default web browser. If not, you can access it at `http://localhost:8501`.

## 📁 Project Structure

```
arduino-who-know/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
└── README.md              # This file
```

## 📋 Available Arduino Boards

The application currently includes detailed information about:

- Arduino UNO
- Arduino Nano
- Arduino Mega
- Arduino Leonardo
- Arduino Due

## 🧩 How It Works

The application uses a Python dictionary to store all the information about different Arduino boards. When a user selects a board from the sidebar, the application retrieves the information and displays it in an organized manner using Streamlit's interface components.

The custom CSS provides a sleek red and black theme that enhances the user experience and reflects the Arduino brand aesthetics.

## 🔧 Customization

### Adding More Arduino Boards

To add a new Arduino board, simply extend the `arduino_boards` dictionary in `app.py` with a new entry following the established pattern:

```python
"New Arduino Board": {
    "image": "URL_to_image",
    "intro": "Brief introduction",
    "microcontroller": "MCU type",
    # Add all other required fields
}
```

### Modifying the Theme

You can customize the color theme by editing the CSS in the `apply_custom_css()` function in `app.py`.

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Requirements

Create a `requirements.txt` file in your project directory with the following dependencies:

```
streamlit>=1.8.0
pandas>=1.3.0
pillow>=8.0.0
```

## 🙏 Acknowledgements

- [Arduino](https://www.arduino.cc/) for creating amazing open-source hardware
- [Streamlit](https://streamlit.io/) for making it easy to create data apps in Python

## 📞 Contact

If you have any questions or feedback, please open an issue on this repository or contact [your-email@example.com].

---

Happy coding and tinkering with Arduino boards! 🤖
