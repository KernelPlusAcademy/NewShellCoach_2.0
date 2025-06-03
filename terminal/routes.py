
from flask import Blueprint, render_template, request, jsonify
import openai
import os

terminal_bp = Blueprint('terminal', __name__)

@terminal_bp.route('/terminal')
def terminal_view():
    return render_template('terminal.html')

@terminal_bp.route('/explain', methods=['POST'])
def explain_command():
    data = request.get_json()
    command = data.get('command', '')
    explanation = generate_explanation(command)
    return jsonify({'explanation': explanation})

def generate_explanation(command):
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful Linux assistant."},
                {"role": "user", "content": f"Explain what this Linux command does: {command}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"


# Simulated command history (in-memory)
command_history = []

@terminal_bp.route('/history', methods=['GET'])
def history():
    return jsonify({'history': command_history})

@terminal_bp.route('/explain', methods=['POST'])
def explain_command_with_history():
    data = request.get_json()
    command = data.get('command', '')
    command_history.append(command)
    explanation = generate_explanation(command)
    return jsonify({'explanation': explanation})
