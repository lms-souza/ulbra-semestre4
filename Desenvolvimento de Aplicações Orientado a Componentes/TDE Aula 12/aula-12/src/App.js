import React from 'react';
import './App.css';
import BuscaCEP from './components/BuscaCep';
import Header from './components/Header';
import Usuario from './components/Usuario';
import Formulario from './components/Formulario';

function App() {
  return (
    <div>
      <div>
        <Header title={"Entrevero"}/>
        <Usuario name={"Leonardo"}/>
        </div>
        <BuscaCEP/>
        
        <div>
          <Formulario/>
        </div>
    </div>
  );
}

export default App;