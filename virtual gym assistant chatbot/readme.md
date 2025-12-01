# GymGenie - Virtual Gym Assistant 🤖💪
<img width="1619" height="788" alt="image" src="https://github.com/user-attachments/assets/26647ffe-f470-401f-997d-97c5fcad6e95" />


##  Project Overview
GymGenie is an ***Egyption*** AI-powered virtual gym assistant that provides personalized fitness guidance, nutrition advice, and workout recommendations. Built with Google's Gemini AI and deployed via Streamlit, it serves as your 24/7 digital personal trainer.

##  Features
- 🤖 **AI-Powered Guidance**: Uses Google Gemini for intelligent fitness recommendations
- 📊 **Personalized Assessments**: Collects user metrics (weight, age, height, goals) for customized plans
- 🍎 **Nutrition & Diet Advice**: Provides meal recommendations based on fitness goals
- 💪 **Workout Planning**: Suggests exercise routines and techniques
- 🎯 **Goal-Oriented**: Focuses on helping users achieve their target weight and fitness levels
- 🌐 **Web-Based Interface**: Accessible from any device with a browser
- 🔒 **Secure Configuration**: API keys protected via environment variables

## 🛠️ Technologies Used
- **Python 3.9+**
- **Streamlit** - Web application framework
- **Google Gemini API** - AI model for fitness guidance
- **dotenv** - Environment variable management
- **CSS** - Custom styling and UI enhancements

## 📁 Project Structure
```
gymgenie/
├── GYM.py              # Main Streamlit application
├── styles.css          # Custom CSS styling
├── .env               # Environment variables (API keys)
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- Google AI Studio API key (Gemini API)
- pip (Python package manager)

### Step-by-Step Setup

1. **Clone or create the project directory**
   ```bash
   mkdir gymgenie
   cd gymgenie
   ```

2. **Create and activate virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit google-genai python-dotenv
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your Gemini API key:
     ```env
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

5. **Create CSS file**
   - Create `styles.css` in the project root with your custom styling

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🔧 Configuration

### Environment Variables
The application requires the following environment variable:
- `GEMINI_API_KEY`: Your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### System Prompt Customization
The AI behavior is controlled by the `SYSTEM_INSTRUCTION` in `app.py`. Modify this to change:
- Information collected from users
- Response scope (fitness-related only)
- Language preferences
- Interaction protocols

##  Usage

1. **Launch the app**: Run `streamlit run app.py`
2. **Initial Assessment**: The bot will ask for your weight, age, height, and fitness goals
3. **Ask Questions**: Inquire about:
   - Workout routines
   - Nutrition and diet plans
   - Exercise techniques
   - Progress tracking
   - Fitness-related queries

4. **Scope Limitation**: The bot only responds to fitness-related questions

##  Security Notes

- **Never commit** your `.env` file to version control
- Add `.env` to your `.gitignore` file
- Keep your API keys secure and rotate them periodically
- The app uses session state to maintain conversation context

##  Code Structure

### Main Components
1. **Environment Setup**: Loads API keys securely
2. **UI Configuration**: Sets up Streamlit page and custom CSS
3. **Chat Initialization**: Creates Gemini chat session with system instructions
4. **Message Handling**: Manages conversation flow and display
5. **Response Processing**: Sends queries to Gemini and displays responses

### Key Functions
- `load_css()`: Loads custom styling
- Chat session management using Streamlit session state
- Message display with role-based styling
- Error handling for missing API keys

## 🎨 Customization

### Styling
Edit `styles.css` to:
- Change colors and fonts
- Adjust message bubble styles
- Modify layout and spacing
- Add animations or transitions

### Functionality
Modify `app.py` to:
- Change the system prompt for different bot behavior
- Add new user metrics to collect
- Implement additional features like progress tracking
- Integrate with fitness APIs or databases


## ⚠️ Limitations

- Requires internet connection for Gemini API access
- Limited to fitness-related queries only
- Does not store user data persistently (session-based)
- Dependent on Google Gemini API availability and quotas

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

##  Acknowledgments
- Google Gemini AI for the language model
- Streamlit for the deployment framework
- Python community for excellent libraries

## 📞 Support
For issues or questions:
1. Check if your API key is valid and has sufficient quota
2. Ensure all dependencies are installed correctly
3. Verify the `.env` file is in the correct location
4. Check the browser console for errors

---

*Remember: Consistency is key to fitness success. Let GymGenie guide your journey!*
