import axios from "axios";
import { useParams } from "react-router-dom";
import { React, useState, useEffect } from "react";
import Ancestry from "../plan/Ancestry";
import Background from "../plan/Background";
import Stats from "../plan/Stats";
import "../../css/pages/Plan.css";
import Classes from "../plan/Classes";

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
      <h1>Level 0</h1>
      <Stats stats={plan[0].stats} />
      <Ancestry ancestries={plan[0].races} />
      <Background backgrounds={plan[0].backgrounds} />
      <Classes classes={plan[1]} />
    </div>
  );

  return (
    <div className="planPage">
      {levels}
    </div>
  );
}
