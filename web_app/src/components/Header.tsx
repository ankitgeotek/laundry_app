// src/components/Header.tsx
/**
 * Header Component.
 *
 * Renders the application header with a sidebar toggle button and a theme toggle button.
 * The theme toggle button is implemented using the ThemeToggle component.
 *
 * Props:
 * - onToggleSidebar: Callback function to toggle the sidebar.
 * - toggleTheme: Callback function to toggle between light and dark mode.
 * - theme: The current theme.
 */
import React from 'react';
import ThemeToggle from './ThemeToggle';

interface HeaderProps {
  onToggleSidebar: () => void;
  toggleTheme: () => void;
  theme: 'light' | 'dark';
}

const Header: React.FC<HeaderProps> = ({ onToggleSidebar, toggleTheme, theme }) => {
  return (
    <header className="header">
      <button onClick={onToggleSidebar} className="toggle-sidebar-button">
        ☰
      </button>
      <h1>--- Indian Laundry House ---</h1>
      {/* Use the ThemeToggle component for switching theme */}
      <ThemeToggle theme={theme} toggleTheme={toggleTheme} />
    </header>
  );
};

export default Header;
