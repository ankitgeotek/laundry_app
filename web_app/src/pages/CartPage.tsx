// src/pages/CartPage.tsx
/**
 * CartPage Component.
 *
 * Displays all cart items for the authenticated user, handles empty cart cases,
 * shows a summary including total price, and provides buttons to proceed to checkout or clear the cart.
 */
import React, { useEffect, useState } from 'react';
import { fetchCartItems, clearCart, getCartTotal } from '../services/api';
import CartItem from '../components/CartItem';
import './CartPage.css';


const CartPage: React.FC = () => {
  const [items, setItems] = useState<any[]>([]);
  const [total, setTotal] = useState<number>(0);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>('');

  const loadCart = async () => {
    setLoading(true);
    try {
      const data = await fetchCartItems();
      setItems(data);
      const totalPrice = await getCartTotal();
      setTotal(totalPrice);
    } catch (err: any) {
      console.error('Error fetching cart items:', err);
      setError(err.detail || 'Failed to fetch cart items.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadCart();
  }, []);

  const handleClearCart = async () => {
    try {
      await clearCart();
      loadCart();
    } catch (error) {
      console.error('Error clearing cart:', error);
    }
  };

  if (loading) return <div>Loading cart...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="cart-page">
      <h1>Your Cart</h1>
      {items.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          <div className="cart-items">
            {items.map((item) => (
              <CartItem key={item.id} item={item} onUpdate={loadCart} />
            ))}
          </div>
          <div className="cart-summary">
            <h2>Total: ${total.toFixed(2)}</h2>
            <button className="checkout-button" onClick={() => alert('Proceeding to checkout...')}>
              Proceed to Checkout
            </button>
            <button className="clear-button" onClick={handleClearCart}>
              Clear Cart
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default CartPage;
