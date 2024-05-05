import React, { useState } from 'react';
import axios from 'axios';

function AddPersonForm() {
  const [formData, setFormData] = useState({
    name: '',
    governmentId: '',
    email: '',
    debtAmount: '',
    debtDueDate: ''
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/charges/', formData);
      console.log('Person created:', response.data);
      // Lógica adicional, como limpar o formulário ou atualizar a lista de pessoas
    } catch (error) {
      console.error('Error creating person:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="name" placeholder="Name" value={formData.name} onChange={handleChange} />
      <input type="text" name="governmentId" placeholder="Government ID" value={formData.governmentId} onChange={handleChange} />
      <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} />
      <input type="number" name="debtAmount" placeholder="Debt Amount" value={formData.debtAmount} onChange={handleChange} />
      <input type="date" name="debtDueDate" placeholder="Debt Due Date" value={formData.debtDueDate} onChange={handleChange} />
      <button type="submit">Add Person</button>
    </form>
  );
}

export default AddPersonForm;
