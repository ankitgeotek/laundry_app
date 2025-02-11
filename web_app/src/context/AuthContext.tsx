// src/context/AuthContext.tsx
/**
 * Authentication context.
 * Provides state and functions for logging in, signing up, and logging out.
 */
import { createContext, useState, useEffect, ReactNode } from 'react';
import { loginApi, signupApi } from '../services/api';

interface AuthContextProps {
  user: string | null;
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

interface AuthProviderProps {
  children: ReactNode;
}

/**
 * AuthProvider wraps the application and manages authentication state.
 */
export const AuthProvider = ({ children }: AuthProviderProps) => {
  const [user, setUser] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  // Check for a stored token on mount.
  useEffect(() => {
    const loadUserData = () => {
      try {
        const token = localStorage.getItem('userToken');
        if (token) {
          setUser(token);
        }
      } catch (error) {
        console.error('Error loading user token:', error);
      } finally {
        setLoading(false);
      }
    };
    loadUserData();
  }, []);

  /**
   * Logs in the user by calling the login API.
   */
  const login = async (email: string, password: string) => {
    try {
      const response = await loginApi(email, password);
      if (response.access_token) {
        setUser(response.access_token);
        localStorage.setItem('userToken', response.access_token);
      }
      return response;
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  };

  /**
   * Signs up the user by calling the signup API.
   */
  const signup = async (userData: Record<string, string>) => {
    try {
      const response = await signupApi(userData);
      return response;
    } catch (error) {
      console.error('Signup error:', error);
      throw error;
    }
  };

  /**
   * Logs out the user by clearing the stored token.
   */
  const logout = () => {
    setUser(null);
    localStorage.removeItem('userToken');
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, signup, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
