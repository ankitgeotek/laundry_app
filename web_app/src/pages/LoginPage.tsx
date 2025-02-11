// src/pages/LoginPage.tsx
/**
 * LoginPage component.
 *
 * Renders a login form and handles login submission.
 */
import React, { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import { useNavigate, Link } from 'react-router-dom';

const LoginPage = () => {
  const { login } = useContext(AuthContext);
  const navigate = useNavigate();
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [errorMsg, setErrorMsg] = useState<string>('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await login(email, password);
      navigate('/home');
    } catch (error: any) {
      setErrorMsg(error.detail || 'Login failed. Please check your credentials.');
    }
  };

  return (
    <div style={styles.container}>
      <h2>Login</h2>
      {errorMsg && <p style={styles.error}>{errorMsg}</p>}
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          style={styles.input}
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          style={styles.input}
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button style={styles.button} type="submit">Log In</button>
      </form>
      <p>
        Don't have an account? <Link to="/signup">Sign Up</Link>
      </p>
    </div>
  );
};

const styles = {
  container: { maxWidth: '400px', margin: '2rem auto', textAlign: 'center' },
  form: { display: 'flex', flexDirection: 'column' },
  input: { padding: '10px', marginBottom: '10px', fontSize: '16px' },
  button: { padding: '10px', fontSize: '16px', cursor: 'pointer' },
  error: { color: 'red' },
};

export default LoginPage;
