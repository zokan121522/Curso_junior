import { useState } from "react";

export default function FormularioEmail() {
  const [email, setEmail] = useState("");

  return (
    <div>
      <h3>Email</h3>
      <label>
        <input 
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </label>
      <button disabled={!email.includes("@")}>Enviar</button>
    </div>
  );
}