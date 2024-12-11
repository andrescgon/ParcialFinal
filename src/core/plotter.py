import math
import numpy as np

class AdvancedPlotter:
    def __init__(self, width=80, height=30):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
    
    def plot_function(self, func, x_min, x_max, num_points=200):
        """
        Plot a continuous function by generating multiple points
        
        Args:
        - func: A function that takes x as input and returns y
        - x_min: Minimum x value to plot
        - x_max: Maximum x value to plot
        - num_points: Number of points to sample for smooth plotting
        """
        # Generate evenly spaced points
        x_values = np.linspace(x_min, x_max, num_points)
        y_values = [func(x) for x in x_values]
        
        # Calculate plot boundaries
        self.x_min, self.x_max = x_min, x_max
        self.y_min = min(y_values)
        self.y_max = max(y_values)
        
        # Add some padding
        y_range = self.y_max - self.y_min
        self.y_min -= y_range * 0.1
        self.y_max += y_range * 0.1
   
        
        # Plot points
        for x, y in zip(x_values, y_values):
            x_scaled = int((x - self.x_min) / (self.x_max - self.x_min) * (self.width - 1))
            y_scaled = int((y - self.y_min) / (self.y_max - self.y_min) * (self.height - 1))

            # Ensure we're within canvas bounds
            if 0 <= x_scaled < self.width and 0 <= y_scaled < self.height:
                self.canvas[self.height - 1 - y_scaled][x_scaled] = '*'
    
    def plot_scatter(self, data):
        """
        Plot scattered data points
        
        Args:
        - data: List of (x, y) tuples
        """
        if not data:
            raise ValueError("No data provided")
        
        x_values, y_values = zip(*data)
        
        # Calculate plot boundaries
        self.x_min, self.x_max = min(x_values), max(x_values)
        self.y_min, self.y_max = min(y_values), max(y_values)
        
        # Add some padding
        x_range = self.x_max - self.x_min
        y_range = self.y_max - self.y_min
        
        self.x_min -= x_range * 0.1
        self.x_max += x_range * 0.1
        self.y_min -= y_range * 0.1
        self.y_max += y_range * 0.1
        
        for x, y in data:
            x_scaled = int((x - self.x_min) / (self.x_max - self.x_min) * (self.width - 1))
            y_scaled = int((y - self.y_min) / (self.y_max - self.y_min) * (self.height - 1))
            
            # Ensure we're within canvas bounds
            if 0 <= x_scaled < self.width and 0 <= y_scaled < self.height:
                self.canvas[self.height - 1 - y_scaled][x_scaled] = '*'
    
    def _draw_axes(self):
        """
        Draw coordinate axes with grid and labels
        """
        # Draw horizontal axis
        x_zero = int((-self.x_min) / (self.x_max - self.x_min) * (self.width - 1))
        y_zero = int((-self.y_min) / (self.y_max - self.y_min) * (self.height - 1))

        for col in range(self.width):
            row_index = self.height - 1 - y_zero
            if 0 <= row_index < self.height:
                self.canvas[row_index][col] = '-'
        
        # Draw vertical axis
        for row in range(self.height):
            col_index = x_zero
            if 0 <= col_index < self.width:
                self.canvas[row][col_index] = '|'
        
        # Mark origin
        if 0 <= y_zero < self.height and 0 <= x_zero < self.width:
            self.canvas[self.height - 1 - y_zero][x_zero] = '+'
        
        # Add x-axis labels
        x_step = (self.x_max - self.x_min) / 10
        for i in range(11):
            x = self.x_min + i * x_step
            x_pos = int((x - self.x_min) / (self.x_max - self.x_min) * (self.width - 1))
            
            label = f'{x:.2f}'
            if 0 <= x_pos < self.width and y_zero + 1 < self.height:
                for j, char in enumerate(label):
                    if x_pos + j < self.width:
                        self.canvas[self.height - 1 - y_zero + 1][x_pos + j] = char
        
        # Add y-axis labels
        y_step = (self.y_max - self.y_min) / 5
        for i in range(6):
            y = self.y_max - i * y_step
            y_pos = int((y - self.y_min) / (self.y_max - self.y_min) * (self.height - 1))
            
            label = f'{y:.2f}'
            if 0 <= y_pos < self.height and x_zero > 0:
                for j, char in enumerate(label):
                    if x_zero - len(label) + j >= 0:
                        self.canvas[self.height - 1 - y_pos][x_zero - len(label) + j] = char
    
    def display(self):
        """
        Draw axes and display the plot
        """
        self._draw_axes()
        for row in self.canvas:
            print(''.join(row))
