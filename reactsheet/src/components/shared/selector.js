function getChoices(type, allChoices, currentChoice) {
  let choices = [];

  let used = false;

  allChoices.forEach(choice => {
    if (choice === currentChoice) {
      used = true;
      choices.push(
        <option value={choice} selected>
          {choice}
        </option>
      );
    } else {
      choices.push(
        <option value={choice}>
          {choice}
        </option>
      );
    }
  });

  if (!used) {
    choices.push(
      <option hidden disabled selected value>
        -- select a {type} --
      </option>
    );
  }

  return choices;
}

export default function Selector({
  type,
  choice,
  allChoices,
  setFunction,
  className,
  showLabel = true
}) {
  let label = null;
  if (showLabel) {
    label = (
      <label for={type + "Choice"}>
        {type}:{" "}
      </label>
    );
  }
  return (
    <div className={className + " selector"}>
      {label}
      <select
        name={type + "Choice"}
        id={type + "Choice"}
        onChange={e => setFunction(e.target.value)}
      >
        {getChoices(type, allChoices, choice)}
      </select>
    </div>
  );
}
