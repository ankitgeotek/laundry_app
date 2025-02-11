// src/context/AuthContext.tsx
/**
 * AuthContext Module.
 *
 * Provides authentication state and functions (login, signup, logout).
 * Now stores user details (token and name) so that the header can display a welcome message.
 */

import React, { createContext, useState, useEffect, ReactNode } from 'react';
import { loginApi, signupApi } from '../services/api';

interface User {
  token: string;
  name: string;
  // Additional fields as needed.
}

interface AuthContextProps {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<any>;
  signup: (userData: Record<string, string>) => Promise<any>;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextProps>({
  user: null,
  loading: true,
  login: async () => {},
  signup: async () => {},
  logout: () => {}
});

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  // On mount, load the stored token and user name.
  useEffect(() => {
    const loadUserData = () => {
      try {
        const userToken = localStorage.getItem('userToken');
        const userName = localStorage.getItem('userName');
        if (userToken && userName) {
          setUser({ token: userToken, name: userName });
        }
      } catch (error) {
        console.error('Error loading user token:', error);
      } finally {
        setLoading(false);
      }
    };
    loadUserData();
  }, []);

  const login = async (email: string, password: string) => {
    try {
      const response = await loginApi(email, password);
      // Expect the response to include access_token and a user object with a name.
      if (response.access_token && response.user) {
        setUser({ token: response.access_token, name: response.user.name });
        localStorage.setItem('userToken', response.access_token);
        localStorage.setItem('userName', response.user.name);
      }
      return response;
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  };

  const signup = async (userData: Record<string, string>) => {
    try {
      const response = await signupApi(userData);
      return response;
    } catch (error) {
      console.error('Signup error:', error);
      throw error;
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('userToken');
    localStorage.removeItem('userName');
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, signup, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
