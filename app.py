import streamlit as st
import openai

# Authenticate with OpenAI
openai.api_key = "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"

# Function to interact with the ChatGPT model
def ask_question(question, chat_log=None):
    if chat_log is None:
        chat_log = []

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt= chat_log + [question],
        max_tokens=400,
        temperature=1.0,
        n=1,
        stop=None,
    )

    chat_log.append(question)
    chat_log.append(response.choices[0].text.strip())

    return response.choices[0].text.strip(), chat_log

# Function to provide feedback on user's responses
def provide_feedback(question, user_input):
    feedback_prompt = f"Provide feedback as if I answered this on an interview question. Give me ways to improve my answer: : '{question}'\n\nUser response: '{user_input}'"
    feedback = ''
    while len(feedback.split()) < 150:
        response, _ = ask_question(feedback_prompt)
        feedback += response
        
    return feedback


# Streamlit app
def main():
    st.title('Job Interview Chatbot')

    # Ask the user for their name
    user_name = st.text_input("Enter your name:")

    if user_name:
        st.write(f"Hi {user_name}! Let's begin the interview.")

        # Conversation context
        chat_log = []
        question_index = st.session_state.get('question_index', 0)

        # Ask the user for their job interest
        job_interest = st.text_input("Enter your job interest (e.g., History Teacher, Software Engineer, Cook):")

        if job_interest:
            st.write(f"Great! Let's generate some interview questions based on your interest in {job_interest}.")

            # Generate interview questions based on job interest using the model
            generated_questions, _ = ask_question(f"Generate interview questions for a {job_interest}")
            questions = generated_questions.split("\n")

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
                    st.subheader("Feedback:")
                    st.write(feedback)

                     # Generate a more creative and better-suited "better response" to the question using the model
                    better_response_prompt = f"Generate a more creative and improved response to this question: '{question}'\n\nUser response: '{user_input}'\n\nBetter response (at least 400 words):"
                    better_response = ''
                    while len(better_response.split()) < 250:
                        response, _ = ask_question(better_response_prompt, chat_log[:-1])
                        better_response += response

                    st.subheader("**Better response:**")
                    st.write(better_response)
        else:
            st.write("Please enter your job interest to generate interview questions.")

    else:
        st.write("Please enter your name to begin the interview.")

if __name__ == "__main__":
    main()
