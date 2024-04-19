import { useEffect, useState } from "react";
import Selector from "../shared/selector";
import "../../css/plan/ClassChoice.css";
import CollapsibleTab from "../shared/collapsibleTab";

function getPrevMax(selectionList, index) {
  let selection = selectionList[index].name;
  let max = 0;

  if (selection == "") {
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
  selectionList,
  setSelectionList,
  allClasses,
  index
}) {
  let prevMax = getPrevMax(selectionList, index) + 1;
  const [currentSelection, setCurrentSelection] = useState("");
  const [startLevel, setStartLevel] = useState(prevMax);
  const [endLevel, setEndLevel] = useState(prevMax);
  const [features, setFeatures] = useState([]);

  let endSelector = (
    <Selector
      className="endLevel"
      type={"level"}
      choice={prevMax}
      allChoices={[...Array(21).keys()].slice(prevMax)}
      setFunction={setEndLevel}
      showLabel={false}
    />
  );

  useEffect(
    () => {
      const newList = selectionList.map((selection, i) => {
        if (i == index) {
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
        if (i == index) {
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
        />
      );

      if (currentSelection !== "") {
        let temp = [];
        for (let level = newMax; level <= newEnd; level++) {
          let arr = allClasses[currentSelection]["features"][level];
          arr.forEach(feature => {
            temp.push(
              <CollapsibleTab name={feature.name} text={feature.text} />
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
          choice={""}
          allChoices={Object.keys(allClasses)}
          setFunction={setCurrentSelection}
          showLabel={false}
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
