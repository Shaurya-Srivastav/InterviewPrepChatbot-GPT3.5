# Job Interview Chatbot

The Job Interview Chatbot is an interactive application that helps users practice job interview scenarios. It utilizes the OpenAI GPT-3 language model to generate interview questions and provide feedback on the user's responses. The chatbot aims to assist job seekers in improving their interview skills and providing them with valuable insights to enhance their performance.

## Features

- User authentication with OpenAI to access the GPT-3 language model.
- Automatic generation of interview questions based on the user's job interest.
- Feedback on the user's responses using the GPT-3 language model.
- Generation of a more creative and improved "better response" to each question.
- User-friendly interface built with Streamlit.

## Technical Overview

The Job Interview Chatbot is a Python-based application that leverages OpenAI's GPT-3 language model and Streamlit framework to simulate interactive job interview experiences. Here's a brief technical overview:

* The chatbot utilizes the GPT-3 model to generate interview questions based on the user's job interest.
* Users provide their responses, which are analyzed using sentiment analysis.
* The GPT-3 model generates feedback on the user's response, suggesting improvements and highlighting strengths.
* The chatbot saves the conversation history and uses it to generate a more creative and enhanced "better response" to the question.
* OpenAI API handles the communication with the GPT-3 model, utilizing a variant of the Transformer architecture.
* The vaderSentiment library is used for sentiment analysis, providing insights into the sentiment of user responses.
* Customization options allow users to adjust parameters like temperature and maximum token length for fine-tuning the chatbot's behavior.
* The application provides a user-friendly web interface powered by the Streamlit framework.

In summary, the Job Interview Chatbot combines OpenAI's GPT-3 model, sentiment analysis, and a streamlined interface to deliver a technically sophisticated and interactive job interview practice experience.

## Prerequisites

To run the Job Interview Chatbot, you need to have the following dependencies installed:

- Python 3.6 or later
- Streamlit
- OpenAI Python SDK
- vaderSentiment Python library

## Getting Started

1. Clone the repository: git clone [https://github.com/your-username/job-interview-chatbot.git](https://github.com/your-username/job-interview-chatbot.git)
2. Navigate to the project directory: cd job-interview-chatbot
3. Install the required dependencies: pip install -r requirements.txt
4. Set up your OpenAI API key by replacing `'YOUR_API_KEY'` in the code with your actual API key.
5. Run the application: streamlit run main.py
6. Open your web browser and visit `http://localhost:8501` to access the Job Interview Chatbot.

## Usage

1. Enter your name to begin the interview session.
2. Provide your job interest (e.g., Software Engineer, Data Scientist, Teacher).
3. The chatbot will generate interview questions based on your job interest.
4. For each question, enter your response in the text input field.
5. The chatbot will provide feedback on your response, suggesting improvements and highlighting strengths.
6. It will also generate a more creative and improved "better response" to the question.
7. Use the "Next" button to move to the next question and continue the interview process.

## Customization

- You can customize the behavior of the chatbot by modifying the OpenAI API parameters in the code, such as `temperature` and `max_tokens`.
- Additionally, you can adjust the feedback length by modifying the condition in the `provide_feedback` function.

## Limitations

- The chatbot's performance relies on the capabilities and training of the underlying GPT-3 language model.
- The generated questions and feedback are based on patterns and examples seen in the training data and may not always accurately reflect real-world scenarios.
- The chatbot does not replace human judgment and expertise in evaluating job interview responses.

## Contributing

Contributions to the Job Interview Chatbot project are welcome! If you find any issues or have suggestions for improvement, please submit a pull request or open an issue.
