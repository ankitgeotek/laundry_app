// src/components/CartIcon.tsx
/**
 * CartIcon Component.
 *
 * Displays a cart icon with a badge showing the number of items in the cart.
 * When clicked, navigates the user to the cart page.
 */
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { fetchCartItems } from '../services/api';
import './CartIcon.css';

const CartIcon: React.FC = () => {
  const [count, setCount] = useState<number>(0);
  const navigate = useNavigate();

  // Fetch cart items count on mount.
  useEffect(() => {
    const loadCount = async () => {
      try {
        const items = await fetchCartItems();
        const total = items.reduce((acc: number, item: any) => acc + item.quantity, 0);
        setCount(total);
      } catch (error) {
        console.error('Error fetching cart items:', error);
      }
    };
    loadCount();
  }, []);

  return (
    <div className="cart-icon" onClick={() => navigate('/cart')}>
      <span role="img" aria-label="cart">🛒</span>
      {count > 0 && <span className="cart-badge">{count}</span>}
    </div>
  );
};

export default CartIcon;
