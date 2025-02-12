// src/components/Header.tsx
/**
 * Header Component.
 *
 * Renders the application header with:
 * - A button to toggle the sidebar.
 * - A welcome message displaying the logged-in user's name.
 * - A theme toggle button.
 * - A cart icon that navigates to the cart page.
 */
import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import ThemeToggle from './ThemeToggle';
import CartIcon from './CartIcon';
import { AuthContext } from '../context/AuthContext';
import './Header.css';

interface HeaderProps {
  onToggleSidebar: () => void;
  toggleTheme: () => void;
  theme: 'light' | 'dark';
}

const Header: React.FC<HeaderProps> = ({ onToggleSidebar, toggleTheme, theme }) => {
  const { user } = useContext(AuthContext);

  return (
    <header className="header">
      <button onClick={onToggleSidebar} className="toggle-sidebar-button">
        ☰
      </button>
      <div className="header-middle">
        <h1>My Web App</h1>
        {user && user.name && <span className="welcome-message">Welcome, {user.name}!</span>}
      </div>
      <div className="header-right">
        <ThemeToggle theme={theme} toggleTheme={toggleTheme} />
        <CartIcon />
      </div>
    </header>
  );
};

export default Header;
