// src/components/ThemeToggle.tsx
/**
 * ThemeToggle Component.
 *
 * Renders a stylish toggle switch that lets the user switch between light and dark modes.
 * The toggle's checked state is determined by the current theme (if 'dark', the switch is on).
 *
 * Props:
 * - theme: The current theme ('light' or 'dark').
 * - toggleTheme: A callback function to toggle the theme.
 *
 * Example usage:
 *   <ThemeToggle theme={theme} toggleTheme={toggleTheme} />
 */
import React from 'react';
import './ThemeToggle.css'; // Import the associated CSS styles

interface ThemeToggleProps {
  theme: 'light' | 'dark';
  toggleTheme: () => void;
}

const ThemeToggle: React.FC<ThemeToggleProps> = ({ theme, toggleTheme }) => {
  return (
    <div className="toggle-container">
      <label className="switch">
        {/* 
          The input's checked property is true when the theme is 'dark'.
          When the user toggles the switch, the toggleTheme function is called.
        */}
        <input
          type="checkbox"
          onChange={toggleTheme}
          checked={theme === 'dark'}
        />
        <span className="slider round"></span>
      </label>
    </div>
  );
};

export default ThemeToggle;
