import "./Formulario.css";
import "./Card.css";
import React, { useState } from "react";

function Formulario() {
  const [people, setPeople] = useState([]);
  const [name, setName] = useState("");
  const [egressoConvidado, setEgressoConvidado] = useState(false);
  const [pago, setPago] = useState(false);
  const [imageUrl, setImageUrl] = useState("");
  const [phone, setPhone] = useState("");
  const [nameError, setNameError] = useState("");
  const [phoneError, setPhoneError] = useState("");

  const handleNameChange = (e) => {
    setName(e.target.value);
    setNameError("");
  };

  const handlePhoneChange = (e) => {
    setPhone(e.target.value);
    setPhoneError("");
  };

  const handleEgressoConvidadoChange = () => {
    setEgressoConvidado(!egressoConvidado);
  };

  const handlePagoChange = () => {
    setPago(!pago);
  };

  const handleImageUrlChange = (e) => {
    setImageUrl(e.target.value);
  };

  const handleCadastrar = () => {
    if (name && phone && imageUrl) {
      const newPerson = {
        name,
        phone,
        status: egressoConvidado ? "Sim" : "Não",
        confirmation: pago ? "Sim" : "Não",
        imageUrl,
      };

      const updatedPeople = [...people, newPerson];
      updatedPeople.sort((a, b) => a.name.localeCompare(b.name));
      setPeople(updatedPeople);

      // Limpar os campos do formulário
      setName("");
      setPhone("");
      setEgressoConvidado(false);
      setPago(false);
      setImageUrl("");
    } else {
      if (!name) {
        setNameError("O campo Nome é obrigatório.");
      }
      if (!phone) {
        setPhoneError("O campo Telefone é obrigatório.");
      }
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
          <p className="error-message">{nameError}</p>
        </div>
        <div className="phone-input">
          <label>Telefone:</label>
          <input
            className="input"
            placeholder="Digite seu Telefone"
            type="text"
            value={phone}
            onChange={handlePhoneChange}
          />
          <p className="error-message">{phoneError}</p>
        </div>
        <div className="egresso">
          <label>Egresso/Convidado:</label>
          <div>
            <input
              type="checkbox"
              checked={egressoConvidado}
              onChange={handleEgressoConvidadoChange}
            />
            <span>Sim</span>
          </div>
          <div>
            <input
              type="checkbox"
              checked={!egressoConvidado}
              onChange={handleEgressoConvidadoChange}
            />
            <span>Não</span>
          </div>
        </div>
        <div className="pago">
          <label>Pago:</label>
          <div>
            <input type="checkbox" checked={pago} onChange={handlePagoChange} />
            <span>Sim</span>
          </div>
          <div>
            <input
              type="checkbox"
              checked={!pago}
              onChange={handlePagoChange}
            />
            <span>Não</span>
          </div>
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
              <p>Telefone: {person.phone}</p>
              <p>Egresso/Convidado: {person.status}</p>
              <p>Pago: {person.confirmation}</p>
            </li>
          ))}
        </div>
      </div>
    </>
  );
}

export default Formulario;
