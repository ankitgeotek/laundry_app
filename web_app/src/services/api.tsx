// src/services/api.ts
/**
 * API Service Module.
 *
 * Uses Axios to centralize API requests and automatically attach the authentication token.
 * Contains functions for authentication, service fetching, and cart operations.
 */
import axios from 'axios';
import { ServiceResponseSchema } from '../validators/service_validator';

const API_BASE_URL = import.meta.env.VITE_API_URL; // Imported from .env

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
});

// Attach token to every request if available.
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('userToken');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Fetch services
export const fetchServices = async (): Promise<ServiceResponseSchema[]> => {
  try {
    const response = await apiClient.get('/services/');
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};

// Authentication APIs
export const loginApi = async (email: string, password: string) => {
  try {
    const response = await apiClient.post('/auth/login', { email, password });
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};

export const signupApi = async (userData: Record<string, string>) => {
  try {
    const response = await apiClient.post('/auth/signup', userData);
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};

// Cart operations
export const addCartItem = async (cartData: {
  service_id: number;
  quantity?: number;
  custom_instructions?: string;
}): Promise<any> => {
  try {
    const response = await apiClient.post('/cart/', cartData);
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};

export const fetchCartItems = async (): Promise<any[]> => {
  try {
    const response = await apiClient.get('/cart/');
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};

export const updateCartItem = async (itemId: number, data: any): Promise<any> => {
  try {
    const response = await apiClient.put(`/cart/${itemId}`, data);
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};

export const deleteCartItem = async (itemId: number): Promise<any> => {
  try {
    const response = await apiClient.delete(`/cart/${itemId}`);
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};

export const clearCart = async (): Promise<any> => {
  try {
    const response = await apiClient.delete(`/cart/clear`);
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};

export const getCartTotal = async (): Promise<number> => {
  try {
    const response = await apiClient.get(`/cart/total`);
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};
