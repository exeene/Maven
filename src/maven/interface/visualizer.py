import matplotlib.pyplot as plt
import numpy as np
from flask import render_template_string

class MarketVisualizer:
    def __init__(self, name: str, mood: str = "neutral"):
        self.name = name
        self.mood = mood
        self.web_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                .waifu-container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    background-color: {{ color }};
                }
                h2 {
                    color: white;
                    font-family: Arial, sans-serif;
                }
            </style>
        </head>
        <body>
            <div class="waifu-container">
                <h2>{{ name }} - {{ mood }}</h2>
                <div class="visual" style="background: {{ color }};"></div>
            </div>
        </body>
        </html>
        """
    
    def web_render(self):
        """Generate WebGL-compatible output"""
        mood_colors = self._get_mood_colors()
        return render_template_string(
            self.web_template,
            name=self.name,
            mood=self.mood,
            color=mood_colors.get(self.mood, "#000")
        )
    
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
    
    def _get_mood_colors(self) -> dict:
        """Internal method to map moods to colors."""
        return {
            "happy": "#00FF00",  # Green
            "neutral": "#0000FF",  # Blue
            "sad": "#808080",  # Gray
            "angry": "#FF0000"  # Red
        }
    
    # New Feature: Mood Transition Animation
    def animate_mood_transition(self, new_mood: str, steps: int = 10):
        """
        Animate a transition from the current mood to a new mood.
        Args:
            new_mood: The target mood to transition to.
            steps: Number of steps in the animation.
        """
        current_color = self._get_mood_colors().get(self.mood, "#000")
        target_color = self._get_mood_colors().get(new_mood, "#000")
        
        # Convert hex colors to RGB tuples
        current_rgb = tuple(int(current_color[i:i+2], 16) for i in (1, 3, 5))
        target_rgb = tuple(int(target_color[i:i+2], 16) for i in (1, 3, 5))
        
        # Generate intermediate colors
        for step in range(steps + 1):
            r = current_rgb[0] + (target_rgb[0] - current_rgb[0]) * step // steps
            g = current_rgb[1] + (target_rgb[1] - current_rgb[1]) * step // steps
            b = current_rgb[2] + (target_rgb[2] - current_rgb[2]) * step // steps
            
            intermediate_color = f"#{r:02x}{g:02x}{b:02x}"
            
            # Update mood and render
            self.mood = f"transitioning to {new_mood}" if step < steps else new_mood
            self.render_mood()
            plt.pause(0.2)  # Pause for animation effect

    def visualize_heatmap(self, portfolio_data):
        heatmap_data = self.prepare_heatmap_data(portfolio_data)
        plt.imshow(heatmap_data, cmap='coolwarm')
        plt.colorbar()
        plt.show()

    def prepare_heatmap_data(self, portfolio_data):
        # Prepare data for heatmap visualization
        pass