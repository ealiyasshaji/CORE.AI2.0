import streamlit as st
import pandas as pd
from PIL import Image
import base64
import io

# Set page configuration
st.set_page_config(
    page_title="ARDUINO WHO-KNOW?",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for red and black theme
def apply_custom_css():
    st.markdown("""
    <style>
        .main {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        .stButton button {
            background-color: #E51B23;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 0.5rem 1rem;
        }
        .stButton button:hover {
            background-color: #B71C1C;
        }
        .stSelectbox label, .stSelectbox div[data-baseweb="select"] {
            color: #FFFFFF;
        }
        h1, h2, h3 {
            color: #E51B23;
        }
        .stTabs [data-baseweb="tab-list"] {
            background-color: #2D2D2D;
        }
        .stTabs [data-baseweb="tab"] {
            color: #FFFFFF;
        }
        .stTabs [aria-selected="true"] {
            background-color: #E51B23;
        }
        .stDataFrame {
            background-color: #2D2D2D;
        }
        .css-1oe6wy4 {
            color: #FFFFFF;
        }
    </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# Arduino boards data
arduino_boards = {
    "Arduino UNO": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000066_front_1_1.jpg",
        "intro": "The Arduino UNO is the most popular Arduino board, perfect for beginners and experienced makers alike.",
        "microcontroller": "ATmega328P",
        "operating_voltage": "5V",
        "input_voltage": "7-12V",
        "digital_pins": "14 (of which 6 provide PWM output)",
        "analog_pins": "6",
        "flash_memory": "32 KB (ATmega328P) of which 0.5 KB used by bootloader",
        "sram": "2 KB (ATmega328P)",
        "eeprom": "1 KB (ATmega328P)",
        "clock_speed": "16 MHz",
        "dimensions": "68.6 x 53.4 mm",
        "weight": "25g",
        "compatible_modules": [
            "LED Matrix", "Relay Module", "Bluetooth Module", "WiFi Module", 
            "LCD Display", "Servo Motors", "Ultrasonic Sensor", "Temperature Sensor"
        ],
        "components": {
            "ATmega328P": "Main microcontroller that runs your code",
            "16 MHz Crystal Oscillator": "Provides clock timing for the microcontroller",
            "USB Port": "For power and programming",
            "Power Jack": "Alternative power input",
            "ICSP Header": "For programming the bootloader",
            "Reset Button": "Resets the board",
            "Power LED": "Indicates when the board is powered",
            "TX/RX LEDs": "Indicate serial communication",
            "Voltage Regulator": "Regulates input voltage to 5V"
        }
    },
    "Arduino Nano": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000005_front_8.jpg",
        "intro": "The Arduino Nano is a compact board perfect for projects where space is limited.",
        "microcontroller": "ATmega328P",
        "operating_voltage": "5V",
        "input_voltage": "7-12V",
        "digital_pins": "14 (of which 6 provide PWM output)",
        "analog_pins": "8",
        "flash_memory": "32 KB (ATmega328P) of which 2 KB used by bootloader",
        "sram": "2 KB (ATmega328P)",
        "eeprom": "1 KB (ATmega328P)",
        "clock_speed": "16 MHz",
        "dimensions": "45 x 18 mm",
        "weight": "7g",
        "compatible_modules": [
            "LED Matrix", "Relay Module", "Bluetooth Module", "WiFi Module", 
            "LCD Display", "Servo Motors", "Ultrasonic Sensor", "Temperature Sensor"
        ],
        "components": {
            "ATmega328P": "Main microcontroller that runs your code",
            "16 MHz Crystal Oscillator": "Provides clock timing for the microcontroller",
            "Mini-B USB Port": "For power and programming",
            "ICSP Header": "For programming the bootloader",
            "Reset Button": "Resets the board",
            "Power LED": "Indicates when the board is powered",
            "TX/RX LEDs": "Indicate serial communication",
            "Voltage Regulator": "Regulates input voltage to 5V"
        }
    },
    "Arduino Mega": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000067_front.jpg",
        "intro": "The Arduino Mega is a more powerful board with more pins and memory, perfect for complex projects.",
        "microcontroller": "ATmega2560",
        "operating_voltage": "5V",
        "input_voltage": "7-12V",
        "digital_pins": "54 (of which 15 provide PWM output)",
        "analog_pins": "16",
        "flash_memory": "256 KB (ATmega2560) of which 8 KB used by bootloader",
        "sram": "8 KB (ATmega2560)",
        "eeprom": "4 KB (ATmega2560)",
        "clock_speed": "16 MHz",
        "dimensions": "101.52 x 53.3 mm",
        "weight": "37g",
        "compatible_modules": [
            "LED Matrix", "Relay Module", "Bluetooth Module", "WiFi Module", 
            "LCD Display", "Servo Motors", "Ultrasonic Sensor", "Temperature Sensor",
            "GPS Module", "SD Card Module", "Camera Module", "Stepper Motor Driver",
            "CNC Shield", "3D Printer Controller"
        ],
        "components": {
            "ATmega2560": "Main microcontroller that runs your code",
            "16 MHz Crystal Oscillator": "Provides clock timing for the microcontroller",
            "USB Port": "For power and programming",
            "Power Jack": "Alternative power input",
            "ICSP Header": "For programming the bootloader",
            "Reset Button": "Resets the board",
            "Power LED": "Indicates when the board is powered",
            "TX/RX LEDs": "Indicate serial communication",
            "Voltage Regulator": "Regulates input voltage to 5V"
        }
    },
    "Arduino Leonardo": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000057_front_1.jpg",
        "intro": "The Arduino Leonardo is the first Arduino board with built-in USB communication, eliminating the need for a secondary processor.",
        "microcontroller": "ATmega32U4",
        "operating_voltage": "5V",
        "input_voltage": "7-12V",
        "digital_pins": "20 (of which 7 provide PWM output)",
        "analog_pins": "12",
        "flash_memory": "32 KB (ATmega32U4) of which 4 KB used by bootloader",
        "sram": "2.5 KB (ATmega32U4)",
        "eeprom": "1 KB (ATmega32U4)",
        "clock_speed": "16 MHz",
        "dimensions": "68.6 x 53.3 mm",
        "weight": "28g",
        "compatible_modules": [
            "LED Matrix", "Relay Module", "Bluetooth Module", "WiFi Module", 
            "LCD Display", "Servo Motors", "Ultrasonic Sensor", "Temperature Sensor",
            "Keyboard Emulation", "Mouse Emulation", "MIDI devices"
        ],
        "components": {
            "ATmega32U4": "Main microcontroller with built-in USB communication",
            "16 MHz Crystal Oscillator": "Provides clock timing for the microcontroller",
            "Micro USB Port": "For power and programming",
            "Power Jack": "Alternative power input",
            "ICSP Header": "For programming the bootloader",
            "Reset Button": "Resets the board",
            "Power LED": "Indicates when the board is powered",
            "TX/RX LEDs": "Indicate serial communication",
            "Voltage Regulator": "Regulates input voltage to 5V"
        }
    },
    "Arduino Due": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000062_front_1.jpg",
        "intro": "The Arduino Due is the first Arduino board based on a 32-bit ARM core microcontroller, offering significantly more processing power.",
        "microcontroller": "AT91SAM3X8E",
        "operating_voltage": "3.3V",
        "input_voltage": "7-12V",
        "digital_pins": "54 (of which 12 provide PWM output)",
        "analog_pins": "12",
        "flash_memory": "512 KB",
        "sram": "96 KB",
        "clock_speed": "84 MHz",
        "dimensions": "101.6 x 53.3 mm",
        "weight": "36g",
        "compatible_modules": [
            "LED Matrix", "Relay Module", "Bluetooth Module", "WiFi Module", 
            "LCD Display", "Servo Motors", "Ultrasonic Sensor", "Temperature Sensor",
            "GPS Module", "SD Card Module", "Camera Module", "Stepper Motor Driver",
            "CNC Shield", "3D Printer Controller", "Audio Processing"
        ],
        "components": {
            "AT91SAM3X8E": "32-bit ARM Cortex-M3 microcontroller",
            "84 MHz Crystal Oscillator": "Provides clock timing for the microcontroller",
            "2 Micro USB Ports": "One for programming, one for native USB",
            "Power Jack": "Alternative power input",
            "ICSP Header": "For programming the bootloader",
            "Reset Buttons": "2 reset buttons (one for each USB port)",
            "Power LED": "Indicates when the board is powered",
            "TX/RX LEDs": "Indicate serial communication",
            "Voltage Regulator": "Regulates input voltage to 3.3V"
        }
    },
    "Arduino Micro": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000053_featured_1.jpg",
        "intro": "The Arduino Micro is the smallest board in the Arduino family, featuring the ATmega32U4 microcontroller with built-in USB.",
        "microcontroller": "ATmega32U4",
        "operating_voltage": "5V",
        "input_voltage": "7-12V",
        "digital_pins": "20 (of which 7 provide PWM output)",
        "analog_pins": "12",
        "flash_memory": "32 KB (ATmega32U4) of which 4 KB used by bootloader",
        "sram": "2.5 KB (ATmega32U4)",
        "eeprom": "1 KB (ATmega32U4)",
        "clock_speed": "16 MHz",
        "dimensions": "48 x 18 mm",
        "weight": "13g",
        "compatible_modules": [
            "LED Matrix", "Small LCD Display", "Bluetooth Module", "Temperature Sensor",
            "Keyboard Emulation", "Mouse Emulation", "MIDI devices"
        ],
        "components": {
            "ATmega32U4": "Main microcontroller with built-in USB communication",
            "16 MHz Crystal Oscillator": "Provides clock timing for the microcontroller",
            "Micro USB Port": "For power and programming",
            "Reset Button": "Resets the board",
            "Power LED": "Indicates when the board is powered",
            "TX/RX LEDs": "Indicate serial communication",
            "Voltage Regulator": "Regulates input voltage to 5V"
        }
    },
    "Arduino Yún": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000008_featured.jpg",
        "intro": "The Arduino Yún combines the power of Linux with the ease of Arduino, featuring both a microcontroller and a microprocessor.",
        "microcontroller": "ATmega32U4",
        "microprocessor": "Atheros AR9331",
        "operating_voltage": "5V",
        "input_voltage": "5V",
        "digital_pins": "20",
        "analog_pins": "12",
        "flash_memory": "32 KB (ATmega32U4) + 16 MB (Linux)",
        "sram": "2.5 KB (ATmega32U4) + 64 MB (Linux)",
        "wifi": "IEEE 802.11b/g/n",
        "ethernet": "10/100 Mbit/s",
        "usb": "2.0 Host",
        "clock_speed": "16 MHz (ATmega32U4) + 400 MHz (AR9331)",
        "dimensions": "73 x 53 mm",
        "weight": "32g",
        "compatible_modules": [
            "WiFi Projects", "IOT Applications", "Web Servers", "Cloud Integration",
            "Remote Monitoring", "Home Automation"
        ],
        "components": {
            "ATmega32U4": "Arduino microcontroller that runs sketches",
            "Atheros AR9331": "Linux microprocessor for networking and complex processing",
            "16 MHz Crystal Oscillator": "Provides clock timing for the microcontroller",
            "Micro USB Port": "For power and programming",
            "Ethernet Port": "For wired network connection",
            "WiFi Module": "For wireless connectivity",
            "Reset Buttons": "Separate reset buttons for Arduino and Linux",
            "microSD Slot": "For expanded storage",
            "USB Host Port": "For connecting USB devices"
        }
    },
    "Arduino Portenta H7": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/b/abx00042_featured.jpg",
        "intro": "The Arduino Portenta H7 is a high-performance board designed for industrial applications and artificial intelligence.",
        "microcontroller": "STM32H747XI dual Cortex-M7+M4",
        "operating_voltage": "3.3V",
        "input_voltage": "5V USB or 6-60V VIN",
        "digital_pins": "22",
        "analog_pins": "7",
        "flash_memory": "2 MB Flash + 16 MB SDRAM",
        "connectivity": "WiFi, Bluetooth Low Energy, Ethernet",
        "clock_speed": "480 MHz (M7) + 240 MHz (M4)",
        "dimensions": "66 x 25 mm",
        "weight": "15g",
        "compatible_modules": [
            "Computer Vision", "Machine Learning", "High-Speed Data Processing",
            "Industrial Control", "Real-time Operating Systems", "Edge Computing"
        ],
        "components": {
            "STM32H747XI": "Dual-core ARM Cortex microcontroller",
            "2MB Flash Memory": "For program storage",
            "16MB SDRAM": "For fast data processing",
            "USB-C Port": "For power and programming",
            "WiFi/BT Module": "For wireless connectivity",
            "Crypto-Authentication": "For secure communications",
            "DisplayPort": "For video output",
            "High-Density Connectors": "For expansion boards and shields"
        }
    },
    "Arduino MKR WiFi 1010": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/b/abx00023_featured.jpg",
        "intro": "The Arduino MKR WiFi 1010 offers WiFi and Bluetooth connectivity in a compact form factor for IoT projects.",
        "microcontroller": "SAMD21 Cortex-M0+",
        "connectivity": "u-blox NINA-W10 (ESP32)",
        "operating_voltage": "3.3V",
        "input_voltage": "5V USB or 5-12V VIN",
        "digital_pins": "22",
        "analog_pins": "7",
        "flash_memory": "256 KB",
        "sram": "32 KB",
        "clock_speed": "48 MHz",
        "dimensions": "61.5 x 25 mm",
        "weight": "10g",
        "compatible_modules": [
            "WiFi Projects", "Bluetooth Projects", "IoT Devices", "Remote Sensing",
            "Smart Home Devices", "Connected Wearables"
        ],
        "components": {
            "SAMD21": "Low-power ARM Cortex-M0+ microcontroller",
            "NINA-W10 Module": "WiFi and Bluetooth module based on ESP32",
            "USB Port": "For power and programming",
            "Li-Po Charging Circuit": "For battery operation",
            "Crypto-Authentication": "For secure communications",
            "ECC508 Crypto Chip": "For enhanced security"
        }
    },
    "Arduino Pro Mini": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000087_featured.jpg",
        "intro": "The Arduino Pro Mini is a minimalist board intended for semi-permanent installation in projects requiring small size.",
        "microcontroller": "ATmega328P",
        "operating_voltage": "3.3V or 5V (depending on model)",
        "input_voltage": "3.35-12V (5V model) or 3.3-12V (3.3V model)",
        "digital_pins": "14 (of which 6 provide PWM output)",
        "analog_pins": "8",
        "flash_memory": "32 KB (ATmega328P) of which 2 KB used by bootloader",
        "sram": "2 KB (ATmega328P)",
        "eeprom": "1 KB (ATmega328P)",
        "clock_speed": "8 MHz (3.3V model) or 16 MHz (5V model)",
        "dimensions": "33 x 18 mm",
        "weight": "5g",
        "compatible_modules": [
            "Small LED Displays", "Sensors", "Battery-powered Projects",
            "Wearable Electronics", "Space-constrained Applications"
        ],
        "components": {
            "ATmega328P": "Main microcontroller that runs your code",
            "Crystal Oscillator": "Provides clock timing for the microcontroller",
            "Voltage Regulator": "Regulates input voltage",
            "Power LED": "Indicates when the board is powered",
            "Reset Button": "Resets the board"
        }
    },
    "Arduino Zero": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/b/abx00003_featured.jpg",
        "intro": "The Arduino Zero is a 32-bit extension of the UNO platform, featuring a powerful ARM Cortex-M0+ processor.",
        "microcontroller": "ATSAMD21G18 (Cortex-M0+)",
        "operating_voltage": "3.3V",
        "input_voltage": "7-12V",
        "digital_pins": "14 (of which 12 provide PWM output)",
        "analog_pins": "6 (12-bit ADC)",
        "flash_memory": "256 KB",
        "sram": "32 KB",
        "clock_speed": "48 MHz",
        "dimensions": "68.6 x 53.3 mm",
        "weight": "12g",
        "compatible_modules": [
            "Advanced Signal Processing", "Audio Applications", "Digital Synthesizers",
            "USB Devices", "High-precision Sensors"
        ],
        "components": {
            "ATSAMD21G18": "32-bit ARM Cortex-M0+ microcontroller",
            "USB Port": "For power and programming",
            "Embedded Debugger": "For advanced debugging capabilities",
            "Reset Button": "Resets the board",
            "Power LED": "Indicates when the board is powered",
            "Debug LEDs": "Indicate debugging status"
        }
    },
    "Arduino Lilypad": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000011_featured.jpg",
        "intro": "The Arduino Lilypad is designed for e-textiles and wearable projects with a unique circular design.",
        "microcontroller": "ATmega328P",
        "operating_voltage": "2.7-5.5V",
        "input_voltage": "2.7-5.5V",
        "digital_pins": "14 (of which 6 provide PWM output)",
        "analog_pins": "6",
        "flash_memory": "32 KB (ATmega328P) of which 2 KB used by bootloader",
        "sram": "2 KB (ATmega328P)",
        "eeprom": "1 KB (ATmega328P)",
        "clock_speed": "8 MHz",
        "dimensions": "50 mm diameter",
        "weight": "4g",
        "compatible_modules": [
            "Wearable Projects", "E-textiles", "LED Sequins", "Conductive Thread",
            "Fabric Sensors", "Soft Circuits"
        ],
        "components": {
            "ATmega328P": "Main microcontroller",
            "Sew Tabs": "Large conductive pads for sewing with conductive thread",
            "Power Header": "For battery connection",
            "Reset Switch": "Resets the board",
            "Power LED": "Indicates when the board is powered"
        }
    },
    "Arduino MKR1000": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/b/abx00004_featured.jpg",
        "intro": "The Arduino MKR1000 combines the functionality of the Zero and WiFi Shield in a compact form factor.",
        "microcontroller": "SAMD21 Cortex-M0+",
        "connectivity": "WINC1500 WiFi Module",
        "operating_voltage": "3.3V",
        "input_voltage": "5V USB or 5-12V VIN",
        "digital_pins": "22",
        "analog_pins": "7 (12-bit ADC)",
        "flash_memory": "256 KB",
        "sram": "32 KB",
        "clock_speed": "48 MHz",
        "dimensions": "61.5 x 25 mm",
        "weight": "10g",
        "compatible_modules": [
            "WiFi Projects", "IoT Devices", "Remote Sensing", 
            "Smart Home Devices", "Connected Wearables"
        ],
        "components": {
            "SAMD21": "Low-power ARM Cortex-M0+ microcontroller",
            "WINC1500": "WiFi module",
            "USB Port": "For power and programming",
            "Li-Po Charging Circuit": "For battery operation",
            "Power LED": "Indicates when the board is powered",
            "Crypto-Authentication": "For secure communications"
        }
    },
    "Arduino Esplora": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000095_featured.jpg",
        "intro": "The Arduino Esplora is a ready-to-use board with built-in sensors and inputs inspired by game controllers.",
        "microcontroller": "ATmega32U4",
        "operating_voltage": "5V",
        "input_voltage": "5V USB",
        "digital_pins": "20",
        "analog_pins": "12",
        "flash_memory": "32 KB (ATmega32U4) of which 4 KB used by bootloader",
        "sram": "2.5 KB (ATmega32U4)",
        "eeprom": "1 KB (ATmega32U4)",
        "clock_speed": "16 MHz",
        "dimensions": "165 x 60 mm",
        "weight": "53g",
        "compatible_modules": [
            "Game Controllers", "Interactive Applications", "Educational Projects",
            "TFT LCD Screen", "SD Card Module"
        ],
        "components": {
            "ATmega32U4": "Main microcontroller with built-in USB",
            "Joystick": "2-axis analog joystick with push button",
            "Buttons": "4 push buttons in diamond pattern",
            "Linear Potentiometer": "Slider for analog input",
            "Accelerometer": "3-axis accelerometer",
            "Temperature Sensor": "For ambient temperature readings",
            "Light Sensor": "For ambient light readings",
            "Microphone": "For sound detection",
            "RGB LED": "Programmable RGB LED",
            "Buzzer": "For sound output",
            "TFT LCD Connector": "For connecting compatible displays",
            "microSD Card Slot": "For storage expansion"
        }
    },
    "Arduino Ethernet": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/0/a000072_featured_1.jpg",
        "intro": "The Arduino Ethernet is an Arduino UNO with built-in Ethernet connectivity for network applications.",
        "microcontroller": "ATmega328P",
        "connectivity": "W5100 Ethernet Controller",
        "operating_voltage": "5V",
        "input_voltage": "7-12V",
        "digital_pins": "14 (of which 4 provide PWM output)",
        "analog_pins": "6",
        "flash_memory": "32 KB (ATmega328P) of which 0.5 KB used by bootloader",
        "sram": "2 KB (ATmega328P)",
        "eeprom": "1 KB (ATmega328P)",
        "clock_speed": "16 MHz",
        "dimensions": "68.6 x 53.4 mm",
        "weight": "28g",
        "compatible_modules": [
            "Web Servers", "Data Logging", "Remote Control Systems",
            "Network Sensors", "Home Automation", "IOT Gateways"
        ],
        "components": {
            "ATmega328P": "Main microcontroller",
            "W5100 Ethernet Controller": "Provides network connectivity",
            "RJ45 Port": "For Ethernet connection",
            "Power Jack": "Alternative power input",
            "microSD Card Slot": "For storage expansion",
            "Reset Button": "Resets the board",
            "Power LED": "Indicates when the board is powered",
            "Ethernet Status LEDs": "Indicate network activity"
        }
    },
    "Arduino MKR Fox 1200": {
        "image": "https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/1000x750/f8876a31b63532bbba4e781c30024a0a/a/b/abx00005_featured.jpg",
        "intro": "The Arduino MKR Fox 1200 provides SigFox connectivity for IoT devices with long range and low power consumption.",
        "microcontroller": "SAMD21 Cortex-M0+",
        "connectivity": "ATA8520 SigFox Module",
        "operating_voltage": "3.3V",
        "input_voltage": "5V USB or 5-12V VIN",
        "digital_pins": "22",
        "analog_pins": "7 (12-bit ADC)",
        "flash_memory": "256 KB",
        "sram": "32 KB",
        "clock_speed": "48 MHz",
        "dimensions": "61.5 x 25 mm",
        "weight": "10g",
        "compatible_modules": [
            "Long-range IoT", "Remote Monitoring", "Asset Tracking",
            "Environmental Sensing", "Smart Agriculture"
        ],
        "components": {
            "SAMD21": "Low-power ARM Cortex-M0+ microcontroller",
            "ATA8520": "SigFox module for LPWAN connectivity",
            "USB Port": "For power and programming",
            "Li-Po Charging Circuit": "For battery operation",
            "SigFox Antenna": "For network connectivity",
            "Power LED": "Indicates when the board is powered"
        }
    },    
    
}

# Function to load and display image
def load_image(url):
    try:
        st.image(url, use_column_width=True)
    except Exception as e:
        st.error(f"Error loading image: {e}")

# Main app
def main():
    # Header
    st.title("ARDUINO WHO-KNOW?")
    st.markdown("### Your Guide to Arduino Circuit Boards")
    
    # Sidebar for board selection
    st.sidebar.title("Select Arduino Board")
    selected_board = st.sidebar.selectbox(
        "Choose a board:",
        list(arduino_boards.keys())
    )
    
    # Display selected board info
    if selected_board:
        board_info = arduino_boards[selected_board]
        
        # Create columns for layout
        col1, col2 = st.columns([1, 2])
        
        # Left column - Image
        with col1:
            load_image(board_info["image"])
        
        # Right column - Basic info
        with col2:
            st.markdown(f"## {selected_board}")
            st.markdown(board_info["intro"])
            
            # Create tabs for different sections
            tabs = st.tabs(["Specifications", "Components", "Compatible Modules"])
            
            # Tab 1: Specifications
            with tabs[0]:
                specs_df = pd.DataFrame({
                    "Specification": [
                        "Microcontroller", "Operating Voltage", "Input Voltage", 
                        "Digital I/O Pins", "Analog Input Pins", "Flash Memory", 
                        "SRAM", "EEPROM", "Clock Speed", "Dimensions", "Weight"
                    ],
                    "Value": [
                        board_info["microcontroller"],
                        board_info["operating_voltage"],
                        board_info["input_voltage"],
                        board_info["digital_pins"],
                        board_info["analog_pins"],
                        board_info["flash_memory"],
                        board_info.get("sram", "N/A"),
                        board_info.get("eeprom", "N/A"),
                        board_info["clock_speed"],
                        board_info["dimensions"],
                        board_info["weight"]
                    ]
                })
                st.table(specs_df)
            
            # Tab 2: Components
            with tabs[1]:
                components = board_info["components"]
                for component, description in components.items():
                    st.markdown(f"**{component}**: {description}")
            
            # Tab 3: Compatible Modules
            with tabs[2]:
                modules = board_info["compatible_modules"]
                for module in modules:
                    st.markdown(f"- {module}")
        
        # Board comparison button
        if st.button("Compare with other boards"):
            st.markdown("## Board Comparison")
            
            # Prepare comparison data
            comparison_data = {
                "Board": list(arduino_boards.keys()),
                "Microcontroller": [board["microcontroller"] for board in arduino_boards.values()],
                "Operating Voltage": [board["operating_voltage"] for board in arduino_boards.values()],
                "Digital Pins": [board["digital_pins"].split()[0] for board in arduino_boards.values()],
                "Analog Pins": [board["analog_pins"] for board in arduino_boards.values()],
                "Flash Memory": [board["flash_memory"].split()[0] + " KB" for board in arduino_boards.values()],
                "Clock Speed": [board["clock_speed"] for board in arduino_boards.values()]
            }
            
            comparison_df = pd.DataFrame(comparison_data)
            st.dataframe(comparison_df)

if __name__ == "__main__":
    main()
