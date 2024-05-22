import { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import { Chart, registerables } from "chart.js";
import axios from "axios";
import { useLocation, useParams } from "react-router-dom";
import Toggles from "../sheet/Toggles";
Chart.register(...registerables);

const sendRequest = async (setLoading, setData, id) => {
  setLoading(true);

  let checked = document.querySelectorAll(".selectorToggle:checked");

  let payload = [];
  checked.forEach(item => payload.push(item.name));

  const response = await axios.post(
    "http://127.0.0.1:8000/api/characters/" + id + "/graph",
    payload
  );

  let data = JSON.parse(response.data);

  setData(data);

  setLoading(false);
};

export default function Graph() {
  const [loading, setLoading] = useState(true);
  const location = useLocation();
  const { graphInfo, toggles } = location.state;
  const { id } = useParams();

  const [graphData, setGraphData] = useState(graphInfo);

  const AC = graphData.AC;
  delete graphData.AC;

  let datasets = [];

  for (let [name, line] of Object.entries(graphData)) {
    datasets.push({
      label: name,
      backgroundColor: "rgb(0, 255, 0)",
      borderColor: "rgb(0, 255, 0)",
      data: line
    });
  }

  const graph = {
    labels: AC,
    datasets: datasets
  };

  useEffect(() => {
    setLoading(false);
  }, []);

  if (loading) {
    return <h2>Loading...</h2>;
  } else {
    return (
      <section className="damageGraph">
        <Line data={graph} options={{}} />
        <Toggles
          togglesInfo={toggles}
          setResponse={setGraphData}
          id={id}
          url={"http://127.0.0.1:8000/api/characters/" + id + "/graph"}
        />
      </section>
    );
  }
}
