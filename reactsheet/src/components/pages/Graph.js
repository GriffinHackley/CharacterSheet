import { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import { Chart, registerables } from "chart.js";
import axios from "axios";
Chart.register(...registerables);

// function getSelectors(characterSelectors) {
//   // Default selectors
//   let defaults = ["advantage", "critical"];

//   let selectors = defaults.concat(characterSelectors);

//   let ret = [];
//   for (let selector in selectors) {
//     selector = selectors[selector];
//     ret.push(
//       <div>
//         <input
//           type="checkbox"
//           className="selectorToggle"
//           id={selector}
//           name={selector}
//           value={selector}
//         />
//         <label for={selector}>
//           {selector}
//         </label>
//       </div>
//     );
//   }

//   return ret;
// }

// const sendRequest = async (setLoading, setData, id) => {
//   setLoading(true);

//   let checked = document.querySelectorAll(".selectorToggle:checked");

//   let payload = [];
//   checked.forEach(item => payload.push(item.name));

//   const response = await axios.post(
//     "http://127.0.0.1:8000/api/characters/" + id + "/graph",
//     payload
//   );

//   let data = JSON.parse(response.data);

//   setData(data);

//   setLoading(false);
// };

export default function Graph({ graphInfo }) {
  const [loading, setLoading] = useState(true);

  let id = 50;

  const graph = {
    labels: graphInfo.AC,
    datasets: [
      {
        label: "Normal",
        backgroundColor: "rgb(0, 255, 0)",
        borderColor: "rgb(0, 255, 0)",
        data: graphInfo.normal
      },
      {
        label: "Power Attack",
        backgroundColor: "rgb(255, 0, 0)",
        borderColor: "rgb(255, 0, 0)",
        data: graphInfo.powerAttack
      }
    ]
  };

  //   let selectors = getSelectors([]);

  useEffect(() => {
    setLoading(false);
  }, []);

  if (loading) {
    return <h2>Loading...</h2>;
  } else {
    return (
      <section className="damageGraph">
        <Line data={graph} options={{}} />
        {/* <div className="selectors">
          {selectors}
        </div>
        <button
          type="button"
          onClick={() => sendRequest(setLoading, setData, id)}
        >
          Submit
        </button> */}
      </section>
    );
  }
}
