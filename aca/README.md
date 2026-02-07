# Python Learning Platform - Modern UI

A modern, interactive web-based platform for learning Python programming with real-time code execution and a beautiful user interface.

## Features

✨ **Interactive Learning**
- Structured lessons covering Python fundamentals to advanced topics
- Real-time code execution in the browser
- Instant feedback and error messages
- Syntax-highlighted code editor with CodeMirror

🎨 **Modern UI/UX**
- Gradient backgrounds and glassmorphism effects
- Responsive design for all devices
- Dark theme optimized for coding
- Smooth animations and transitions

🚀 **Key Components**
- **Home Page**: Overview of all available lessons
- **Lesson Pages**: Interactive tutorials with code examples
- **Playground**: Free-form Python coding environment
- **Progress Tracking**: Visual indicators of learning progress

## Installation

1. **Clone or navigate to the project directory**
```bash
cd c:\Users\alvin\TEst\introtodeeplearning\aca
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open your browser**
Navigate to: `http://localhost:5000`

## Project Structure

```
aca/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css          # Modern CSS styling
│   └── js/
│       ├── main.js            # Core JavaScript functionality
│       ├── lesson.js          # Lesson page interactivity
│       └── playground.js      # Playground functionality
└── templates/
    ├── base.html              # Base template with navbar
    ├── index.html             # Home page
    ├── lesson.html            # Individual lesson page
    └── playground.html        # Code playground
```

## Usage

### Learning Path
1. Start from the home page to see all available lessons
2. Click on any lesson to begin learning
3. Follow the structured topics within each lesson
4. Write and execute code directly in the browser
5. See immediate results and error messages

### Playground
- Access the playground from the navigation bar
- Write any Python code you want to experiment with
- Execute code with the "Run Code" button or `Ctrl+Enter`
- Perfect for testing ideas and practicing

## Lesson Topics

**Lesson 1: Python Basics**
- Variables and Data Types
- Lists and Loops
- Dictionaries

**Lesson 2: Functions and Control Flow**
- Functions
- If-Else Statements
- List Comprehensions

**Lesson 3: Object-Oriented Programming**
- Classes and Objects
- Inheritance

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Code Editor**: CodeMirror
- **Icons**: Font Awesome
- **Styling**: Custom CSS with modern design patterns

## Features in Detail

### Interactive Code Execution
- All Python code runs server-side for security
- Standard library fully available
- Output captured and displayed in real-time
- Error messages formatted for easy debugging

### Modern Design
- Gradient backgrounds
- Glassmorphism UI elements
- Smooth transitions and animations
- Fully responsive layout
- Dark theme optimized for coding

### Keyboard Shortcuts
- `Ctrl/Cmd + Enter`: Run code in active editor

## Security Note

This platform executes Python code on the server. In a production environment, you should:
- Implement code sandboxing
- Add user authentication
- Set execution timeouts
- Limit resource usage
- Validate and sanitize all inputs

## Future Enhancements

- [ ] User authentication and profiles
- [ ] Progress tracking and achievements
- [ ] More advanced Python topics
- [ ] Code challenges and quizzes
- [ ] Community features and code sharing
- [ ] Mobile app version

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and add your own lessons, improve the UI, or enhance functionality!

---

**Happy Learning! 🐍**
