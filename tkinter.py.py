import tkinter as tk
from tkinter import Text, Button, filedialog
import emoji
from tkinter import colorchooser

# Roles and Permissions
def change_bg_color():
    color = colorchooser.askcolor()[1]
    root.configure(bg=color)

# Create the main window
root = tk.Tk()
root.title("Personal Diary")

# Create a button to change background color
bg_color_button = tk.Button(root, text="Change Background Color", command=change_bg_color)
bg_color_button.pack()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class DiaryApp:
    def __init__(self):
        self.users = []  # Store user objects in memory

    def register_user(self, username, password):
        # Check if the username is unique (you can implement this logic)
        # Create a new user and add them to the list of users
        new_user = User(username, password)
        self.users.append(new_user)

    def login_user(self, username, password):
        # Check if the username and password match an existing user (you can implement this logic)
        # Return the user object if authenticated
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

# Create an instance of the diary application
diary_app = DiaryApp()
class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self)
        self.button["text"] = "Click me!"
        self.button["command"] = self.say_hello
        self.button.pack(side="top")

    def say_hello(self):
        print("Hello, Tkinter!")

root = tk.Tk()
app = MyFrame(master=root)

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Diary")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to your Personal Diary!")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry)
        self.add_button.pack()

        self.read_button = tk.Button(self.root, text="Read Entries", command=self.read_entries)
        self.read_button.pack()

    def add_entry(self):
        entry_text = self.entry.get()
        # Add the entry text to your diary or perform the desired action
def read_entries(self):                            

        # Read and display diary entries or perform the desired action
   root = tk.Tk()
   app = DiaryApp(root)
   root.mainloop()

        
# Login route
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard')) # Redirect to a protected route
        else:
            flash('Login unsuccessful. Please check your credentials.', 'danger')
    return render_template('login.html', title='Login', form=form)
from functools import wraps

# Custom decorator for admin routes
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            return abort(403) # Unauthorized
        return f(*args, **kwargs)
    return decorated_function
def save_entry():
    entry_text = entry.get("3.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if file_path:
        with open(file_path, "w") as file:
            file.write(entry_text)

def load_entry():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if file_path:
        with open(file_path, "r") as file:
            entry_text = file.read()
            entry.delete("1.0", "end")
            entry.insert("1.0", entry_text)

def insert_emoji(emoji_text):
    entry.insert(tk.INSERT, emoji.emojize(emoji_text, use_aliases=True))

root = tk.Tk()
root.title("Personal Diary")

label = tk.Label(root, text="My Personal Diary")
label.pack()

entry = Text(root, height=40, width=60)
entry.pack()

save_button = Button(root, text="Save Entry", command=save_entry)
save_button.pack()

load_button = Button(root, text="Load Entry", command=load_entry)
load_button.pack()

next_button = tk.Button(root, text="Next Entry", command=read_entries)
next_button.pack()

# Emoji Picker Buttons
emoji_buttons = [
    "😀", "😃", "😄", "😁", "😆",
    "😅", "😂", "🤣", "😊", "😇"
]

for emoji_text in emoji_buttons:
    emoji_button = Button(root, text=emoji_text, command=lambda t=emoji_text: insert_emoji(t))
    emoji_button.pack(side=tk.LEFT)

root.mainloop()