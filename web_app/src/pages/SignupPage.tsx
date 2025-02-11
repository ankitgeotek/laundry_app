// src/pages/SignupPage.tsx
/**
 * SignupPage component.
 *
 * Renders a registration form and handles user signup.
 */
import React, { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import { useNavigate, Link } from 'react-router-dom';

const SignupPage = () => {
  const { signup } = useContext(AuthContext);
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    phone: '',
    address: ''
  });
  const [errorMsg, setErrorMsg] = useState<string>('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await signup(formData);
      alert('Signup successful! Please log in.');
      navigate('/login');
    } catch (error: any) {
      setErrorMsg(error.detail || 'Signup failed. Please try again.');
    }
  };

  return (
    <div style={styles.container}>
      <h2>Sign Up</h2>
      {errorMsg && <p style={styles.error}>{errorMsg}</p>}
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          style={styles.input}
          type="text"
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          style={styles.input}
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          style={styles.input}
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <input
          style={styles.input}
          type="text"
          name="phone"
          placeholder="Phone"
          value={formData.phone}
          onChange={handleChange}
        />
        <input
          style={styles.input}
          type="text"
          name="address"
          placeholder="Address"
          value={formData.address}
          onChange={handleChange}
        />
        <button style={styles.button} type="submit">Sign Up</button>
      </form>
      <p>
        Already have an account? <Link to="/login">Log In</Link>
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

export default SignupPage;
