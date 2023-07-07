export default function Background({ background }) {
  let text = [];

  for (let lines in background.feature.feature) {
    for (let line in lines) {
      text.push(
        <p>
          {background.feature.feature[line].text}
        </p>
      );
    }
  }

  let proficiencies = [];

  for (let type in background.proficiencies) {
    let profs = background.proficiencies[type];
    if (profs.length !== 0) {
      proficiencies.push(
        <div>
          <h5>
            {type}:
          </h5>
          <div>
            {profs.join(", ")}
          </div>
        </div>
      );
    }
  }

  return (
    <div>
      <h4>
        {background.name}
      </h4>
      <div className="backgroundText">
        {text}
      </div>
      <div className="proficiencies">
        {proficiencies}
      </div>
    </div>
  );
}
