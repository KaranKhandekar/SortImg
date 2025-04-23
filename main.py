import os
import shutil
import time
import webbrowser
from tkinter import Tk, Button, Label, filedialog, messagebox
from PIL import Image

def create_folders():
    global white_background_folder, non_white_background_folder
    folder_location = filedialog.askdirectory(title="Select Folder Location")
    if folder_location:
        white_background_folder = os.path.join(folder_location, 'white_background')
        non_white_background_folder = os.path.join(folder_location, 'non_white_background')
        os.makedirs(white_background_folder, exist_ok=True)
        os.makedirs(non_white_background_folder, exist_ok=True)
        messagebox.showinfo("Folders Created", f"Folders created successfully at {folder_location}")
    else:
        messagebox.showwarning("No Location Selected", "Please select a folder location.")

def is_white_background(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            pixels = img.load()
            
            
            # Check the top right 5x5 pixels
            for x in range(width-5, width):
                for y in range(5):
                    if pixels[x, y][:3] != (255, 255, 255):  # Compare only RGB values
                        return False
            return True
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return False

def sort_images(source_folder, status_label, count_label, time_label):
    global white_background_folder, non_white_background_folder
    start_time = time.time()
    status_label.config(text="Status: In Progress")
    count = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(source_folder, filename)
            try:
                if is_white_background(image_path):
                    destination = os.path.join(white_background_folder, filename)
                else:
                    destination = os.path.join(non_white_background_folder, filename)
                
                shutil.move(image_path, destination)
                count += 1
            except Exception as e:
                print(f"Error moving file {filename}: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    status_label.config(text="Status: Idle")
    count_label.config(text=f"Images Processed: {count}")
    time_label.config(text=f"Time Taken: {elapsed_time:.2f} seconds")
    messagebox.showinfo("Process Complete", "Image sorting complete.")

def run_app():
    root = Tk()
    root.title("SortImg for Saks")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - 500) // 2
    y = (screen_height - 500) // 2

    root.geometry(f"500x500+{x}+{y}")

    root.configure(bg='#edeceb')

    # Create a frame to hold the buttons
    button_frame = Label(root, bg='#edeceb')
    button_frame.pack(expand=True)

    folder_button = Button(button_frame, text="Select Folder Location", command=create_folders, font=('Helvetica', 12), fg='black', bg='#edeceb')
    folder_button.pack(pady=10)

    def on_run():
        global white_background_folder, non_white_background_folder
        if not white_background_folder or not non_white_background_folder:
            messagebox.showwarning("Folders Not Created", "Please select folder location first.")
            return
        source_folder = filedialog.askdirectory(title="Select Source Folder")
        if source_folder:
            sort_images(source_folder, status_label, count_label, time_label)
        else:
            messagebox.showwarning("No Folder Selected", "Please select a source folder.")

    def on_how_to_use():
        webbrowser.open("https://karankhandekar.github.io/saks_sort_img/how_to_use.html")

    def on_help():
        webbrowser.open("https://karankhandekar.github.io/saks_sort_img/documentation.html")

    run_button = Button(button_frame, text="Run", command=on_run, font=('Helvetica', 12), fg='black', bg='#edeceb')
    run_button.pack(pady=10)

    how_to_use_button = Button(button_frame, text="How to Use", command=on_how_to_use, font=('Helvetica', 12), fg='black', bg='#edeceb')
    how_to_use_button.pack(pady=10)

    help_button = Button(button_frame, text="Help", command=on_help, font=('Helvetica', 12), fg='black', bg='#edeceb')
    help_button.pack(pady=10)

    status_label = Label(root, text="Status: Idle", font=('Helvetica', 12), fg='black', bg='#edeceb')
    status_label.pack(pady=10)

    count_label = Label(root, text="Images Processed: 0", font=('Helvetica', 12), fg='black', bg='#edeceb')
    count_label.pack(pady=10)

    time_label = Label(root, text="Time Taken: 0.00 seconds", font=('Helvetica', 12), fg='black', bg='#edeceb')
    time_label.pack(pady=10)

    info_label = Label(root, text="This is for internal use only", font=('Helvetica', 10), fg='black', bg='#edeceb')
    info_label.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    run_app()
