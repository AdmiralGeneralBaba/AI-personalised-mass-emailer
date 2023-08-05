import tkinter as tk
from tkinter import filedialog
from ai_email_maker import AIEmailMaker
class EmailSenderGUI:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AI Email Sender")
        self.test = AIEmailMaker()
        self.sender_list = []
        self.password_list = []
        self.json_file = ""
        
        self.create_widgets()
        
    def create_widgets(self):
        # Creating sender email input field
        self.email_label = tk.Label(self.window, text="Email Sender")
        self.email_label.pack()
        self.email_input = tk.Entry(self.window)
        self.email_input.pack()
        
        # Creating password input field
        self.pass_label = tk.Label(self.window, text="Email Password")
        self.pass_label.pack()
        self.pass_input = tk.Entry(self.window, show="*")
        self.pass_input.pack()
        
        # Button to add email and password to respective lists
        self.add_button = tk.Button(self.window, text="Add Email", command=self.add_email)
        self.add_button.pack()
        
        # Button to select JSON file
        self.file_button = tk.Button(self.window, text="Select JSON", command=self.load_json)
        self.file_button.pack()
        
        # Button to start email sending process
        self.send_button = tk.Button(self.window, text="Start Email Sending", command=self.send_emails)
        self.send_button.pack()
    
    def add_email(self):
        self.sender_list.append(self.email_input.get())
        self.password_list.append(self.pass_input.get())
        
        # Clear the input fields after adding
        self.email_input.delete(0, 'end')
        self.pass_input.delete(0, 'end')
    
    def load_json(self):
        self.json_file = filedialog.askopenfilename(initialdir="/", title="Select JSON file",
                                            filetypes=(("jsonl files", "*.jsonl"), ("all files", "*.*")))
        if self.json_file:
            self.json_data = self.test.load_json_objects(self.json_file)
        
    def send_emails(self):
        if self.sender_list and self.password_list and self.json_file:
            self.test.ai_email_full_sending_and_creation(self.sender_list, self.password_list, self.json_data)
        
def main():
    gui = EmailSenderGUI()
    gui.window.mainloop()

if __name__ == "__main__":
    main()