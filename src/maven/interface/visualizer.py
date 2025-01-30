import matplotlib.pyplot as plt
import numpy as np

class WaifuRenderer:
    def __init__(self, name: str, mood: str = "neutral"):
        """Initialize the visualizer with character name and mood."""
        self.name = name
        self.mood = mood
    
    def render_mood(self):
        """Display a simple visualization of the waifu's mood."""
        mood_colors = {
            "happy": "green",
            "neutral": "blue",
            "sad": "gray",
            "angry": "red"
        }
        color = mood_colors.get(self.mood, "black")
        
        fig, ax = plt.subplots()
        circle = plt.Circle((0.5, 0.5), 0.4, color=color)
        ax.add_patch(circle)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"{self.name} is feeling {self.mood}")
        plt.show()