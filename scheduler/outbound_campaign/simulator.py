from agent.reasoning.llm_agent import extract_intent
from agent.tools.tool_router import execute_tool


def run_reminder_campaign():

    reminder_text = "Reminder: You have an appointment tomorrow."

    print("AI Agent:", reminder_text)

    patient_response = "Can we move it to Friday?"

    print("Patient:", patient_response)

    intent = extract_intent(patient_response)

    result = execute_tool(intent)

    print("AI Agent Response:", result)