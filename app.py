# import streamlit as st
# import openai
# import random

# # Set up OpenAI API credentials
# openai.api_key = ''

# # Define the chatbot's initial message
# intro_message = "Welcome to the Software Engineering Interview Bot! I'll ask you some questions commonly asked in software engineering interviews. Let's get started!"

# # Define a set of software engineering interview questions
# interview_questions = [
#     "Tell me about your experience with software development.",
#     "Explain the principles of object-oriented programming.",
#     "What is the difference between a stack and a queue?",
#     "How do you optimize the performance of a web application?",
#     "What is the role of indexing in databases?",
#     "Describe the process of version control and why it is important.",
#     "How do you handle debugging and troubleshooting in your projects?",
#     "What is the difference between unit testing and integration testing?",
#     "Explain the concept of RESTful API and its advantages.",
#     "How do you ensure the security of a web application?",
# ]

# # Define a set of positive feedback messages
# positive_feedback = [
#     "Great job!",
#     "Excellent response!",
#     "Impressive answer!",
#     "Well done!",
#     "Fantastic explanation!",
# ]

# # Define a set of negative feedback messages
# negative_feedback = [
#     "Hmm, could you provide more details?",
#     "I'm not sure I understood your answer. Can you clarify?",
#     "That's not quite what I was looking for. Can you try again?",
#     "I think your answer is incomplete. Can you elaborate?",
#     "Your response needs improvement. Please try again.",
# ]

# # Initialize chat history
# chat_history = []

# # Main Streamlit app
# def main():
#     st.title("Software Engineering Interview Bot")
#     st.sidebar.title("Chat Configuration")

#     # Set the user name
#     user_name = st.sidebar.text_input("Your Name", "Guest")

#     # Display intro message
#     st.markdown("<style>.chat-container{background-color: #F6F6F6; border-radius: 8px; padding: 15px;}"
#                 ".message{background-color: #FFFFFF; border-radius: 8px; padding: 10px; margin-bottom: 10px;}"
#                 ".user-message{background-color: #DCF8C6; color: #000000;}"
#                 ".bot-message{background-color: #FFFFFF; color: #000000; text-align: right;}</style>",
#                 unsafe_allow_html=True)
#     st.markdown("<div class='chat-container'>"
#                 "<div class='message bot-message'>" + intro_message + "</div>"
#                 "</div>", unsafe_allow_html=True)

#     # Main chat loop
#     while True:
#         # User input
#         user_input = st.text_input("You", key=f"user_input_{len(chat_history)}")

#         # Send user input to the chatbot
#         chat_history.append(f"{user_name}: {user_input}")

#         # Get chatbot's response
#         response = get_chatbot_response(chat_history)

#         # Add chatbot's response to the chat log
#         chat_history.append("Bot: " + response)

#         # Display chat log
#         st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
#         for message in chat_history:
#             role, content = message.split(": ")
#             if role == user_name:
#                 st.markdown("<div class='message user-message'><strong>" + user_name + ":</strong> " + content + "</div>",
#                             unsafe_allow_html=True)
#             else:
#                 st.markdown("<div class='message bot-message'><strong>Bot:</strong> " + content + "</div>",
#                             unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#         # Provide feedback on the response
#         if response:
#             if response in interview_questions:
#                 st.markdown("<div class='feedback-container'>"
#                             "<strong>Feedback:</strong> " + get_feedback(response, user_input) +
#                             "</div>", unsafe_allow_html=True)

# # Function to get the chatbot's response
# def get_chatbot_response(chat_history):
#     input_text = "\n".join(chat_history[-5:])  # Use last 5 messages for context

#     # If there is a user question, prioritize it
#     if "?" in input_text:
#         return answer_question(input_text)

#     # Otherwise, ask a software engineering interview question
#     question = random.choice(interview_questions)
#     return question

# # Function to answer a user question
# def answer_question(question):
#     response = openai.Completion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "I am the interviewer. Please provide your response."},
#             {"role": "user", "content": question},
#         ],
#         max_tokens=50,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     return response.choices[0].message.get("content")

# # Function to provide feedback on the user's reply
# def get_feedback(question, user_reply):
#     # Check if the user's reply matches the expected answer
#     if user_reply.lower() in question.lower():
#         return random.choice(positive_feedback)
#     else:
#         return random.choice(negative_feedback)

# if __name__ == "__main__":
#     main()











import streamlit as st
import openai

# Authenticate with OpenAI
openai.api_key = 'YOUR_API_KEY'

# Function to interact with the ChatGPT model
def ask_question(question, chat_log=None):
    if chat_log is None:
        chat_log = []
        
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=chat_log + [question],
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    
    chat_log.append(question)
    chat_log.append(response.choices[0].text.strip())
    
    return response.choices[0].text.strip(), chat_log

# Function to provide feedback on user's responses
def provide_feedback(question, user_input):
    if "teaching experience" in question.lower() and "relevant" in user_input.lower():
        feedback = "Great! Your teaching experience is relevant to the position."
    elif "lesson planning" in question.lower() and "thorough" in user_input.lower():
        feedback = "Excellent! Your approach to lesson planning is thorough and well-structured."
    elif "classroom management" in question.lower() and "effective" in user_input.lower():
        feedback = "Impressive! Your classroom management strategies seem effective."
    else:
        feedback = "Your response shows potential, but it can be improved. Try to provide more specific examples or elaborate further."
        
    return feedback

# Streamlit app
def main():
    st.title('History Teacher Interview Chatbot')
    
    # Initialize the chat log
    chat_log = []
    
    # Ask the user for their name
    user_name = st.text_input("Enter your name:")
    
    if user_name:
        st.write(f"Hello, {user_name}! Let's begin the interview.")
        
        # List of interview questions
        questions = [
            "Tell me about your teaching experience in history.",
            "Tell me about your approach to lesson planning in history.",
            "How do you manage classroom behavior and maintain an effective learning environment?",
            "How do you incorporate technology into your history lessons?",
            "How do you assess student learning and provide feedback?",
            "How do you promote inclusivity and diversity in your history classroom?"
        ]
        
        # Loop to ask interview questions
        for i, question in enumerate(questions):
            user_input = st.text_input("You:", key=f"question_{i}").strip()
            
            if user_input:
                # Ask the question to the model
                response, chat_log = ask_question(user_input, chat_log)
                
                # Display the model's response
                st.write("ChatGPT:", response)
                
                # Provide feedback on the user's response
                if len(chat_log) % 2 == 0:
                    feedback = provide_feedback(question, user_input)
                    st.write("Feedback:", feedback)
                
    else:
        st.write("Please enter your name to begin the interview.")
        
if __name__ == "__main__":
    main()
