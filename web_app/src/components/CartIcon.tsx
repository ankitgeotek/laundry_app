// src/components/CartIcon.tsx
/**
 * CartIcon Component.
 *
 * Displays a cart icon with a badge showing the number of items.
 * Uses CartContext so that it always reflects the current cart count.
 * When clicked, navigates the user to the cart page.
 */
import React, { useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { CartContext } from '../context/CartContext';
import './CartIcon.css';

const CartIcon: React.FC = () => {
  const { cartCount, refreshCart } = useContext(CartContext);
  const navigate = useNavigate();

  // Optionally, refresh the cart count when the window gains focus.
  useEffect(() => {
    const handleFocus = () => {
      refreshCart();
    };
    window.addEventListener('focus', handleFocus);
    return () => {
      window.removeEventListener('focus', handleFocus);
    };
  }, [refreshCart]);

  return (
    <div className="cart-icon" onClick={() => navigate('/cart')}>
      <span role="img" aria-label="cart">🛒</span>
      {cartCount > 0 && <span className="cart-badge">{cartCount}</span>}
    </div>
  );
};

export default CartIcon;
