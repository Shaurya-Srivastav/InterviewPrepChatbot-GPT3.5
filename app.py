import streamlit as st
import openai
import random

# Set up OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Define the chatbot's initial message
intro_message = "Welcome to the Software Engineering Interview Bot! I'll ask you some questions commonly asked in software engineering interviews. Let's get started!"

# Define a set of software engineering interview questions
interview_questions = [
    "Tell me about your experience with software development.",
    "Explain the principles of object-oriented programming.",
    "What is the difference between a stack and a queue?",
    "How do you optimize the performance of a web application?",
    "What is the role of indexing in databases?",
    "Describe the process of version control and why it is important.",
    "How do you handle debugging and troubleshooting in your projects?",
    "What is the difference between unit testing and integration testing?",
    "Explain the concept of RESTful API and its advantages.",
    "How do you ensure the security of a web application?",
]

# Define a set of positive feedback messages
positive_feedback = [
    "Great job!",
    "Excellent response!",
    "Impressive answer!",
    "Well done!",
    "Fantastic explanation!",
]

# Define a set of negative feedback messages
negative_feedback = [
    "Hmm, could you provide more details?",
    "I'm not sure I understood your answer. Can you clarify?",
    "That's not quite what I was looking for. Can you try again?",
    "I think your answer is incomplete. Can you elaborate?",
    "Your response needs improvement. Please try again.",
]

# Initialize chat history
chat_history = []

# Main Streamlit app
def main():
    st.title("Software Engineering Interview Bot")
    st.sidebar.title("Chat Configuration")

    # Set the user name
    user_name = st.sidebar.text_input("Your Name", "Guest")

    # Display intro message
    st.markdown("### Bot:")
    st.text_area("Chat Log", value=intro_message, key="chat_log")

    # Main chat loop
    while True:
        # User input
        user_input = st.text_input("You", key="user_input")

        # Send user input to the chatbot
        chat_history.append(f"{user_name}: {user_input}")

        # Get chatbot's response
        response = get_chatbot_response(chat_history)

        # Add chatbot's response to the chat log
        chat_history.append("Bot: " + response)

        # Display chat log
        st.text_area("Chat Log", value="\n".join(chat_history), key="chat_log")

        # Clear user input after sending
        st.text_input("You", key="user_input")

        # Provide feedback on the response
        if response:
            st.markdown("### Bot:")
            st.text(response)

            # Check if the bot asked a question
            if response in interview_questions:
                st.markdown("### Feedback:")
                st.text(get_feedback(response, user_input))

# Function to get the chatbot's response
def get_chatbot_response(chat_history):
    input_text = "\n".join(chat_history[-5:])  # Use last 5 messages for context

    # If there is a user question, prioritize it
    if "?" in input_text:
        return answer_question(input_text)

    # Otherwise, ask a software engineering interview question
    question = random.choice(interview_questions)
    return question

# Function to answer a user question
def answer_question(question):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message.get("content")

# Function to provide feedback on the user's reply
def get_feedback(question, user_reply):
    # Check if the user's reply matches the expected answer
    if user_reply.lower() in question.lower():
        return random.choice(positive_feedback)
    else:
        return random.choice(negative_feedback)

if __name__ == "__main__":
    main()
