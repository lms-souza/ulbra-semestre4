import React, { useState, useEffect } from "react";
import './BuscaCep.css';

function BuscaCEP() {
  const [cep, setCep] = useState("");
  const [endereco, setEndereco] = useState({});
  const [horaAtual, setHoraAtual] = useState("");
  const [mostrarInformacoes, setMostrarInformacoes] = useState(false);

  const handleCEPChange = (e) => {
    setCep(e.target.value);
  };

  const buscarCEP = async () => {
    try {
      const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
      if (!response.ok) {
        throw new Error("CEP não encontrado");
      }
      const data = await response.json();
      setEndereco(data);
      setMostrarInformacoes(true); // Mostrar informações após a busca
    } catch (error) {
      console.error(error);
      setEndereco({});
      setMostrarInformacoes(false); // Ocultar informações em caso de erro
    }
  };

  const hideInformacoes = () => {
    setMostrarInformacoes(false);
  };

  useEffect(() => {
    const intervalId = setInterval(() => {
      const dataAtual = new Date();
      setHoraAtual(dataAtual.toLocaleString());
    }, 1000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <div className="card-container">
      <h1 className="card-title">Busca de CEP</h1>
      <div className="input-container">
        <input
          type="text"
          placeholder="Digite o CEP"
          value={cep}
          onChange={handleCEPChange}
          className="input"
        />
        <button onClick={buscarCEP} className="button">
          Buscar
        </button>
      </div>
      {mostrarInformacoes && (
        <div className="card-content">
          {endereco.cep && (
            <div className="card-data">
              <h2>Dados do CEP:</h2>
              <p>CEP: {endereco.cep}</p>
              <p>Bairro: {endereco.bairro}</p>
              <p>Cidade: {endereco.localidade}</p>
            </div>
          )}
          <button onClick={hideInformacoes} className="buttonInf">
            Ocultar Informações
          </button>
        </div>
      )}
      <div className="hora-container">
        <p className="hora">Hora Atual: {horaAtual}</p>
      </div>
    </div>
  );
}

export default BuscaCEP;