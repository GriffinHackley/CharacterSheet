new Chart("powerAttackGraph", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [
      {
        label: "Normal",
        data: normalData,
        borderColor: "blue",
        fill: false
      },
      {
        label: "Power Attack",
        data: powerData,
        borderColor: "red",
        fill: false
      }
    ]
  },
  options: {
    maintainAspectRatio: false,
    legend: { display: true },
    animation: false,
    scales: {
      xAxes: [
        {
          display: true,
          scaleLabel: {
            display: true,
            labelString: "Target AC"
          }
        }
      ],
      yAxes: [
        {
          display: true,
          scaleLabel: {
            display: true,
            labelString: "Average Damage"
          }
        }
      ]
    }
  }
});
