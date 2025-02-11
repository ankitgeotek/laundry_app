// src/components/CartItem.tsx
/**
 * CartItem Component.
 *
 * Displays a single cart item with service details, quantity, and controls to update or remove the item.
 *
 * Props:
 * - item: The cart item object.
 * - onUpdate: Callback to refresh the cart data.
 */
import React, { useState } from 'react';
import { updateCartItem, deleteCartItem } from '../services/api';
import './CartItem.css';

interface CartItemProps {
  item: any; // Ideally, define an interface for cart items.
  onUpdate: () => void;
}

const CartItem: React.FC<CartItemProps> = ({ item, onUpdate }) => {
  const [quantity, setQuantity] = useState<number>(item.quantity);
  const [loading, setLoading] = useState<boolean>(false);

  const handleUpdate = async () => {
    setLoading(true);
    try {
      await updateCartItem(item.id, { quantity });
      onUpdate();
    } catch (error) {
      console.error('Error updating cart item:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async () => {
    setLoading(true);
    try {
      await deleteCartItem(item.id);
      onUpdate();
    } catch (error) {
      console.error('Error deleting cart item:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="cart-item">
      <div className="cart-item-info">
        <h3>{item.service.name}</h3>
        {item.service.image_url && (
          <img src={item.service.image_url} alt={item.service.name} className="cart-item-image" />
        )}
        <p>{item.service.description}</p>
        <p>Price: ${item.service.base_price.toFixed(2)}</p>
      </div>
      <div className="cart-item-controls">
        <label>
          Quantity:
          <input
            type="number"
            min="1"
            value={quantity}
            onChange={(e) => setQuantity(Number(e.target.value))}
          />
        </label>
        <button onClick={handleUpdate} disabled={loading}>Update</button>
        <button onClick={handleDelete} disabled={loading}>Remove</button>
      </div>
    </div>
  );
};

export default CartItem;
