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
        max_tokens=500,
        temperature=0.7,
        n=1,
        stop=None,
    )

    chat_log.append(question)
    chat_log.append(response.choices[0].text.strip())

    return response.choices[0].text.strip(), chat_log

# Function to provide feedback on user's responses
def provide_feedback(question, user_input):
    # Provide your own implementation or use external libraries for advanced feedback analysis
    # You can train a custom feedback analysis model or use pre-trained models like sentiment analysis
    # Here, we'll use a simple rule-based approach as an example
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

    # Ask the user for their name
    user_name = st.text_input("Enter your name:")

    if user_name:
        st.write(f"Hi {user_name}! Let's begin the interview.")

        # Conversation context
        chat_log = []
        question_index = st.session_state.get('question_index', 0)

        # List of interview questions
        questions = [
            "What got you interested in teaching history?",
            "What makes you stand out as a history teacher?",
            "How do you incorporate technology into your history lessons?",
            "Tell me about a challenging situation you faced as a history teacher and how you handled it.",
            "How do you assess student learning and provide feedback?",
            "How do you promote inclusivity and diversity in your history classroom?"
        ]

        if question_index < len(questions):
            if st.button("Next"):
                question_index += 1
                st.session_state['question_index'] = question_index
                st.empty()

            question = questions[question_index]
            st.write("Question:", question)
            user_input = st.text_input("Your response:", key=f"question_{question_index}").strip()

            if user_input:
                # Save user input to the conversation log
                chat_log.append(f"{user_name}: {user_input}")

                # Provide feedback on the user's response
                feedback = provide_feedback(question, user_input)
                st.write("Feedback:", feedback)

                # Generate a longer "better response" to the question using the model
                better_response = ""
                while len(better_response.split()) < 350:
                    response, _ = ask_question(question, chat_log[:-1])
                    better_response = response

                st.write("Better response:")
                st.write(better_response)

    else:
        st.write("Please enter your name to begin the interview.")

if __name__ == "__main__":
    main()
