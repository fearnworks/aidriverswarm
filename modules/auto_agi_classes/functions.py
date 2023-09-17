import os
import interpreter
import pyautogui
import time
from termcolor import colored
from modules.swarmGPT import GPTSwarm, OpenAIApiCaller, Config


def read_file(file_path: str) -> str:
    """Reads the contents of a file and returns it as a string"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f'contents of {file_path}:{f.read()}'

def write_file(file_path: str, content: str) -> str:
    """Writes the contents of a file and returns a confirmation message.
    Respond with a JSON-encoded string only.
    Return only plain strings without any control characters, such as newline ('\n') or tab ('\t').
    """
    abs_working_dir = os.path.abspath(os.getcwd())
    abs_file_path = os.path.abspath(file_path)
    if not abs_file_path.startswith(abs_working_dir):
            return 'Error: Invalid file path. Writing outside of working directory is not permitted.'
    with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    return f'File {file_path} was successfully written. move on to the next step. stop if all steps are completed. '

def append_file(file_path: str, content: str) -> str:
    """Appends content to the end of a file and returns a confirmation message"""
    with open(file_path, 'a', encoding='utf-8') as f:
            f.write(content)
    return f'Content was successfully appended to {file_path}. move on to the next step. stop if all steps are completed.'

def create_directory(dir_path: str) -> str:
    """Creates a directory and returns a confirmation message"""
    os.mkdir(dir_path)
    return f'Directory {dir_path} was successfully created. move on to the next step. stop if all steps are completed.'

def list_files(dir_path: str) -> str:
    """Lists the files in a directory and returns a confirmation message"""
    return f'Files in {dir_path}:\n' + '\n'.join(os.listdir(dir_path))

def code_interpreter(message: str) -> str:
    """Use this to ask code interpreter to execute user's requests only when user asks for you to use the code interpreter. ask to code interpreter in natural language. refer to code interpreter as "you" You are prohibited to call this unless the user asks for you to call this function sepcifically."""
    
    response = interpreter.chat(message, return_messages=True)[-1]["content"]
    print(response)
    # reset the interpreter after each use
    interpreter.reset()
    return f'Code interpreter respondes as: {response}. move on to the next step. stop if all steps are completed.'

def start_auto_agi(message: str) -> str:
    """Use this to start an instance of auto agi with the task or message user requested only when user asks for you start an auto agi. If no message is necessary send None. You are prohibited to call this unless the user asks for you to call this function sepcifically."""
    # Open the command prompt with the desired command
    os.system('start cmd /K python auto_agi.py')
    # open auto agi in a conda environment wait 2 second then run the script
    # os.system('start cmd /K conda activate python_web')
    # time.sleep(2)  # Adjust this sleep duration as needed
    # pyautogui.write('python auto_agi.py')
    # time.sleep(0.5)
    # pyautogui.press('enter')

    # Wait for a brief moment to ensure the script is ready to receive input
    time.sleep(3)  # Adjust this sleep duration as needed

    # Use pyautogui to type the input
    if not message == "None":
        pyautogui.write("multi")
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.write(message  + "\n" + "done")
        time.sleep(0.5)

        pyautogui.press('enter')
    return f'auto_agi.py script for "{message[:30]}..." was successfully started. move on to the next step. stop if all steps are completed.'

def call_swarm(user_message: str) -> str:
    '''Use this only when user has asked you to utilize the swarm or swarm gpt to complete a task. You are prohibited to call this unless the user asks for you to call this function sepcifically.'''
    print(colored("...INITIALIZING SWARM...", "red"))
    # user_message = "Write the full code for a snake game with pygame. 3 snakes move automatically towards the food. there is a user snake which is also competing. keep track of the scores. snakes wrap around the screen. "
    user_message = user_message
    gpt_api_caller = OpenAIApiCaller()
    swarm = GPTSwarm(user_message, gpt_api_caller)
    # exit()
    synthesized_response = swarm.generate_response()
    print(synthesized_response)
    return f'Swarm responsds as: {synthesized_response}. move on to the next step. stop if all steps are completed.'