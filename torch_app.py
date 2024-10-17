import ipywidgets as widgets
from IPython.display import display

# Define the button click functions
def turn_on(b):
    print("Torch is ON!")
    
def turn_off(b):
    print("Torch is OFF!")

# Create buttons
on_button = widgets.Button(description="Turn ON")
off_button = widgets.Button(description="Turn OFF")

# Attach the click event to the buttons
on_button.on_click(turn_on)
off_button.on_click(turn_off)

# Display the buttons
display(on_button, off_button)
