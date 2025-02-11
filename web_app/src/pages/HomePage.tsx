// src/pages/HomePage.tsx
/**
 * HomePage Component.
 *
 * Fetches and displays all available services using the ServiceCard component.
 * This component is displayed once the customer has logged in.
 */

import React, { useEffect, useState } from 'react';
import { fetchServices } from '../services/api';
import { ServiceResponseSchema } from '../validators/service_validator';
import ServiceCard from '../components/ServiceCard';
import './HomePage.css'; // Optional: CSS for HomePage layout

// Define the expected service type separately
type ServiceType = {
  id: number;
  name: string;
  description: string;
  price: number;
  category?: string;
};

const HomePage: React.FC = () => {
  // State to hold the list of services.
  const [services, setServices] = useState<ServiceType[]>([]); // FIXED: Use explicit type instead of Zod schema
  // State to manage the loading indicator.
  const [loading, setLoading] = useState<boolean>(true);
  // State to store error messages.
  const [error, setError] = useState<string | null>(null); // Use null for better type safety

  // Fetch services when the component mounts.
  useEffect(() => {
    const getServices = async () => {
      try {
        const data = await fetchServices();
        setServices(data);
      } catch (err: unknown) {
        console.error('Error fetching services:', err);
        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError('Failed to fetch services.');
        }
      } finally {
        setLoading(false);
      }
    };
    getServices();
  }, []);

  // Show a loading state while fetching data.
  if (loading) {
    return <div>Loading services...</div>;
  }

  // Show an error message if there's an error.
  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="home-container">
      <h1>Select Services</h1>
      <div className="services-grid">
        {services.map((service) => (
          <ServiceCard key={service.id} service={service} />
        ))}
      </div>
    </div>
  );
};

export default HomePage;
