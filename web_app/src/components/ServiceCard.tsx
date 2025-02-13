// src/components/ServiceCard.tsx
import React, { useState, useContext } from 'react';
import { ServiceResponseSchema } from '../validators/service_validator';
import { addCartItem } from '../services/api';
import AddToCartModal from './AddToCartModal';
import { CartContext } from '../context/CartContext';
import './ServiceCard.css';

interface ServiceCardProps {
  service: ServiceResponseSchema;
}

const ServiceCard: React.FC<ServiceCardProps> = ({ service }) => {
  const [modalVisible, setModalVisible] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  const { refreshCart } = useContext(CartContext);

  const openModal = () => setModalVisible(true);
  const closeModal = () => setModalVisible(false);

  const handleConfirm = async (quantity: number, instructions: string) => {
    setLoading(true);
    setError('');
    try {
      await addCartItem({ service_id: service.id, quantity, custom_instructions: instructions });
      alert('Service added to cart!');
      refreshCart(); // Update the global cart count
      closeModal();
    } catch (err: any) {
      console.error('Error adding service to cart:', err);
      setError(err.detail || 'Failed to add service to cart.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="service-card">
      {service.image_url && (
        <img src={service.image_url} alt={service.name} className="service-image" />
      )}
      <div className="service-content">
        <h2 className="service-name">{service.name}</h2>
        {service.description && <p className="service-description">{service.description}</p>}
        <p className="service-price">Price: ${service.base_price.toFixed(2)}</p>
        {service.category && <p className="service-category">Category: {service.category}</p>}
        {error && <p className="error">{error}</p>}
        <button onClick={openModal} className="add-to-cart-button">
          Add to Cart
        </button>
      </div>
      <AddToCartModal visible={modalVisible} onConfirm={handleConfirm} onCancel={closeModal} />
    </div>
  );
};

export default ServiceCard;
