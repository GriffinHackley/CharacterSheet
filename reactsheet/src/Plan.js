import axios from "axios";
import { useParams } from "react-router-dom";
import { React, useState, useEffect } from "react";
import Background from "./components/plan/Background";

const loadPlan = async (setLoading, setPlan, id) => {
  setLoading(true);

  const response = await axios.get(
    `http://127.0.0.1:8000/api/characters/${id}/plan`
  );
  let character = JSON.parse(response.data);
  setPlan(character);

  setLoading(false);
};

export default function Plan() {
  const [loading, setLoading] = useState(true);
  const [plan, setPlan] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    loadPlan(setLoading, setPlan, id);
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  let levels = [];

  levels.push(
    <div className="level">
      <h2>Level 0</h2>
      <Background background={plan[0].Background} />
    </div>
  );

  return (
    <div>
      {levels}
    </div>
  );
}
