import React from 'react';
import PersonList from './components/PersonList';
import AddPersonForm from './components/AddPersonForm';

import './components/HomePage/HomePage.css'; 

function App() {
  return (
    <><div className="header">
      <h1>Hello Kanastra!</h1>
    </div>
    <div className="body">
      <h2>Sistema de Cadastro Cobranças</h2>
    </div>
    <div>
      <PersonList />
      <AddPersonForm />
    </div>
    </>
  );
}

export default App;
