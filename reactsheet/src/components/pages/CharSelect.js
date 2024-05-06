import axios from "axios";
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const getCharacters = async (setLoading, setCharacters) => {
  setLoading(true);

  const response = await axios.get("http://127.0.0.1:8000/api/characters");
  setCharacters(response.data);

  setLoading(false);
};

export default function CharSelect() {
  const [loading, setLoading] = useState(true);
  const [characters, setCharacters] = useState(true);

  useEffect(() => {
    getCharacters(setLoading, setCharacters);
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  let content = [];

  for (let character in characters) {
    // let id = characters[character].id;
    // let name = characters[character].name;
    let id = character;
    let name = characters[character];
    content.push(
      <li key={id}>
        <Link to={`/character/${id}`}>
          {name}
        </Link>
      </li>
    );
  }
  return (
    <div>
      {content}
    </div>
  );
}
