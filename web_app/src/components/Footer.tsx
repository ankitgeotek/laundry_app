// src/components/Footer.tsx
/**
 * Footer Component.
 *
 * Renders the footer content for the web application.
 */

import React, { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

const Footer = () => {
  const { logout } = useContext(AuthContext);
  const navigate = useNavigate(); // FIXED: Declare navigate

  const handleLogout = () => {
    logout();
    navigate('/login'); // FIXED: navigate is now defined
  };

  return (
    <footer className="footer">
      <p>&copy; 2025 My Web App. All rights reserved.</p>
      <p>Contact: support@example.com</p>
      <button style={styles.button} onClick={handleLogout}>Log Out</button>
    </footer>
  );
};

const styles = {
  button: { padding: '10px 20px', fontSize: '16px', cursor: 'pointer' },
};

export default Footer;
