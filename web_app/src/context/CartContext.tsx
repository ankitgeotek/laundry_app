// src/context/CartContext.tsx
/**
 * CartContext Module.
 *
 * Provides global state for the cart count and a function to refresh the cart count
 * by fetching the latest cart items from the backend.
 */

import React, { createContext, useState, useEffect, ReactNode, useCallback } from 'react';
import { fetchCartItems } from '../services/api';

export interface CartContextProps {
  cartCount: number;
  refreshCart: () => void;
}

export const CartContext = createContext<CartContextProps>({
  cartCount: 0,
  refreshCart: () => {},
});

export const CartProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [cartCount, setCartCount] = useState<number>(0);

  const refreshCart = useCallback(async () => {
    try {
      const items = await fetchCartItems();
      const total = items.reduce((acc: number, item: any) => acc + item.quantity, 0);
      setCartCount(total);
    } catch (error) {
      console.error('Error refreshing cart count:', error);
    }
  }, []);

  useEffect(() => {
    refreshCart();
  }, [refreshCart]);

  return (
    <CartContext.Provider value={{ cartCount, refreshCart }}>
      {children}
    </CartContext.Provider>
  );
};
