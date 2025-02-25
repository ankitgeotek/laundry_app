// src/components/Layout.tsx
/**
 * Layout Component.
 *
 * Combines the Header, Sidebar, Main content, and Footer components.
 * The Header includes a welcoming message and a cart link.
 */
import React, { useState, useContext } from 'react';
import Header from './Header';
import Sidebar from './Sidebar';
import Footer from './Footer';
import { ThemeContext } from '../context/ThemeContext';
import './Layout.css';

const Layout = ({ children }: { children: React.ReactNode }) => {
  const { theme, toggleTheme } = useContext(ThemeContext);
  const [sidebarOpen, setSidebarOpen] = useState<boolean>(true);

  const handleToggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <div className={`layout-container ${theme}`}>
      <Header
        onToggleSidebar={handleToggleSidebar}
        toggleTheme={toggleTheme}
        theme={theme}
      />
      <div className="content-area">
        <Sidebar isOpen={sidebarOpen} />
        <main className="main">{children}</main>
      </div>
      <Footer />
    </div>
  );
};

export default Layout;
