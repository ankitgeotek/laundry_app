// src/pages/HomePage.tsx
/**
 * HomePage Component.
 *
 * Fetches and displays all available services using the ServiceCard component.
 * Services are displayed in a responsive grid.
 */
import React, { useEffect, useState } from 'react';
import { fetchServices } from '../services/api';
import { ServiceResponseSchema } from '../validators/service_validator';
import ServiceCard from '../components/ServiceCard';
import './HomePage.css';

const HomePage: React.FC = () => {
  const [services, setServices] = useState<ServiceResponseSchema[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    const loadServices = async () => {
      try {
        const data = await fetchServices();
        setServices(data);
      } catch (err: any) {
        console.error('Error fetching services:', err);
        setError(err.detail || 'Failed to fetch services.');
      } finally {
        setLoading(false);
      }
    };
    loadServices();
  }, []);

  if (loading) {
    return <div>Loading services...</div>;
  }
  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="home-container">
      <h1>Our Services</h1>
      <div className="services-grid">
        {services.map((service) => (
          <ServiceCard key={service.id} service={service} />
        ))}
      </div>
    </div>
  );
};

export default HomePage;
