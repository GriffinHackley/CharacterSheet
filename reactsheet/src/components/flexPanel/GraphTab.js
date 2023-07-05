import { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";

export default function GraphTab({ graphInfo }) {
  const [loading, setLoading] = useState(true);

  const data = {
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

  useEffect(() => {
    setLoading(false);
  }, []);

  if (loading) {
    return <h2>Loading...</h2>;
  } else {
    return (
      <section className="damageGraph">
        <Line data={data} options={{}} />
      </section>
    );
  }
}
