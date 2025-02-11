// src/services/api.ts
/**
 * API service module.
 *
 * Uses Axios to centralize API requests and automatically attaches the authentication token.
 */
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000'; // Replace with your actual backend URL

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000, // 10 seconds timeout
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to attach the token (if available)
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

/**
 * fetchServices: Retrieves all available services from the backend.
 *
 * Assumes the endpoint returns an array of service objects.
 *
 * @returns {Promise<ServiceResponseSchema[]>} A promise that resolves to an array of services.
 */
export const fetchServices = async (): Promise<ServiceResponseSchema[]> => {
  try {
    const response = await apiClient.get('/services/');
    // If the endpoint returns an array directly, we can return response.data.
    return response.data;
  } catch (error: any) {
    throw error.response ? error.response.data : error;
  }
};

/**
 * Existing API functions for login and signup can remain here...
 */
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

// Import the response schema type (defined in validators/service_validator.ts)
import { ServiceResponseSchema } from '../validators/service_validator';
