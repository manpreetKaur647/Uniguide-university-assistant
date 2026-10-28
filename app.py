import streamlit as st

# --------------------------------
# 1. WEBSITE SETTINGS
# --------------------------------
st.set_page_config(
    page_title="UniGuide - University Assistant",
    page_icon="🎓",
    layout="centered"
)

ASSISTANT_NAME = "UniGuide"

st.title("🎓 UniGuide")
st.subheader("Your University Assistant")
st.caption("Transport | Gate Pass | About the Creator | FAQs")

st.info(
    "Student support chatbot prototype. "
    "Confirm official university information with the university."
)

# --------------------------------
# 2. CREATOR PROFILE
# --------------------------------
creator = {
    "name": "Manpreet Kaur",
    "course": "MBA",
    "university": "Akal University, Talwandi Sabo",
    "role": "Student and project creator",
    "project": (
        "A university assistant prototype designed to help "
        "students with transport information and gate pass guidance."
    )
}

# --------------------------------
# 3. TRANSPORT INFORMATION
# Replace samples with verified details
# --------------------------------
transport = {
    "route a": "Sample Route A: 7:30 AM",
    "route b": "Sample Route B: 7:45 AM",
    "route c": "Sample Route C: 8:00 AM"
}

# --------------------------------
# 4. FICTIONAL GATE PASS RECORDS
# --------------------------------
demo_statuses = {
    "DEMO001": "Applied",
    "DEMO002": "Pending",
    "DEMO003": "Approved",
    "DEMO004": "Rejected"
}

# --------------------------------
# 5. COMMON QUESTIONS AND ANSWERS
# Add more FAQs in this section
# --------------------------------
faqs = {
    "what is this project": (
        "UniGuide is a prototype designed to help students "
        "find university transport information and gate pass guidance."
    ),
    "what can you do": (
        "I can answer questions about my creator, sample transport "
        "routes, gate pass procedures, and common university FAQs."
    ),
    "what is akal university": (
        "My creator studies at Akal University, Talwandi Sabo. "
        "For official university information, please consult "
        "the university's official channels."
    ),
    "how can i get help": (
        "Ask me about the creator, transport, gate passes, "
        "or type 'help' to see example questions."
    )
}

# --------------------------------
# 6. ANSWER QUESTIONS
# --------------------------------
def get_answer(question):
    q = question.lower().strip()

    # Creator details
    if any(x in q for x in [
        "who created you",
        "who is your creator",
        "who made you",
        "who developed you",
        "who is the developer"
    ]):
        return (
            f"I am {ASSISTANT_NAME}, a university assistant prototype "
            f"created by {creator['name']}."
        )

    if any(x in q for x in [
        "tell me about yourself",
        "tell me about your creator",
        "tell me about manpreet",
        "who is manpreet",
        "about the creator",
        "about manpreet kaur"
    ]):
        return (
            f"My creator is {creator['name']}. "
            f"She is pursuing {creator['course']} at "
            f"{creator['university']}. "
            f"She is a {creator['role']}. "
            f"{creator['project']}"
        )

    if any(x in q for x in [
        "your name",
        "name of this assistant",
        "what are you called"
    ]):
        return f"My name is {ASSISTANT_NAME}."

    if any(x in q for x in [
        "which course",
        "what course",
        "what is her course",
        "what is manpreet studying"
    ]):
        return (
            f"{creator['name']} is pursuing "
            f"{creator['course']}."
        )

    if any(x in q for x in [
        "which university",
        "what university",
        "where does manpreet study"
    ]):
        return (
            f"{creator['name']} studies at "
            f"{creator['university']}."
        )

    if any(x in q for x in [
        "your role",
        "creator's role",
        "what is manpreet's role"
    ]):
        return (
            f"{creator['name']} is a "
            f"{creator['role']}."
        )

    # Fictional gate pass status lookup
    for demo_id, status in demo_statuses.items():
        if demo_id.lower() in q:
            return (
                f"Demo application {demo_id} has status: {status}. "
                "This is fictional test data, not a real student record."
            )

    # Transport information
    for route, details in transport.items():
        if route in q:
            return (
                f"{details}. This is a fictional sample schedule. "
                "Please confirm actual timings with the university."
            )

    if any(x in q for x in [
        "bus", "transport", "route", "bus timing",
        "bus time", "bus schedule"
    ]):
        return (
            "You can ask about Route A, Route B, or Route C. "
            "These are sample routes. Actual university transport "
            "details have not been connected to this prototype."
        )

    # Gate pass guidance
    if any(x in q for x in [
        "gate pass", "gatepass", "leave pass",
        "apply for pass", "pass procedure"
    ]):
        return (
            "Sample gate pass procedure:\n"
            "1. Sign in to the official student portal.\n"
            "2. Open the Gate Pass section.\n"
            "3. Enter the required information.\n"
            "4. Submit the application if the portal allows it.\n"
            "5. Check the portal for updates.\n\n"
            "Please confirm the actual procedure with your university."
        )

    if "pending" in q:
        return "Pending means an application is waiting for a decision."

    if "approved" in q:
        return "Approved means an application has been accepted."

    if "rejected" in q:
        return "Rejected means an application was not accepted."

    # Additional FAQs
    for keyword, answer in faqs.items():
        if keyword in q:
            return answer

    if any(x in q for x in ["hello", "hi", "hey"]):
        return (
            f"Hello! 👋 I am {ASSISTANT_NAME}. "
            "Ask me about my creator, university transport, "
            "or gate pass guidance."
        )

    if "help" in q:
        return (
            "Try asking:\n"
            "- Who created you?\n"
            "- Tell me about Manpreet Kaur.\n"
            "- Which course is she pursuing?\n"
            "- What is your name?\n"
            "- What time does Route A leave?\n"
            "- How do I apply for a gate pass?\n"
            "- Check DEMO002\n"
            "- What does Pending mean?"
        )

    return (
        "Sorry, this information is not available in my current "
        "FAQs. Please confirm it with the university or add a "
        "suitable question and answer to my FAQ section."
    )

# --------------------------------
# 7. ABOUT THE CREATOR PANEL
# --------------------------------
with st.expander("👩‍🎓 About the Creator"):
    st.write("**Name:**", creator["name"])
    st.write("**Course:**", creator["course"])
    st.write("**University:**", creator["university"])
    st.write("**Role:**", creator["role"])
    st.write("**Project:**", creator["project"])

# --------------------------------
# 8. EXAMPLE QUESTIONS
# --------------------------------
with st.expander("💡 Example questions"):
    st.markdown("""
    - Who created you?
    - Tell me about Manpreet Kaur.
    - Which course is she pursuing?
    - What is your name?
    - What is this project about?
    - What time does Route A leave?
    - How do I apply for a gate pass?
    - Check DEMO002.
    """)

# --------------------------------
# 9. CHAT INTERFACE
# --------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask UniGuide a question...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    answer = get_answer(question)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

# --------------------------------
# 10. DEMO STATUS LIST
# --------------------------------
with st.expander("🧪 View fictional test records"):
    for demo_id, status in demo_statuses.items():
        st.write(f"{demo_id} — {status}")

    st.caption(
        "These records are fictional and do not connect "
        "to the university's actual gate pass system."
    )
