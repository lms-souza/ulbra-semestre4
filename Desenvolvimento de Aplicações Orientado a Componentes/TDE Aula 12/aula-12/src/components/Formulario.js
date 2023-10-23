import "./Formulario.css";
import "./Card.css";
import React, { useState } from "react";

function Formulario() {
  const [people, setPeople] = useState([]);
  const [name, setName] = useState("");
  const [egressoConvidado, setEgressoConvidado] = useState("Não");
  const [pago, setPago] = useState("Não");
  const [imageUrl, setImageUrl] = useState("");

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const handleEgressoConvidadoChange = (e) => {
    setEgressoConvidado(e.target.value);
  };

  const handlePagoChange = (e) => {
    setPago(e.target.value);
  };

  const handleImageUrlChange = (e) => {
    setImageUrl(e.target.value);
  };

  const handleCadastrar = () => {
    if (name && imageUrl) {
      const newPerson = {
        name,
        status: egressoConvidado === "Sim" ? "Egresso/Convidado" : "Estudante",
        confirmation: pago === "Sim" ? "Confirmado" : "Não confirmado",
        imageUrl,
      };

      const updatedPeople = [...people, newPerson];
      updatedPeople.sort((a, b) => a.name.localeCompare(b.name));
      setPeople(updatedPeople);

      // Limpar os campos do formulário
      setName("");
      setEgressoConvidado("Não");
      setPago("Não");
      setImageUrl("");
    }
  };

  return (
    <>
      <div className="formulario">
        <h1 className="card-title">Cadastro de Pessoas</h1>
        <div className="nome-input">
          <label>Nome:</label>
          <input
            className="input"
            placeholder="Digite seu Nome"
            type="text"
            value={name}
            onChange={handleNameChange}
          />
        </div>
        <div className="egresso">
          <label>Egresso/Convidado:</label>
          <select
            className="input-egresso"
            value={egressoConvidado}
            onChange={handleEgressoConvidadoChange}
          >
            <option value="Sim">Sim</option>
            <option value="Não">Não</option>
          </select>
        </div>
        <div className="pago">
          <label>Pago:</label>
          <select
            className="input-pago"
            value={pago}
            onChange={handlePagoChange}
          >
            <option value="Sim">Sim</option>
            <option value="Não">Não</option>
          </select>
        </div>
        <div className="url">
          <label>URL da Imagem:</label>
          <input
            className="url-input"
            placeholder="Digite sua ImgURL"
            type="text"
            value={imageUrl}
            onChange={handleImageUrlChange}
          />
        </div>
        <button className="button" onClick={handleCadastrar}>
          Cadastrar
        </button>
      </div>
      
      <div className="all-cards">
        <div className="cards-container">
          {people.map((person, index) => (
            <li key={index} className="card">
              <img src={person.imageUrl} alt={person.name} />
              <p>Nome: {person.name}</p>
              <p>Status: {person.status}</p>
              <p>Confirmação: {person.confirmation}</p>
            </li>
          ))}
        </div>
      </div>
    </>
  );
}

export default Formulario;
