import React, { useState } from 'react';
import axios from 'axios';

import "./FormPage/FormPage.css"

function AddPersonForm() {
    const [formData, setFormData] = useState({
        name: '',
        governmentId: '',
        email: '',
        debtAmount: '',
        debtDueDate: ''
    });

    const [submitSuccess, setSubmitSuccess] = useState(false);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/charges/', formData)
            .then(response => {
                console.log(response.data);
                setSubmitSuccess(true);
            })
            .catch(error => {
                console.error('Error creating charge:', error);
            });
    };

    return (
        <div> 
            {submitSuccess && <p>Dados enviados com sucesso!</p>}
            <form onSubmit={handleSubmit}>
                <input type="text" name="name" placeholder="Name" onChange={handleChange} />
                <input type="text" name="governmentId" placeholder="Government ID" onChange={handleChange} />
                <input type="email" name="email" placeholder="Email" onChange={handleChange} />
                <input type="number" name="debtAmount" placeholder="Debt Amount" onChange={handleChange} />
                <input type="date" name="debtDueDate" placeholder="Debt Due Date" onChange={handleChange} />
                <button type="submit">Create Charge</button>
            </form>
        </div>
    );
}

export default AddPersonForm;