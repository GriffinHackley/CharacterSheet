import { useState, useEffect } from "react";
import ClassChoice from "./ClassChoice";

export default function Classes({ classes }) {
  const [classChoiceList, setClassChoiceList] = useState([]);

  let selections = [];
  for (const [name, value] of Object.entries(classes.choice)) {
    let subclassName = classes.all[name]["subclassName"];
    selections.push({
      name: name,
      subclass: value.options[subclassName].choice,
      endLevel: value.level
    });
  }

  const [selectionList, setSelectionList] = useState(selections);

  useEffect(
    () => {
      let choiceList = selectionList.map((selection, index) => {
        return (
          <ClassChoice
            def={selection}
            selectionList={selectionList}
            setSelectionList={setSelectionList}
            allClasses={classes.all}
            index={index}
            key={"classChoice-" + index}
          />
        );
      });
      setClassChoiceList(choiceList);
    },
    [selectionList]
  );

  return (
    <div>
      <h3>Classes</h3>
      <button
        onClick={() =>
          setSelectionList([
            ...selectionList,
            { name: "default", endLevel: -1 }
          ])}
      >
        Add Class
      </button>
      {classChoiceList}
    </div>
  );
}
