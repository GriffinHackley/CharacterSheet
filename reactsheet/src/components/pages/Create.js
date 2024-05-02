import axios from "axios";
import "../../css/pages/Create.css";
import { useState, useEffect } from "react";

const loadOptions = async (setLoading, setOptions) => {
  setLoading(true);

  const response = await axios.get("http://127.0.0.1:8000/api/create");
  let options = JSON.parse(response.data);
  setOptions(options);

  setLoading(false);
};

export default function Create() {
  const [loading, setLoading] = useState(true);
  const [options, setOptions] = useState([]);

  useEffect(() => {
    loadOptions(setLoading, setOptions);
  }, []);

  let list = [];
  for (let option in options) {
    let content = [];
    let choices = options[option];

    for (let choice in choices) {
      content.push(
        <li>
          <div className="choice popout shiftedRight" data-popout="ffhdjkashdf">
            {choices[choice]}
          </div>
        </li>
      );
    }

    list.push(
      <div>
        <h2>
          {option}
        </h2>
        <ul>
          {content}
        </ul>
      </div>
    );
  }

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      {list}
    </div>
  );
}
