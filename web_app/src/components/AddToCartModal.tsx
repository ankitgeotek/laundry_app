// src/components/AddToCartModal.tsx
/**
 * AddToCartModal Component.
 *
 * Displays a modal dialog prompting the user to input the quantity (integer)
 * and any specific instructions for adding a service to the cart.
 * It uses React portals so that the modal is rendered as a child of #modal-root.
 * Features a confirm button at the bottom and a cancel (close) button at the top right.
 *
 * Props:
 * - visible: Boolean indicating whether the modal is visible.
 * - onConfirm: Callback function called with (quantity, instructions) when confirmed.
 * - onCancel: Callback function called when the modal is canceled/closed.
 */
import React, { useState, useEffect, useContext } from 'react';
import ReactDOM from 'react-dom';
import { ThemeContext } from '../context/ThemeContext';
import './AddToCartModal.css';

interface AddToCartModalProps {
  visible: boolean;
  onConfirm: (quantity: number, instructions: string) => void;
  onCancel: () => void;
}

const AddToCartModal: React.FC<AddToCartModalProps> = ({ visible, onConfirm, onCancel }) => {
  const { theme } = useContext(ThemeContext);
  const [quantity, setQuantity] = useState<number>(1);
  const [instructions, setInstructions] = useState<string>('');

  useEffect(() => {
    if (visible) {
      setQuantity(1);
      setInstructions('');
    }
  }, [visible]);

  if (!visible) return null;

  return ReactDOM.createPortal(
    <div className="modal-overlay">
      <div className={`modal-container ${theme}`}>
        <div className="modal-header">
          <h2 className="modal-title">Add to Cart</h2>
          <button className="modal-close-button" onClick={onCancel} aria-label="Close">
            ×
          </button>
        </div>
        <div className="modal-body">
          <label className="modal-label">
            Quantity:
            <input
              type="number"
              min="1"
              value={quantity}
              onChange={(e) => setQuantity(Number(e.target.value))}
              className="modal-input"
            />
          </label>
          <label className="modal-label">
            Instructions (optional):
            <textarea
              value={instructions}
              onChange={(e) => setInstructions(e.target.value)}
              placeholder="Enter any specific instructions..."
              className="modal-textarea"
            />
          </label>
        </div>
        <div className="modal-footer">
          <button className="modal-confirm-button" onClick={() => onConfirm(quantity, instructions)}>
            Confirm
          </button>
        </div>
      </div>
    </div>,
    document.getElementById('modal-root')!
  );
};

export default AddToCartModal;
