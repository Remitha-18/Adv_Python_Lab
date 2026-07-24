from tkinter import Tk, filedialog
from PIL import Image


def load_image_from_explorer():
    # Hide the main root window of tkinter
    root = Tk()
    root.withdraw()

    # Define allowed file types
    file_types = [("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp")]

    # Open the file explorer and get the selected file path
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=file_types
    )

    # Check if the user selected a file or cancelled
    if file_path:
        print(f"Loading image from: {file_path}")

        # Load the image using Pillow
        img = Image.open(file_path)

        # Display the image on your screen
        img.show()

        return img
    else:
        print("No image was selected.")
        return None


# Run the function
loaded_image = load_image_from_explorer()