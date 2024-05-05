import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PersonList() {
  const [persons, setPersons] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/charges/')
      .then(response => {
        setPersons(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h2>Sistema de Cobranças</h2>
      <ul>
        {persons.map(person => (
          <li key={person.id}>
            <strong>Nome:</strong> {person.name}<br />
            <strong>Documento:</strong> {person.governmentId}<br />
            <strong>Email:</strong> {person.email}<br />
            <strong>Dívida:</strong> {person.debtAmount}<br />
            <strong>Data:</strong> {person.debtDueDate}<br />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PersonList;
