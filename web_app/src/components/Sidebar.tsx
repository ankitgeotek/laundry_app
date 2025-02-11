// src/components/Sidebar.tsx
/**
 * Sidebar Component.
 *
 * Renders the navigation sidebar with links. If the sidebar is toggled off,
 * it returns null (i.e. does not render).
 */

import React from 'react';
import { Link } from 'react-router-dom';

interface SidebarProps {
  isOpen: boolean;
}

const Sidebar = ({ isOpen }: SidebarProps) => {
  if (!isOpen) return null; // If sidebar is hidden, render nothing.
  return (
    <aside className="sidebar">
      <nav>
        <ul>
          <li><Link to="/home">Home</Link></li>
          <li><Link to="/profile">Profile</Link></li>
          <li><Link to="/about">About</Link></li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
