import { useEffect, useState } from "react";
import Selector from "../shared/Selector";
import "../../css/plan/ClassChoice.css";
import CollapsibleTab from "../shared/collapsibleTab";

function getPrevMax(selectionList, index) {
  let selection = selectionList[index].name;
  let max = 0;

  if (selection === "") {
    return max;
  }

  for (let i = 0; i < index; i++) {
    if (selectionList[i].name !== selection) {
      continue;
    }

    let level = parseInt(selectionList[i].endLevel);

    if (selectionList[i].endLevel > max) {
      max = level;
    } else if (level <= max) {
      //   throw `Selection at index ${i} has an endlevel less than the previous max`;
    }
  }
  return max;
}

export default function ClassChoice({
  def,
  selectionList,
  setSelectionList,
  allClasses,
  index
}) {
  let prevMax = getPrevMax(selectionList, index) + 1;
  if (def.level < prevMax) {
    throw `Invalid class selections for ${def.name}`;
  }
  const [currentSelection, setCurrentSelection] = useState(def.name);
  const [startLevel, setStartLevel] = useState(prevMax);

  const [endLevel, setEndLevel] = useState(def.endLevel);
  const [features, setFeatures] = useState([]);

  let endSelector = (
    <Selector
      className="endLevel"
      type={"level"}
      choice={prevMax > endLevel ? prevMax : endLevel}
      allChoices={[...Array(21).keys()].slice(prevMax)}
      setFunction={setEndLevel}
      showLabel={false}
      index={index}
    />
  );

  useEffect(
    () => {
      const newList = selectionList.map((selection, i) => {
        if (i === index) {
          return {
            name: currentSelection,
            endLevel: getPrevMax(selectionList, index) + 1
          };
        } else {
          return { name: selection.name, endLevel: selection.endLevel };
        }
      });
      setSelectionList(newList);
    },
    [currentSelection]
  );

  useEffect(
    () => {
      const newList = selectionList.map((selection, i) => {
        if (i === index) {
          return {
            name: selection.name,
            endLevel: endLevel
          };
        } else {
          return { name: selection.name, endLevel: selection.endLevel };
        }
      });
      setSelectionList(newList);
    },
    [endLevel]
  );

  useEffect(
    () => {
      const newMax = getPrevMax(selectionList, index) + 1;
      setStartLevel(newMax);

      let newEnd = endLevel;
      if (newEnd < newMax) {
        newEnd = newMax;
        setEndLevel(newEnd);
      }

      endSelector = (
        <Selector
          className="endLevel"
          type={"level"}
          choice={newEnd}
          allChoices={[...Array(21).keys()].slice(newMax)}
          setFunction={setEndLevel}
          showLabel={false}
          index={index}
        />
      );

      if (currentSelection !== "default") {
        let temp = [];
        for (let level = newMax; level <= newEnd; level++) {
          let currentClass = currentSelection;
          if (currentSelection.includes("-")) {
            currentClass = currentClass.split("-")[0];
          }
          let arr = allClasses[currentClass]["features"][level];
          arr.forEach(feature => {
            temp.push(
              <CollapsibleTab
                value={feature.name}
                name={feature.name}
                text={feature.text}
                key={feature.name + "-" + currentClass}
              />
            );
          });
        }
        setFeatures(temp);
      }
    },
    [selectionList]
  );

  return (
    <div className="classChoice">
      <div className="classHeader">
        <Selector
          className={"classSelector"}
          type={"class"}
          choice={currentSelection}
          allChoices={Object.keys(allClasses)}
          setFunction={setCurrentSelection}
          showLabel={false}
          index={index}
        />
        <div className="levels">
          <div>
            {startLevel}
          </div>
          {"--->"}
          {endSelector}
        </div>
      </div>
      {features}
    </div>
  );
}
