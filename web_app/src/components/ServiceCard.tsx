// src/components/ServiceCard.tsx
/**
 * ServiceCard Component.
 *
 * Displays a single service, including its image (if provided), name, description, price, and category.
 * This component is built using basic React, HTML, and CSS for maximum customization.
 *
 * Props:
 * - service: An object representing a service, matching the ServiceResponseSchema interface.
 */

import React from 'react';
import { ServiceResponseSchema } from '../validators/service_validator';
import './ServiceCard.css';

interface ServiceCardProps {
  service: ServiceResponseSchema;
}

const ServiceCard: React.FC<ServiceCardProps> = ({ service }) => {
  return (
    <div className="service-card">
      {service.image_url && (
        <img
          src={service.image_url}
          alt={service.name}
          className="service-image"
        />
      )}
      <div className="service-content">
        <h2 className="service-name">{service.name}</h2>
        {service.description && (
          <p className="service-description">{service.description}</p>
        )}
        <p className="service-price">Price: ${service.base_price.toFixed(2)}</p>
        {service.category && (
          <p className="service-category">Category: {service.category}</p>
        )}
      </div>
    </div>
  );
};

export default ServiceCard;
