"""
chatbot.py — Entry point for the Todo AI Chatbot.
Phase III: AI-Powered Todo Chatbot

Run with: python chatbot.py
Requires: Phase II backend running at localhost:8000
"""
import os
from dotenv import load_dotenv
from agents import Runner
from agent import create_todo_agent

load_dotenv()


def check_openai_key() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set.")
        print("Copy .env.example to .env and add your OpenAI API key.")
        raise SystemExit(1)


def print_banner() -> None:
    print("=" * 60)
    print("  Todo Evolution — Phase III: AI-Powered Chatbot")
    print("  Spec-Kit Plus | Panaversity Hackathon 2026")
    print("=" * 60)
    print("  Powered by: OpenAI Agents SDK + MCP Tools")
    print("  Backend: http://localhost:8000 (must be running)")
    print("-" * 60)
    print("  Type your request in natural language.")
    print("  Examples:")
    print('    "Add buy groceries with high priority"')
    print('    "Show my pending tasks"')
    print('    "Mark the groceries task as done"')
    print('    "Delete all completed tasks"')
    print('    Type "exit" to quit.')
    print("=" * 60)
    print()


def main() -> None:
    check_openai_key()
    print_banner()

    agent = create_todo_agent()
    conversation_history = []

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "bye"):
            print("Assistant: Goodbye! Have a productive day!")
            break

        conversation_history.append({"role": "user", "content": user_input})

        try:
            result = Runner.run_sync(agent, conversation_history)
            response = result.final_output

            conversation_history.append({"role": "assistant", "content": response})

            print(f"\nAssistant: {response}\n")

        except Exception as e:
            print(f"\nAssistant: Sorry, I ran into an error: {e}")
            print("Make sure the Phase II backend is running at localhost:8000\n")


if __name__ == "__main__":
    main()
